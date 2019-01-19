from collections import OrderedDict
import itertools

from boo.file.path import raw    
from boo.rename import DEFAULT_LOOKUP_DICT
from boo.read.dataset import Dataset, inn

#print(next(d.raws()))
#print(next(d.rows()))
#print(next(d.dicts()))

def test_inn():
    d = Dataset(raw(2012), DEFAULT_LOOKUP_DICT)
    x = inn(d.dicts(), 2457009983)
    bool1 = x['cf_oper'] + x['cf_inv'] + x['cf_fin'] == x['cf']
    bool2 = x['tp_capital'] + x['tp_long'] + x['tp_short'] == x['tp']
    bool3 = x['ta_nonfix'] + x['ta_fix'] == x['ta']
    assert all([bool1, bool2, bool3])