from boo.account.sections import account_section

def test_account_section():
    assert account_section(1150) == "БУХГАЛТЕРСКИЙ БАЛАНС"
    assert account_section('1150') == "БУХГАЛТЕРСКИЙ БАЛАНС"
