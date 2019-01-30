from boo.account.table import table_numeric, table_starts


def test_callable():
    table_numeric()
    table_starts()
    assert 1