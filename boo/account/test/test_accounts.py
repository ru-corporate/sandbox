from boo.account.names import account_name
from boo.account.sections import account_section


def test_account_name():
    assert account_name(1150) == "Основные средства"
    assert account_name('1150') == "Основные средства"


def test_account_section():
    assert account_section(1150) == "БУХГАЛТЕРСКИЙ БАЛАНС"
    assert account_section('1150') == "БУХГАЛТЕРСКИЙ БАЛАНС"
