import numpy
from boo.read.dtypes import dtypes

def test_dtypes():
    assert dtypes({'1110': 'of'}) == \
           {'ok1': numpy.int64, 'ok2': numpy.int64,
            'ok3': numpy.int64, 'org': str, 
            'title': str, 'region': str, 
            'inn': str, 'okpo': str, 
            'okopf': str, 'okfs': str, 
            'unit': str, 'of': numpy.int64, 
            'of_lag': numpy.int64}
    
