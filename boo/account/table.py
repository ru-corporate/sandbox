from boo.account.names import account_name
from boo.account.variables import DEFAULT_LOOKUP_DICT, balance, opu, \
                                  cf_oper, cf_inv, cf_fin 



def row_items(pairs):
    return [(p[0], p[1], account_name(p[0])) for p in pairs]

def row(lst):
    return " ".join(["|", " | ".join(lst), "|"])

def newlined(gen):
    return "\n".join(map(row,gen))

header = ["Код отчетности", "Переменная", "Наименование показателя"]
mid = [":---------------:", ":---------------", ":------------------------"]


def table(gen):
    return newlined([header]+[mid]+row_items(opu))
    
H = "###"
print(H, "Баланс")
print(table(balance))
print(H, "Отчет о финансовых результатах")
print(table(opu))
print(H, "Отчет о движении денежных средств")
print(H, "Операционная деятельность")
print(table(cf_oper))
print(H, "Инвестицонная деятельность")
print(table(cf_inv))
print(H, "Финансовая деятельность")
print(table(cf_fin))

# -- Операционная деятельность
# -- Инвестицонная деятельность
# -- Финансовая деятельность