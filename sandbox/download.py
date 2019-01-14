"""Download CSV file from Rosstat web site."""

import requests
import os
from .util import files 
from .util import messenger


def is_provided(year):
    if year not in list(range(2012, 2017+1)):
        raise ValueError(year)     


def url(year):
    """
    Construct filenames similar to
    http://www.gks.ru/opendata/storage/7708234640-bdboo2012/data-20181029t000000-structure-20121231t000000.csv
    """
    is_provided(year)
    return ('http://www.gks.ru/opendata/storage/' +
            '7708234640-bdboo{}/'.format(year) +
            'data-20181029t000000-structure-{}1231t000000.csv'.format(year)
            )


assert url(2012) == 'http://www.gks.ru/opendata/storage/7708234640-bdboo2012/data-20181029t000000-structure-20121231t000000.csv'


def curl(url: str, path: str):
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)


def download(year: int, force=False):    
    u = url(year) 
    p = util.files.raw(year)
    echo = util.messenger.create(year)
    if os.path.exists(p) and not force:
        echo("Already downloaded", 
             "\n    URL was", u, 
             "\n    Local path is", p)
    else:
        echo("Downloading from", u)
        curl(u, p)
        echo("Saved at", p)


if __name__ == "__main__":
    pass
    #download(2012)
    #download(2013)
    #download(2014)
    #download(2015)
    #download(2016)
    #download(2017)