"""Download CSV file from Rosstat web site."""

import requests
from tqdm import tqdm


def curl(url: str, path: str, max_chunk=None):
    r = requests.get(url, stream=True)

    def _tqdm_curl(iterable): return tqdm(iterable, unit=' k')
    with open(path, 'wb') as f:
        i = 0
        for chunk in _tqdm_curl(r.iter_content(chunk_size=1024)):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
            i += 1
            if max_chunk and i >= max_chunk:
                break
