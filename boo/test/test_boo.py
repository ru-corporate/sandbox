from pathlib import Path
import pandas as pd

from boo.boo import download, build, read_dataframe
from boo.file.path import raw, processed

def delete(path):
    try:
        Path(path).unlink() 
    except FileNotFoundError:
        pass         
   
class Test_Sample_Download:
    
    def setup_method(self):
        delete(raw(0))
        delete(processed(0))

    def teardown_method(self):
        self.setup_method()
        
    def test_download(self):
        fn = download(0)
        assert Path(fn).exists()
    
    def test_build(self):
        download(0)
        fn = build(0)
        assert Path(fn).exists()
    
    def test_build_read_returns_dataframe(self):
        download(0)
        build(0)
        df = read_dataframe(0)
        assert isinstance(df, pd.DataFrame)

    def test_build_read_returns_sum(self):
        download(0)
        build(0)
        df = read_dataframe(0)
        assert sum(df.cf) == -7032726    
    