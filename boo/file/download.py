"""Download CSV file from Rosstat web site."""

import requests
from tqdm import tqdm


def url(year):
    """
    Construct filenames similar to
    http://www.gks.ru/opendata/storage/7708234640-bdboo2012/data-20181029t000000-structure-20121231t000000.csv
    """
    return ('http://www.gks.ru/opendata/storage/' +
            '7708234640-bdboo{}/'.format(year) +
            'data-20181029t000000-structure-{}1231t000000.csv'.format(year)
            )

def curl(url: str, path: str, max_chunk=None):
    r = requests.get(url, stream=True)
    _tqdm_curl = lambda iterable: tqdm(iterable, unit=' k')
    with open(path, 'wb') as f:
        i = 0
        for chunk in _tqdm_curl(r.iter_content(chunk_size=1024)):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
            i += 1
            if max_chunk and i >= max_chunk:
                break

#if __name__ == "__main__":
#    from pathlib import Path
#    assert url(2012) == 'http://www.gks.ru/opendata/storage/7708234640-bdboo2012/data-20181029t000000-structure-20121231t000000.csv'
#    u = url(2012)
#    curl(u, 'dat.dat', 200)
#    p = Path('dat.dat')
#    assert p.stat().st_size == 200 * 1024
#    p.unlink()             