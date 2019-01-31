from boo.account.names import account_name

def test_account_name():
    assert account_name(1150) == "Основные средства"
    assert account_name('1150') == "Основные средства"
