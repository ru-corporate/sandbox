import os
import pandas as pd
from tqdm import tqdm

from boo.file.download import curl
from boo.file.csv import yield_rows, save_rows
from boo.row import Reader
from boo.account.variables import COLUMNS
from boo.settings import is_valid, url, DataFile


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


class Dataset:
    def __init__(self, filepath, columns_dict):
        self.reader = Reader(**columns_dict)
        self.filepath = filepath

    def raw_rows(self):
        return yield_rows(self.filepath)        

    def rows(self):
        return map(self.reader.parse_row, self.raw_rows())

    def dicts(self):
        return map(self.reader.to_dict, self.raw_rows())    
                
       
def colnames(columns_dict):
    return Reader(**columns_dict).colnames


def dtypes(columns_dict):    
    return Reader(**columns_dict).dtypes


@print_year
def build(year, columns_dict=COLUMNS):
    """Преобразовать и сохранить CSV файл для года *year*  используя 
       *columns_dict* для переименования столбцов.

     Возвращает:
        (str) путь к преобразованному CSV файлу
    """    
    _, raw_path, processed_path = args(year)
    cannot_overwrite(processed_path)
    print("Reading and processing CSV file", raw_path)
    _gen = Dataset(raw_path, columns_dict).rows()
    gen = tqdm(_gen, unit=' lines')
    save_rows(processed_path, stream=gen, column_names=colnames(columns_dict))
    print("Saved processed CSV file as", processed_path)
    return processed_path

    
@print_year
def read_dataframe(year, columns_dict=COLUMNS):
    """Прочитать данные из преобразованного файла за год *year*.

    Возвращает:
        (pandas.DataFrame) - фрейм с данными за *year*
    """
    _, _, processed_path = args(year)
    print("Reading processed CSV file", processed_path)
    # FIXME: dtypes() может возвращать типы по загловкам столбцов файла,
    #       column_rename_dict=DEFAULT_LOOKUP_DICT фактически не нужен.
    return _dataframe(processed_path, dtypes=dtypes(columns_dict))


def files(year):
    _, raw_path, processed_path = args(year)
    return dict(raw=str(raw_path), processed=str(processed_path))


def _dataframe(path, dtypes):
    with open(path, 'r', encoding='utf-8') as f:
        return pd.read_csv(f, dtype=dtypes)
