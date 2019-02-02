"""CSV file read and write operations."""

import csv
import os
import requests
from tqdm import tqdm

def cannot_overwrite(func):
    def wrapper(path, *arg, **kwarg):
        if os.path.exists(path):
            raise FileExistsError("File already exists: %s" % path)
        return func(path, *arg, **kwarg)
    return wrapper


@cannot_overwrite
def curl(path: str, url: str, max_chunk=None):
    cannot_overwrite(path)
    r = requests.get(url, stream=True)
    iterable = tqdm(r.iter_content(chunk_size=1024), unit=' k')
    with open(path, 'wb') as f:
        i = 0
        for chunk in iterable:
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
            i += 1
            if max_chunk and i >= max_chunk:
                break

CSV_OUTPUT_FORMAT = dict(lineterminator="\n", quoting=csv.QUOTE_MINIMAL)

def yield_rows(path,
               _enc='windows-1251',
               _sep=";"):
    """Emit CSV rows by filename."""
    with open(path, 'r', encoding=_enc) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=_sep)
        for row in spamreader:
            yield row

@cannot_overwrite
def save_rows(path,
              stream,
              column_names=None,
              _fmt=CSV_OUTPUT_FORMAT,
              _enc='utf-8'):
    with open(path, 'w', encoding=_enc) as file:
        writer = csv.writer(file, **_fmt)
        if column_names:
            writer.writerow(column_names)
        writer.writerows(stream)
        