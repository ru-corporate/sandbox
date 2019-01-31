import numpy
from boo.row import dtypes

def test_dtypes():
    assert dtypes(['of']) == {'of': numpy.int64}
    assert dtypes(['ok1']) == {'ok1': numpy.int64}
    assert dtypes(['inn']) == {'inn': str}
    assert dtypes(['okopf']) == {'okopf': str}