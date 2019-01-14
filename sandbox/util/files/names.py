from pathlib import Path


def whereami():
    return Path(__file__).parents[0]


DATA_FOLDER = whereami().parents[0].parents[0]  / 'data'
if not DATA_FOLDER .exists():
    DATA_FOLDER .mkdir(parents=True)


def name(tag, year: int):    
    return f"{tag}-{year}.csv"


def raw(year: int):
    return DATA_FOLDER / name("rosstat", year)


def processed(year: int):
    return DATA_FOLDER / name("processed", year)    
