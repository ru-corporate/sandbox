import pytest
from pathlib import Path
from collections import OrderedDict
import itertools

from boo.account.variables import DEFAULT_LOOKUP_DICT
from boo.read.dataset import Dataset

from boo.file.download import curl
from boo.settings import url


# FIXME: may use raw('sample') fixture
@pytest.fixture
def temp_file():
    # FIXME: must save file to temporary location
    filename = 'dat.csv'
    curl(url(2012), filename, 200)
    yield Path(filename)
    Path(filename).unlink()


def test_inn(temp_file):
    d = Dataset(temp_file, DEFAULT_LOOKUP_DICT)
    # the inn number is close to start of file
    x = inn(d.dicts(), 2457009983)
    bool1 = x['cf_oper'] + x['cf_inv'] + x['cf_fin'] == x['cf']
    bool2 = x['tp_capital'] + x['tp_long'] + x['tp_short'] == x['tp']
    bool3 = x['ta_nonfix'] + x['ta_fix'] == x['ta']
    assert all([bool1, bool2, bool3])


def length(gen):
    return sum(1 for _ in gen)


def slice(gen, i, j):
    return list(itertools.islice(gen, i, j))


def nth(gen, n):
    return slice(gen, n + 1)[0]


def inn(gen, inn):
    inn = str(inn)
    for d in gen:
        if d['inn'] == inn:
            return d

# FIXME: make tests
# print(next(d.raws()))
# print(next(d.rows()))
# print(next(d.dicts()))
