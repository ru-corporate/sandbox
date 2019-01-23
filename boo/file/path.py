import os
from boo.settings import data_folder


def name(tag, year: int):
    return f"{tag}-{year}.csv"


def raw(year: int, loc=data_folder):
    return loc() / name("rosstat", year)


def processed(year: int, loc=data_folder):
    return loc() / name("processed", year)


def cannot_overwrite(path):
    if os.path.exists(path):
        raise FileExistsError("File already exists: %s" % path)
