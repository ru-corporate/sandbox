"""Create column names based on *lookup_dict*."""

from boo.account.variables import TTL_COLUMNS, RENAME_TEXT


def split(text: str):
    def fst(text): return text[0]

    def last(text): return text[-1]

    def trim(text): return text[0:-1]
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

    def modify_prefix(self, lookup_dict):
        v = self.prefix
        self.prefix = lookup_dict.get(v, v)
        return self


class Colnames:
    def __init__(self, ttl_codes):
        self.array = [Colname(x) for x in ttl_codes]

    def rename(self, lookup_dict):
        self.array = [x.modify_prefix(lookup_dict) for x in self.array]
        return self

    def filter(self, lookup_dict):
        _names = list(lookup_dict.values())
        self.array = [c for c in self.array if c.prefix in _names]
        return self

    def as_strings(self):
        return list(map(str, self.array))

# -- все буквенные переменные переименовали (делается всегда)


def root():
    return Colnames(TTL_COLUMNS).rename(lookup_dict=RENAME_TEXT)

# below are public functions


def base_columns():
    return root().as_strings()

# -- переименовали числовые переменные


def long_colnames(lookup_dict):
    return root().rename(lookup_dict).as_strings()

# -- переименовали числовые переменные и оставили только их


def data_colnames(lookup_dict):
    return root().rename(lookup_dict).filter(lookup_dict).as_strings()


if __name__ == '__main__':
    print(long_colnames({'1110': 'of'}))
    print(data_colnames({'1110': 'of'}))
