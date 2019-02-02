from pathlib import Path

# allowed years
YEAR_0 = 2012
YEAR_LAST = 2017


def whereami(x=__file__):
    return Path(x).parents[0]


def default_data_folder():
    home = Path.home() / ".boo"
    home.mkdir(parents=True, exist_ok=True)
    return home
    

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

    @staticmethod
    def name(tag: str, year: str):
        return f"{tag}-{year}.csv"


def raw_filepath(year):
    return str(DataFile(None).raw(year))


def processed_filepath(year):
    return str(DataFile(None).processed(year))



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
