import pytest
from pathlib import Path

from boo.rename import DEFAULT_LOOKUP_DICT
from boo.read.dataset import Dataset, inn

from boo.file.download import curl, url

#print(next(d.raws()))
#print(next(d.rows()))
#print(next(d.dicts()))

@pytest.fixture
def temp_file():
    filename = 'dat.csv'
    curl(url(2012), filename, 200)
    yield Path(filename)
    Path(filename).unlink()

def test_inn(temp_file):
    d = Dataset(temp_file, DEFAULT_LOOKUP_DICT)
    # the inn is clode to start of file
    x = inn(d.dicts(), 2457009983)
    bool1 = x['cf_oper'] + x['cf_inv'] + x['cf_fin'] == x['cf']
    bool2 = x['tp_capital'] + x['tp_long'] + x['tp_short'] == x['tp']
    bool3 = x['ta_nonfix'] + x['ta_fix'] == x['ta']
    assert all([bool1, bool2, bool3])