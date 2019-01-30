import os
import pandas as pd
from tqdm import tqdm

from boo.file.download import curl
from boo.file.csv import save_rows
from boo.read.dataset import Dataset
from boo.account.variables import DEFAULT_LOOKUP_DICT
from boo.settings import is_valid, url, DataFile
from boo.read.dtypes import dtypes



def cannot_overwrite(path):
    if os.path.exists(path):
        raise FileExistsError("File already exists: %s" % path)


def validate(year):
    if not is_valid(year):
        raise ValueError(f"Year not supported: {year}")


def args(year, data_folder=None):
    validate(year)
    location = DataFile(data_folder)    
    return url(year), location.raw(year), location.processed(year)


def print_year(func):
    def wrapper(year, *arg, **kwarg):        
        print("Year:", year)
        return func(year, *arg, **kwarg)
    return wrapper


@print_year
def download(year):
    url, raw_path, _ = args(year)
    cannot_overwrite(raw_path)
    print("Downloading", url)
    curl(url, raw_path)
    print("Saved as", raw_path)
    return raw_path


@print_year
def build(year, column_rename_dict=DEFAULT_LOOKUP_DICT):
    """Преобразовать и сохранить CSV файл для года *year*
       используя *column_rename_dict* для переименования столбцов 
       исходного файла.

       Преобразование данных:
        - Ввести новые названия столбцов, отражающие смысл переменных отчетности
        - Уменьшить размер файлов за счет удаления пустых и неиспользуемых столбцов
        - Привести все строки к одинаковым единицам измерения (тыс. руб.)
        - Преобразовать отдельные колонки в более удобные: 
            * короткое название компании
            * код ОКВЭД разбить на три уровня
        - Устранить повторы в данных (убрать дублирование по коду ИНН)
        
        Возвращает:
        (str) путь к преобразованному csv файлу
    """    
    _, raw_path, processed_path = args(year)
    cannot_overwrite(processed_path)
    d = Dataset(raw_path, column_rename_dict)
    gen = tqdm(d.rows(), unit=' lines')
    print("Reading and processing CSV file", raw_path)
    save_rows(processed_path, stream=gen, column_names=d.colnames)
    # TODO: записываем dtypes https://stackoverflow.com/a/50423394/1758363
    print("Saved processed CSV file as", processed_path)
    return processed_path


@print_year
def read_dataframe(year, column_rename_dict=DEFAULT_LOOKUP_DICT):
    """Прочитать данные из преобразованного файла за год *year*.

    Возвращает:
        (pandas.DataFrame) - фрейм с данными за *year*
    """    
    _, _, processed_path = args(year)
    print("Reading processed CSV file", processed_path)
    #FIXME: dtypes() может возвращать типы по загловкам столбцов файла,
    #       column_rename_dict=DEFAULT_LOOKUP_DICT фактически не нужен.
    return _dataframe(processed_path, dtypes=dtypes(column_rename_dict))


def files(year):
    _, raw_path, processed_path = args(year)
    return dict(raw=str(raw_path), processed=str(processed_path)) 


def _dataframe(path, dtypes):
    with open(path, 'r', encoding='utf-8') as f:
        return pd.read_csv(f, dtype=dtypes)
