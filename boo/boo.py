import pandas as pd
from tqdm import tqdm

from boo.read.dataset import Dataset
from boo.read.dtypes import dtypes
from boo.file.path import raw, processed, cannot_overwrite
from boo.file.csv_io import save_rows_to_path
from boo.file.download import url, curl
from boo.rename import DEFAULT_LOOKUP_DICT
from boo.settings import is_valid


def validate(year: int):
    if not is_valid(year):
        raise ValueError("Year not supported: %i" % year)
    print("Year:", year)


def args(year):
    validate(year)
    return url(year), raw(year), processed(year)


def download(year):
    url, raw_path, _ = args(year)
    cannot_overwrite(raw_path)
    print("Downloading from", url)
    curl(url, raw_path)
    print("Saved at", raw_path)
    return raw_path


def build(year, lookup_dict=DEFAULT_LOOKUP_DICT):
    _, raw_path, processed_path = args(year)
    cannot_overwrite(processed_path)
    d = Dataset(raw_path, lookup_dict)
    gen = tqdm(d.rows(), unit=' lines')
    print("Reading and processing CSV file", raw_path)
    save_rows_to_path(processed_path, stream=gen, column_names=d.colnames)
    print("Saved processed CSV file as", processed_path)
    return processed_path


def read_dataframe(year, lookup_dict=DEFAULT_LOOKUP_DICT):
    _, _, processed_path = args(year)
    print("Reading processed CSV file", processed_path)
    return _dataframe(processed_path, dtypes=dtypes(lookup_dict))


def _dataframe(path, dtypes):
    with open(path, 'r', encoding='utf-8') as f:
        return pd.read_csv(f, dtype=dtypes)
