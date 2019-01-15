import pandas as pd

from . import reader
from . import files
from . import row

class Dataset:    
    def __init__(self, year):
        self.year = year
        self.echo = messenger.create(self.year)

    def download(self):
        download.download(self.year)
    
    # COMMENT:
    # prepare() actually takes a list of text and data fields as to be renamed
    # trancates columns by these fields, renames lagging variables 
    # and adds new custom text fields (eg splitting okved to 3 parts,
    # changing the unit of account to '000 rub. some of operations can be 
    # done with pandas
    # performed at columns.py 
    def prepare(self):
        self.echo(f"Saving processed CSV file to %s..." % fn)
        reader.save_rows(self.year)
        self.echo("Done")
        
    def dataframe(self):
        self.echo("Reading dataframe from %s..." % fn)
        return reader.dataframe(self.year)

    def __repr__(self):
        return "Dataset(%s)" % self.year

def save_rows(year)
    fn = files.processed(year)
    files.save_rows(path = fn, stream = rows(year), column_names = row.colnames())

def dataframe(year)
    fn = files.processed(self.year)
    with open(fn, 'r', encoding='utf-8') as f:
        return pd.read_csv(f, dtype=row.dtypes())         