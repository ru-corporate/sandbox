from boo.account.names import account_name
from boo.account.variables import balance, opu, cf_oper, cf_inv, cf_fin 


def row_items(pairs):
    return [(p[0], p[1], account_name(p[0])) for p in pairs]

def row(lst):
    return " ".join(["|", " | ".join(lst), "|"])

def newlined(gen):
    return "\n".join(map(row,gen))

HEADER = ["Код отчетности", "Переменная", "Наименование показателя"]
MIDROW = [":------------:", ":--------:", ":---------------------:"]


def table(gen):
    return newlined([HEADER]+[MIDROW]+row_items(gen))


if __name__ == '__main__':    
    H = "\n###"
    H4 = "\n####"
    print()
    print(H, "Баланс")
    print(table(balance))
    print(H, "Отчет о финансовых результатах")
    print(table(opu))
    print(H, "Отчет о движении денежных средств")
    print(H4, "Операционная деятельность")
    print(table(cf_oper))
    print(H4, "Инвестицонная деятельность")
    print(table(cf_inv))
    print(H4, "Финансовая деятельность")
    print(table(cf_fin))
