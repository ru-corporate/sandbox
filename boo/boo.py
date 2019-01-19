import pandas as pd
from tqdm import tqdm

from boo.read.dataset import Dataset
from boo.file.path import raw, processed, cannot_overwrite
from boo.file.csv_io import save_rows_to_path
from boo.file.download import url, curl
from boo.logs import messenger
from boo.rename import DEFAULT_LOOKUP_DICT
from boo.settings import is_valid

class Corporate:    
    def __init__(self, year):
        is_valid(year)
        self.year = year
        self.dataset = Dataset(raw(year), DEFAULT_LOOKUP_DICT)
        self.echo = messenger.create(year)


    def download(self):
        p = raw(self.year)
        cannot_overwrite(p)
        u = url(self.year) 
        self.echo("Downloading from", u)
        curl(u, p)
        self.echo("Saved at", p)
    
    def build(self):        
        self.echo("Reading and processing CSV file %s" % raw(self.year))
        save_rows_to_path(processed(self.year), 
                          stream = tqdm(self.dataset.rows(), unit=' lines'), 
                          column_names = self.dataset.colnames)
        self.echo("Saved processed CSV file as %s" % processed(self.year))
        
    def dataframe(self):
        self.echo("Reading dataframe from %s" %  processed(self.year))
        return dataframe(processed(self.year), self.dataset.dtypes)

    def __repr__(self):
        return "Corporate(%s)" % self.year


def dataframe(path, dtypes):
    with open(path, 'r', encoding='utf-8') as f:
        return pd.read_csv(f, dtype=dtypes)
    