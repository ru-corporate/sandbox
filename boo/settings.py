from pathlib import Path

# path to data folder relative to this file 
DATA_FOLDER = "../data"

YEAR_0 = 2012
YEAR_LAST = 2017


def whereami():
    return Path(__file__).parents[0]


def data_folder():
    return whereami().joinpath(DATA_FOLDER).resolve()    


def is_valid(year:int):
    if year not in list(range(YEAR_0, YEAR_LAST+1)):
        raise ValueError("Year not supported: %i" % year)     