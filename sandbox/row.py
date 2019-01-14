from collections import OrderedDict
from numpy import int64 

from . import columns 


INT_TYPE = int64
EMPTY = int('0')
QUOTE_CHAR = '"'


# transform numbers
def rub_to_thousand(x: int):
    return int(round(0.001*float(x)))

def mln_to_thousand(x: int):
    return 1000*int(x)

def identity(x):
    return int(x) 

# transform strings
def okved3(code_string: str):
    """Get 3 levels of OKVED codes from *code_string*."""
    codes = [int(x) for x in code_string.split(".")]
    return codes + [EMPTY] * (3-len(codes))


def dequote(name: str):
    """Split company *name* to organisation and title."""
    # Warning: will not work well on company names with more than 4 quotechars
    parts = name.split(QUOTE_CHAR)
    org = parts[0].strip()
    cnt = name.count(QUOTE_CHAR)
    if cnt == 2:
        title = parts[1].strip()
    elif cnt > 2:
        title = QUOTE_CHAR.join(parts[1:])
    else:
        title = name
    return org, title.strip()    


def get_unit_adjuster(unit_name: str):
    mapper = {'383': rub_to_thousand,
              '385': mln_to_thousand,
              '384': identity}
    try:
        return mapper[unit_name]
    except KeyError:
        raise ValueError("Unit not supported: %s" % unit_name)
    

def parse(rowd: OrderedDict, datacols = columns.DATACOLS):
    """Return modified *rowd* as list."""
    # assemble new text columns
    ok1, ok2, ok3 = okved3(rowd['okved'])
    org, title = dequote(rowd['name'])
    region = rowd['inn'][0:2]        
    # text    
    text = [ok1, ok2, ok3,
            org, title, region, rowd['inn'],
            rowd['okpo'], rowd['okopf'], rowd['okfs'],
            rowd['unit']]
    # adjust values to '000 rub 
    func = get_unit_adjuster(unit_name=rowd['unit'])
    data = [func(rowd[k]) for k in datacols]
    return text + data


def colnames(datacols = columns.DATACOLS):
    """Return colnames corresponding to parse_row()."""
    return ['ok1', 'ok2', 'ok3',
            'org', 'title', 'region', 'inn',
            'okpo', 'okopf', 'okfs',
            'unit'] + datacols

COLUMNS_SELECTED = colnames()

def make_dict(row):
    return OrderedDict(zip(COLUMNS_SELECTED, row))

def dtypes(columns = COLUMNS_SELECTED):
    """Return types correspoding to get_colnames().
       Used to speed up CSV import in custom_df_reader(). """
    dtype_dict = {k: INT_TYPE for k in columns}
    for key in ['date', 'org', 'title', 'region', 'inn', 
                'okpo', 'okopf', 'okfs']:
         dtype_dict[key] = str
    return dtype_dict

DTYPES_SELECTED = dtypes()
