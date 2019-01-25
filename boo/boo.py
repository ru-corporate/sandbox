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
    print("Downloading from", url)
    curl(url, raw_path)
    print("Saved at", raw_path)
    return raw_path


@print_year
def build(year, lookup_dict=DEFAULT_LOOKUP_DICT):
    _, raw_path, processed_path = args(year)
    cannot_overwrite(processed_path)
    d = Dataset(raw_path, lookup_dict)
    gen = tqdm(d.rows(), unit=' lines')
    print("Reading and processing CSV file", raw_path)
    save_rows(processed_path, stream=gen, column_names=d.colnames)
    # TODO: записываем dtypes https://stackoverflow.com/a/50423394/1758363
    print("Saved processed CSV file as", processed_path)
    return processed_path


@print_year
def read_dataframe(year, lookup_dict=DEFAULT_LOOKUP_DICT):
    _, _, processed_path = args(year)
    print("Reading processed CSV file", processed_path)
    return _dataframe(processed_path, dtypes=dtypes(lookup_dict))


def files(year):
    _, raw_path, processed_path = args(year)
    return dict(raw=str(raw_path), processed=str(processed_path)) 


def _dataframe(path, dtypes):
    with open(path, 'r', encoding='utf-8') as f:
        return pd.read_csv(f, dtype=dtypes)
