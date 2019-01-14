import itertools
import pandas as pd

from .util import files
from .util import messenger
from . import columns
from . import row
from . import download

# Actual pipeline is:
# f row.make_dict . row.parse . columns.make_dict0 . files.yield_rows . files.raw
# dicts = f year

def all_rows(year):
    return files.yield_rows(files.raw(year))    

def dicts0(year):
    return map(columns.make_dict0, all_rows(year))

def rows(year):
    return map(row.parse, dicts0(year))
    
def dicts(year):
    return map(row.make_dict, rows(year))

def length(gen):
    return sum(1 for _ in gen)

def slice(year, i, j):
    return list(itertools.islice(dicts(year), i, j))

def nth(year, n):
    return slice(year, n, n+1)[0]

def inn(year, *inns):
    result = []
    inns_ = [str(i) for i in inns]
    for d in dicts(year):
        i = d['inn'] 
        if i in inns_:
            result.append(d)
            inns_.remove(i)
        if inns_==[]:
            break
    if length(result) == 1: 
        return result[0]
    else:
        return result    

def count(year):
    return length(rows(year))

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
        fn = files.processed(self.year)
        self.echo(f"Saving processed CSV file to %s..." % fn)
        files.save_rows(path = fn,
                             stream = self.rows(),
                             column_names = row.colnames())
        self.echo("Done")
        
    def dataframe(self):
        fn = files.processed(self.year)
        self.echo("Reading dataframe from %s..." % fn)
        with open(fn, 'r', encoding='utf-8') as f:
            return pd.read_csv(f, dtype=row.dtypes())    

    def __repr__(self):
        return "Dataset(%s)" % self.year

if __name__ == '__main__':
    n = 6320002223
    x = inn(2012, n)
    bool1 = x['cf_oper'] + x['cf_inv'] + x['cf_fin'] == x['cf']
    bool2 = x['tp_capital'] + x['tp_long'] + x['tp_short'] == x['tp']
    bool3 = x['ta_nonfix'] + x['ta_fix'] == x['ta']
    # cf is not zero
    print ([bool1, bool2, bool3])
