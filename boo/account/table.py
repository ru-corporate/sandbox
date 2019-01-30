from boo.account.names import account_name
from boo.account.variables import balance, opu, cf_total, \
                                  cf_oper, cf_inv, cf_fin 


HEADER = ["Код отчетности", "Переменная", "Наименование показателя"]
MIDROW = [":------------:", ":--------:", ":----------------------"]


def row_items(pairs):
    return [(p[0], p[1], account_name(p[0])) for p in pairs]

def add_pipes(lst):
    row = ["|", " | ".join(lst), "|"]
    return " ".join(row)

def table_body(gen):
    return [add_pipes(x) for x in [HEADER] + [MIDROW] + row_items(gen)]

def header(text, level):
    return "\n%s %s" % ("#"*level, text)
    
def newlined(gen):
    return "\n".join(gen)

def table(gen, text, level):
    return newlined([header(text, level)]+table_body(gen))

# WONTFIX: | 4400 | cf | Сальдо денежных потоков за отчетный период |
# Это в последнем разделе, но на само мделе, сальдо по трем предыдущим

if __name__ == '__main__':
    sections = [    
        (balance, "Баланс", 3),
        (opu, "Отчет о финансовых результатах", 3),
        (cf_total, "Отчет о движении денежных средств", 3),
        (cf_oper, "Операционная деятельность", 4),
        (cf_inv, "Инвестицонная деятельность", 4),
        (cf_fin, "Финансовая деятельность", 4)]
    for s in sections:    
        print(table(*s))
    