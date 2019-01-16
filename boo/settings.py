from pathlib import Path

# path to data folder relative to this file 
DATA_FOLDER = "../data"

def whereami():
    return Path(__file__).parents[0]

def data_folder():
    return whereami().joinpath(DATA_FOLDER).resolve()    

def is_valid(year:int):
    if year not in list(range(2012, 2017+1)):
        raise ValueError(year)     