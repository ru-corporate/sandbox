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


fst  = lambda code: code[0]
last = lambda code: code[-1]
trim = lambda code: code[0:-1]

class Colname:
    def __init__(self, text):
        self.prefix = text
        self.postfix = ""
        if fst(text) != "3" and last(text) in ["3", "4"]:
            self.prefix = trim(text)
            if last(text) == "4": 
                self.postfix = "_lag"
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return self.prefix + self.postfix


def change_by_dict(columns, lookup_dict):
    for i, c in enumerate(columns):
        try:
           columns[i].prefix = lookup_dict[c.prefix]
        except KeyError:
            pass
    return columns    


def colnames():
    return change_by_dict([Colname(x) for x in TTL_COLUMNS], RENAME_TEXT)


def filter_by_dict(columns, named_values):
    result = []
    # we need just values in lookup_dict, 'of' in {'1110': 'of'}
    for c in columns:
        if c.prefix in named_values: 
            result.append(c)
    return result     


def to_string(columns):
    return [str(x) for x in columns]


def str_keys(d):
    return {str(k):v for k,v in d.items()}


def long_colnames(lookup_dict):
    return to_string(change_by_dict(colnames(), str_keys(lookup_dict)))


def data_colnames(lookup_dict):    
    a = change_by_dict(colnames(), str_keys(lookup_dict))
    b = filter_by_dict(a, lookup_dict.values())
    return to_string(b)


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