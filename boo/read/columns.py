"""Create column names."""

from boo.settings import TTL_COLUMNS

from numpy import int64 
INT_TYPE = int64    


RENAME_TEXT = {'Наименование': 'name',
              'ОКПО': 'okpo',
              'ОКОПФ': 'okopf',
              'ОКФС': 'okfs',
              'ОКВЭД': 'okved',
              'ИНН': 'inn',
              'Код единицы измерения': 'unit',
              'Тип отчета': 'report_type', 
              'Дата актуализации': 'date_published'}


def split(text: str):
    fst  = lambda text: text[0]
    last = lambda text: text[-1]
    trim = lambda text: text[0:-1]
    prefix = text
    postfix = ""
    if fst(text) != "3" and last(text) in ["3", "4"]:
        prefix = trim(text)
        if last(text) == "4": 
            postfix = "_lag"
    return prefix, postfix
    
class Colname:
    def __init__(self, text):
        self.prefix, self.postfix = split(text)
    
    def __str__(self):
        return self.prefix + self.postfix


def change_by_dict(columns, lookup_dict):
    for i, c in enumerate(columns):
        try:
           columns[i].prefix = lookup_dict[c.prefix]
        except KeyError:
            pass
    return columns    


def filter_by_dict(columns, lookup_dict):
    named_values = list(lookup_dict.values())
    result = []
    # we need just values in lookup_dict, 'of' in {'1110': 'of'}
    for c in columns:
        if c.prefix in named_values: 
            result.append(c)
    return result  


def str_keys(d):
    return {str(k):v for k,v in d.items()}

class Colnames:
    def __init__(self, ttl_codes=TTL_COLUMNS):
        self.colnames = change_by_dict([Colname(x) for x in ttl_codes], RENAME_TEXT)
       
    def rename(self, lookup_dict):
        self.colnames = change_by_dict(self.colnames, str_keys(lookup_dict))
        return self
        
    def filter(self, lookup_dict):
        self.colnames = filter_by_dict(self.colnames, str_keys(lookup_dict))
        return self
        
    def as_strings(self):
        return [str(x) for x in self.colnames]      
        
# below are public functions
        
def long_colnames(lookup_dict):
    return Colnames().rename(lookup_dict).as_strings()      


def data_colnames(lookup_dict):    
    return Colnames().rename(lookup_dict).filter(lookup_dict).as_strings()    


def dtypes(colnames):
    """Return types correspoding to long_colnames().
       Used to speed up CSV import. 
    """
    dtype_dict = {k: INT_TYPE for k in colnames}
    for key in ['org', 'title', 'region', 'inn',
                'okpo', 'okopf', 'okfs',
                'unit', 'date_published']:
        if key in colnames:
            dtype_dict[key] = str
    return dtype_dict


if __name__ == '__main__':
    print(long_colnames({'1110':'of'}))    
    print(data_colnames({'1110':'of'}))
    print(data_colnames({1110:'of'}))
    print(dtypes('of ta title'.split(' ')))    