from collections import OrderedDict
import itertools

from boo.file.csv_io import yield_rows_by_path
from boo.read.row import colnames, make_row_parser
from boo.read.columns import dtypes


class Dataset:
    def __init__(self, filepath, lookup_dict):
        self.filepath = filepath
        self.lookup_dict = lookup_dict
        self.colnames = colnames(lookup_dict)

    def raws(self):
        return yield_rows_by_path(self.filepath)

    def rows(self):
        parse_row = make_row_parser(self.lookup_dict)
        return map(parse_row, self.raws())

    def dicts(self): 
        def to_dict(row):
            return OrderedDict(zip(self.colnames, row))    
        return map(to_dict, self.rows())

    @property
    def dtypes(self):
        """Return types correspoding to self.colnames().
        Used to speed up CSV import. """
        return dtypes(self.colnames) 


def length(gen):
    return sum(1 for _ in gen)


def slice(gen, i, j):
    return list(itertools.islice(gen, i, j))


def nth(gen, n):
    return slice(gen, n+1)[0]


def inn(gen, *inns):
    result = []
    inns_ = [str(i) for i in inns]
    for d in gen:
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

#TODO: move to tests
if __name__ == '__main__':
    from boo.file.path import raw    
    from boo.rename import DEFAULT_LOOKUP_DICT
    d = Dataset(raw(2012), DEFAULT_LOOKUP_DICT)
    print(next(d.raws()))
    print(next(d.rows()))
    print(next(d.dicts()))
    x = inn(d.dicts(), 2457009983)
    bool1 = x['cf_oper'] + x['cf_inv'] + x['cf_fin'] == x['cf']
    bool2 = x['tp_capital'] + x['tp_long'] + x['tp_short'] == x['tp']
    bool3 = x['ta_nonfix'] + x['ta_fix'] == x['ta']
    # cf is not zero
    print ([bool1, bool2, bool3])
