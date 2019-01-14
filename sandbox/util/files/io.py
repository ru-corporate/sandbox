"""Generic CSV file read and write operations."""

import csv
import os

FMT = dict(lineterminator="\n", quoting=csv.QUOTE_MINIMAL)


def yield_rows(path, enc='windows-1251', sep=";"):
    """Emit CSV rows by filename."""
    with open(path, 'r', encoding=enc) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=sep)
        for row in spamreader:
            yield row


def _open(path): 
    return open(path, 'w', encoding="utf-8")


def save_rows(path, stream, column_names=None):
    with _open(path) as file:
        writer = csv.writer(file, **FMT)
        if column_names:
            writer.writerow(column_names)
        writer.writerows(stream)


def save_dicts(path, dict_stream, column_names):
    if os.path.exists(path):
        raise Exception("%s already exists" % path)
    with _open(path) as file:
        writer = csv.DictWriter(file, fieldnames=column_names, **FMT)
        for d in dict_stream: 
            writer.writerow(d)
            