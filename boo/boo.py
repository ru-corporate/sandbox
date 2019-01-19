import pandas as pd
from tqdm import tqdm

from boo.read import reader
from boo.util import files
from boo.util import download
from boo.util import messenger
from boo import rename


class Corporate:    
    def __init__(self, year):
        self.year = year
        self.echo = messenger.create(year)
        self.d = reader.Dataset(year, rename.DEFAULT_LOOKUP_DICT)
        self.path = files.processed_path(year)

    def download(self):
        download.download(self.year)
    
    def build(self):        
        self.echo("Saving processed CSV file to %s..." % self.path)
        files.save_rows(self.year, 
                        stream = tqdm(self.d.rows(), unit=' lines'), 
                        column_names = self.d.colnames)
        self.echo("Done")
        
    def dataframe(self):
        self.echo("Reading dataframe from %s..." % self.path )
        return dataframe(self.path, self.d.dtypes)

    def __repr__(self):
        return "Corporate(%s)" % self.year


def dataframe(fn, dtypes):
    with open(fn, 'r', encoding='utf-8') as f:
        return pd.read_csv(f, dtype=dtypes)
    