from pathlib import Path
import pandas as pd
import pytest
#import tempfile
#f = tempfile.gettempdir()

from boo.boo import download, build, read_dataframe, validate, print_year
from boo.settings import DataFile, raw_filepath, processed_filepath


def test_validate_wrong():
    with pytest.raises(ValueError):
        validate(1990)


@print_year
def nothing(year):
    pass


def test_print_year_is_callable():
    nothing(2012)
    assert True


def delete(path):
    try:
        Path(path).unlink()
    except FileNotFoundError:
        pass


class Test_Sample_Download:

    def setup_method(self):
        delete(raw_filepath("sample"))
        delete(processed_filepath("sample"))    

    def teardown_method(self):
        self.setup_method()

    def test_pipeline(self):
        delete(raw_filepath("sample"))
        import os
        assert not os.path.exists("C:\\Users\\Евгений\\.boo\\rosstat-sample.csv")
        fn1 = download("sample")
        assert Path(fn1).exists()
        fn2 = build("sample")
        assert Path(fn2).exists()
        df = read_dataframe("sample")
        assert isinstance(df, pd.DataFrame)
        assert sum(df.cf) == -7032726
