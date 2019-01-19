"""Generic CSV file read and write operations."""

import csv
import os

FMT = dict(lineterminator="\n", quoting=csv.QUOTE_MINIMAL)


def yield_rows_by_path(path, enc='windows-1251', sep=";"):
    """Emit CSV rows by filename."""
    with open(path, 'r', encoding=enc) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=sep)
        for row in spamreader:
            yield row


def wopen(path): 
    return open(path, 'w', encoding="utf-8")


def does_not_exist(path):        
    if os.path.exists(path):
        raise FileExistsError("File already exists: %s" % path)
    
    
def save_rows_to_path(path, stream, column_names=None):
    does_not_exist(path)
    with wopen(path) as file:
        writer = csv.writer(file, **FMT)
        if column_names:
            writer.writerow(column_names)
        writer.writerows(stream)


def save_dicts_to_path(path, dict_stream, column_names):
    does_not_exist(path)
    with wopen(path) as file:
        writer = csv.DictWriter(file, fieldnames=column_names, **FMT)
        for d in dict_stream: 
            writer.writerow(d)