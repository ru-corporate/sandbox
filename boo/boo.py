import pandas as pd
from tqdm import tqdm

from boo.account.variables import COLUMNS
from boo.file import curl, yield_rows, save_rows
from boo.row import Reader
from boo.settings import is_valid, url, raw_filepath, processed_filepath


def validate(year):
    if not is_valid(year):
        raise ValueError(f"Year not supported: {year}")


def print_year(func):
    def wrapper(year, *arg, **kwarg):
        validate(year)
        print("Year:", year)
        return func(year, *arg, **kwarg)
    return wrapper


@print_year
def download(year):
    path, _url = raw_filepath(year), url(year), 
    print("Downloading", url)
    curl(path, _url)
    print("Saved as", path)
    return path


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

    @property
    def colnames(self):
        return self.reader.colnames


# FIXME: dtypes() может возвращать типы по загловкам столбцов файла,
#       column_rename_dict=DEFAULT_LOOKUP_DICT фактически не нужен.
def dtypes(columns_dict=COLUMNS):    
    return Reader(**columns_dict).dtypes


@print_year
def build(year, columns_dict=COLUMNS):
    """Преобразовать и сохранить CSV файл для года *year*  используя 
       *columns_dict* для переименования столбцов.

     Возвращает:
        (str) путь к преобразованному CSV файлу
    """    
    raw_path, processed_path = raw_filepath(year), processed_filepath(year)
    print("Reading and processing CSV file", raw_path)
    d = Dataset(raw_path, columns_dict)
    gen = tqdm(d.rows(), unit=' lines')
    save_rows(processed_path, stream=gen, column_names=d.colnames)
    print("Saved processed CSV file as", processed_path)
    return processed_path

    
@print_year
def read_dataframe(year, columns_dict=COLUMNS):
    """Прочитать данные из преобразованного файла за год *year*.

    Возвращает:
        (pandas.DataFrame) - фрейм с данными за *year*
    """
    path = processed_filepath(year)
    print("Reading processed CSV file", path)
    return _dataframe(path, dtypes=dtypes(columns_dict))


def _dataframe(path, dtypes):
    with open(path, 'r', encoding='utf-8') as f:
        return pd.read_csv(f, dtype=dtypes)
