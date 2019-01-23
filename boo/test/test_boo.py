from pathlib import Path
import pandas as pd
import pytest

from boo.boo import download, build, read_dataframe, validate
from boo.file.path import raw, processed


def test_validate_wrong():
    with pytest.raises(ValueError):
        validate(1990)


def delete(path):
    try:
        Path(path).unlink()
    except FileNotFoundError:
        pass


class Test_Sample_Download:

    def setup_method(self):
        delete(raw("sample"))
        delete(processed("sample"))

    def teardown_method(self):
        self.setup_method()

    def test_pipeline(self):
        fn1 = download("sample")
        assert Path(fn1).exists()
        fn2 = build("sample")
        assert Path(fn2).exists()
        df = read_dataframe("sample")
        assert isinstance(df, pd.DataFrame)
        assert sum(df.cf) == -7032726
