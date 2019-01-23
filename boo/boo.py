import os
import pandas as pd
from tqdm import tqdm

from boo.read.dataset import Dataset
from boo.read.dtypes import dtypes
from boo.file.path import raw, processed
from boo.file.csv_io import save_rows_to_path
from boo.file.download import url, curl
from boo.rename import DEFAULT_LOOKUP_DICT
from boo.settings import is_valid


def cannot_overwrite(path):
    if os.path.exists(path):
        raise FileExistsError("File already exists: %s" % path)


def validate(year):
    if not is_valid(year):
        raise ValueError(f"Year not supported: {year}")


def args(year):
    return url(year), raw(year), processed(year)


def print_year(func):
   def func_wrapper(year, *arg, **kwarg):
       validate(year)
       print ("Year:", year)
       return func(year, *arg, **kwarg)
   return func_wrapper


@print_year
def download(year):
    url, raw_path, _ = args(year)
    cannot_overwrite(raw_path)
    print("Downloading from", url)
    curl(url, raw_path)
    print("Saved at", raw_path)
    return raw_path

@print_year
def nothing(year):
       pass

@print_year
def build(year, lookup_dict=DEFAULT_LOOKUP_DICT):
    _, raw_path, processed_path = args(year)
    cannot_overwrite(processed_path)
    d = Dataset(raw_path, lookup_dict)
    gen = tqdm(d.rows(), unit=' lines')
    print("Reading and processing CSV file", raw_path)
    save_rows_to_path(processed_path, stream=gen, column_names=d.colnames)
    #TODO: записываем dtypes https://stackoverflow.com/a/50423394/1758363
    print("Saved processed CSV file as", processed_path)
    return processed_path


@print_year
def read_dataframe(year, lookup_dict=DEFAULT_LOOKUP_DICT):
    _, _, processed_path = args(year)
    print("Reading processed CSV file", processed_path)
    return _dataframe(processed_path, dtypes=dtypes(lookup_dict))


def _dataframe(path, dtypes):
    with open(path, 'r', encoding='utf-8') as f:
        return pd.read_csv(f, dtype=dtypes)