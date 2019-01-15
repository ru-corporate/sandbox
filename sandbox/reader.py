from collections import OrderedDict
import itertools

try:
    from .util import files
    from . import columns
    from . import row
except ImportError:
    import util.files
    import columns
    import row
    

def length(gen):
    return sum(1 for _ in gen)

class Dataset: 
    def __init__(self, year, lookup_dict):
       self.year = year
       self.make_row = row.make_row_parser(lookup_dict)
       self.columns = columns.new_names(lookup_dict)

    def all_rows(self):
        return files.yield_rows(files.raw(self.year))    

    def rows(self):
        return map(self.make_row, self.all_rows())
        
    def dicts(self):
        def to_dict(row):
            return OrderedDict(self.columns, row) 
        return map(to_dict, self.all_rows())

    def slice(self, i, j):
        return list(itertools.islice(self.dicts(), i, j))

    def nth(self, n):
        return self.slice(n, n+1)[0]

    def inn(self, *inns):
        result = []
        inns_ = [str(i) for i in inns]
        for d in self.dicts():
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

    def count(self):
        return length(self.rows())

if __name__ == '__main__':
    d = Dataset(2012, {""})
    n = 6320002223
    x = inn(2012, n)
    bool1 = x['cf_oper'] + x['cf_inv'] + x['cf_fin'] == x['cf']
    bool2 = x['tp_capital'] + x['tp_long'] + x['tp_short'] == x['tp']
    bool3 = x['ta_nonfix'] + x['ta_fix'] == x['ta']
    # cf is not zero
    print ([bool1, bool2, bool3])
