from pathlib import Path

from boo.file import curl
from boo.settings import url


def test_curl():
    curl('dat.dat', url(2012), 200)
    p = Path('dat.dat')
    assert p.stat().st_size == 200 * 1024
    p.unlink()
