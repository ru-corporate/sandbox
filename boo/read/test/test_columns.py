import numpy
from boo.read import columns

def test_data_colnames_on_int():
    assert columns.data_colnames({1110: 'of'}) == ['of', 'of_lag']

def test_data_colnames_on_string():    
    assert columns.data_colnames({'1110': 'of'}) == ['of', 'of_lag']

def test_long_colnames_on_int():
    assert columns.long_colnames({1110:'of'})   

def test_long_colnames_on_string():    
    assert columns.long_colnames({'1110':'of'})    

def test_Colname():    
    columns.Colname('12603').prefix = '1260'
    columns.Colname('12603').postfix = ''
    columns.Colname('12604').postfix = '_lag'
    columns.Colname('33255').prefix = '33255'   
    
    
if __name__ == "__main__":
    import pytest
    pytest.main(__file__)