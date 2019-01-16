from collections import OrderedDict
import itertools
from numpy import int64 

from boo.util import files
from boo.read import row
from boo import rename

INT_TYPE = int64    

class Dataset: 
    def __init__(self, year, lookup_dict=rename.DEFAULT_LOOKUP_DICT):
       self.year = year
       self.parse_row = row.make_row_parser(lookup_dict)
       self.colnames = row.colnames(lookup_dict)       

    def raws(self):
        return files.yield_raw_rows(self.year)    

    def rows(self):
        return map(self.parse_row, self.raws())
        
    def dicts(self):
        def to_dict(row):
            return OrderedDict(zip(self.colnames, row)) 
        return map(to_dict, self.rows())

    @property 
    def dtypes(self):
        """Return types correspoding to self.colnames().
           Used to speed up CSV import. """
        dtype_dict = {k: INT_TYPE for k in self.colnames}
        for key in ['org', 'title', 'region', 'inn',
                    'okpo', 'okopf', 'okfs',
                    'unit']:
            dtype_dict[key] = str
        return dtype_dict

def length(gen):
    return sum(1 for _ in gen)

def slice(gen, i, j):
    return list(itertools.islice(gen, i, j))

def nth(gen, n):
    return slice(gen, n+1)[0]

def inn(year, *inns):
    result = []
    inns_ = [str(i) for i in inns]
    for d in Dataset(year).dicts():
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

if __name__ == '__main__':
    d = Dataset(2012)
    print(next(d.raws()))
    print(next(d.rows()))
    print(next(d.dicts()))
    n = 2457009983
    x = inn(2012, n)
    bool1 = x['cf_oper'] + x['cf_inv'] + x['cf_fin'] == x['cf']
    bool2 = x['tp_capital'] + x['tp_long'] + x['tp_short'] == x['tp']
    bool3 = x['ta_nonfix'] + x['ta_fix'] == x['ta']
    # cf is not zero
    print ([bool1, bool2, bool3])
