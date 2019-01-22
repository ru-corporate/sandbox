from numpy import int64 
INT_TYPE = int64  

from boo.read import row

def dtypes(lookup_dict):
    """Return types correspoding to column.long_colnames().
       Used to speed up CSV import. 
    """
    colnames = row.colnames(lookup_dict)
    dtype_dict = {k: INT_TYPE for k in colnames}
    for key in ['org', 'title', 'region', 'inn',
                'okpo', 'okopf', 'okfs',
                'unit', 'date_published']:
        if key in colnames:
            dtype_dict[key] = str
    return dtype_dict

if __name__ == '__main__':
    print(dtypes({'1110': 'of'}))    