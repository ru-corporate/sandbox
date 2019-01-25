from boo.settings import url


def test_url():
    assert url(2012) == 'http://www.gks.ru/opendata/storage/7708234640-bdboo2012/data-20181029t000000-structure-20121231t000000.csv'


def test_url_on_string():
    assert url("sample")
