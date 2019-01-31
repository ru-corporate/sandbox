"""CSV file read and write operations."""

import csv

CSV_OUTPUT_FORMAT = dict(lineterminator="\n", quoting=csv.QUOTE_MINIMAL)


def yield_rows(path,
               _enc='windows-1251',
               _sep=";"):
    """Emit CSV rows by filename."""
    with open(path, 'r', encoding=_enc) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=_sep)
        for row in spamreader:
            yield row


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