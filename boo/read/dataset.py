from collections import OrderedDict
import itertools

from boo.file.csv_io import yield_rows_by_path
from boo.read.row import colnames, make_row_parser
from boo.read.columns import dtypes


class Parser:
    def __init__(self, lookup_dict):
        self.lookup_dict = lookup_dict
        self._parse = make_row_parser(lookup_dict)
    
    @property
    def colnames(self):
        return colnames(self.lookup_dict)
    
    @property
    def dtypes(self):
        """Return types correspoding to self.colnames().
           Used to speed up CSV import. """
        return dtypes(self.colnames)     
    
    def to_dict(self, row):
         return OrderedDict(zip(self.colnames, row))
     
    def parse_row(self, row):
        return self._parse(row)


class Dataset:
    def __init__(self, filepath, lookup_dict):
        self.filepath = filepath
        self._parser = Parser(lookup_dict)

    def raws(self):
        return yield_rows_by_path(self.filepath)

    def rows(self):
        return map(self._parser.parse_row, self.raws())

    def dicts(self): 
        return map(self._parser.to_dict, self.rows())
    
    def colnames(self):
        return self._parser.colnames


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
