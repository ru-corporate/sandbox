from pathlib import Path

# allowed years
YEAR_0 = 2012
YEAR_LAST = 2017

# path to data folder relative to this file
DATA_FOLDER = "../data"


def whereami(x=__file__):
    return Path(x).parents[0]


def resolve_path(input_path):
    return whereami().joinpath(input_path).resolve()


def default_data_folder():
    f = resolve_path(DATA_FOLDER)
    f.mkdir(parents=True, exist_ok=True)
    return f


class DataFile:
    def __init__(self, folder=None):
        if folder is None:
            self.folder = default_data_folder()
        else:
            if folder.exists():
                self.folder = folder
            else:
                raise FileNotFoundError(folder)

    def raw(self, year):
        return self.folder / self.name("rosstat", year)

    def processed(self, year):
        return self.folder / self.name("processed", year)

    def dtype(self, year):
        raise NotImplementedError

    @staticmethod
    def name(tag: str, year: str):
        return f"{tag}-{year}.csv"


SAMPLE_TAG = "sample"


def is_valid(year):
    return year in [SAMPLE_TAG] + list(range(YEAR_0, YEAR_LAST + 1))


def url(year):
    """
    Construct filenames similar to
    http://www.gks.ru/opendata/storage/7708234640-bdboo2012/data-20181029t000000-structure-20121231t000000.csv
    """
    if year == SAMPLE_TAG:
        return "https://raw.githubusercontent.com/ru-corporate/sandbox/master/assets/sample.txt"
    else:
        return ('http://www.gks.ru/opendata/storage/' +
                '7708234640-bdboo{}/'.format(year) +
                'data-20181029t000000-structure-{}1231t000000.csv'.format(year)
                )
