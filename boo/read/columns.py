"""Create column names based on *lookup_dict*."""

from boo.account.variables import TTL_COLUMNS, RENAME_TEXT


def split(text: str):
    fst = lambda text: text[0]
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


def replace(lookup_dict, colname):
    v = colname.prefix
    colname.prefix = lookup_dict.get(v, v)
    return colname


def str_keys(d):
    return {str(k): v for k, v in d.items()}


def change_by_dict(columns, lookup_dict):
    lookup_dict = str_keys(lookup_dict)
    rep = lambda colname: replace(lookup_dict, colname)
    return [rep(c) for c in columns]


def filter_by_dict(columns, lookup_dict):
    named_values = list(lookup_dict.values())
    return [c for c in columns if c.prefix in named_values]


class Colnames:
    def __init__(self, ttl_codes):
        self.colnames = [Colname(x) for x in ttl_codes]

    def rename(self, lookup_dict):
        self.colnames = change_by_dict(self.colnames, lookup_dict)
        return self

    def filter(self, lookup_dict):
        self.colnames = filter_by_dict(self.colnames, lookup_dict)
        return self

    def as_strings(self):
        return [str(x) for x in self.colnames]


def _base_columns():
    return Colnames(TTL_COLUMNS).rename(RENAME_TEXT)

# below are public functions

def base_columns():
    return base_columns().as_strings()


def long_colnames(lookup_dict):
    return _base_columns().rename(lookup_dict).as_strings()


def data_colnames(lookup_dict):
    return _base_columns().rename(lookup_dict).filter(lookup_dict).as_strings()


if __name__ == '__main__':
    print(long_colnames({'1110': 'of'}))
    print(data_colnames({'1110': 'of'}))
    print(data_colnames({1110: 'of'}))
