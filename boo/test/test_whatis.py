from boo.views.whatis import whatis

def test_whatis():
 assert whatis("of") == "Основные средства"
 assert whatis("of_lag") == "Основные средства"
 assert whatis("inn") == "ИНН"
 assert whatis("ok1") == "Код ОКВЭД первого уровня"