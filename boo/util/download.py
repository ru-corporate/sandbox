"""Download CSV file from Rosstat web site."""

import requests
from tqdm import tqdm

from boo.util import files
from boo.util import  messenger
from boo import settings


def url(year):
    """
    Construct filenames similar to
    http://www.gks.ru/opendata/storage/7708234640-bdboo2012/data-20181029t000000-structure-20121231t000000.csv
    """
    settings.is_valid(year)
    return ('http://www.gks.ru/opendata/storage/' +
            '7708234640-bdboo{}/'.format(year) +
            'data-20181029t000000-structure-{}1231t000000.csv'.format(year)
            )


assert url(2012) == 'http://www.gks.ru/opendata/storage/7708234640-bdboo2012/data-20181029t000000-structure-20121231t000000.csv'


def tqdm_curl(iterable):
    return tqdm(iterable, unit=' k')

def curl(url: str, path: str, max_chunk=None):
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        i = 0
        for chunk in tqdm_curl(r.iter_content(chunk_size=1024)):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
            i += 1
            if max_chunk and i >= max_chunk:
                break

#For testing
#u = url(year)
#curl(u, 'dat.dat', 200)

def download(year: int):    
    p = files.raw_path(year)
    files.does_not_exist(p)
    u = url(year) 
    echo = messenger.create(year)
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