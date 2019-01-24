from pathlib import Path

from boo.file.download import curl
from boo.settings import url

def test_curl():
    curl(url(2012), 'dat.dat', 200)
    p = Path('dat.dat')
    assert p.stat().st_size == 200 * 1024
    p.unlink()
