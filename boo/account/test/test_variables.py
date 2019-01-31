from boo.account.variables import split, COLUMNS


def test_columns_all_has_length_266():
    assert len(COLUMNS['all_columns']) == 266

def test_columns_text():
    assert COLUMNS['text_columns'] == ['name',
                                       'okpo',
                                       'okopf',
                                       'okfs',
                                       'okved',
                                       'inn',
                                       'unit',
                                       'report_type',
                                       'date_published']


def test_split():
    assert split('12603') == dict(code='1260', is_lagged=False)
    assert split('12604') == dict(code='1260', is_lagged=True)
    assert split('33255') == dict(code='33255', is_lagged=False)


if __name__ == "__main__":
    import pytest
    pytest.main(__file__)
