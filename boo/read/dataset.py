
from boo.file.csv_io import yield_rows_by_path
from boo.read.row import RowParser

class Dataset:
    def __init__(self, filepath, lookup_dict):
        self.filepath = filepath
        self.parser = RowParser(lookup_dict)

    def raws(self):
        return yield_rows_by_path(self.filepath)

    def rows(self):
        return map(self.parser.parse_row, self.raws())

    def dicts(self): 
        return map(self.parser.to_dict, self.rows())
        
    @property    
    def colnames(self):
        return self.parser.colnames
        
        
        