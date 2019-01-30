from boo.account.names import account_name
from boo.account.variables import balance, opu, cf_total, \
    cf_oper, cf_inv, cf_fin, PARSED_FIELDS


HEADER = ["Код отчетности", "Переменная", "Наименование показателя"]
MIDROW = [":------------:", ":--------:", ":----------------------"]


def unpack(pairs):
    return [(p[0], p[1], account_name(p[0])) for p in pairs]


def add_pipes(items):
    return " ".join(["|", " | ".join(items), "|"])


def table_body(gen, th=HEADER):
    return [add_pipes(x) for x in [th] + [MIDROW] + list(gen)]


def header(text, level):
    return "\n%s %s" % ("#" * level, text)


def newlined(gen):
    return "\n".join(gen)


def table(gen, text, level):
    return newlined([header(text, level)] + table_body(gen))


def table_numeric():
    sections = [
        (balance, "Баланс", 3),
        (opu, "Отчет о финансовых результатах", 3),
        (cf_total, "Отчет о движении денежных средств", 3),
        (cf_oper, "Операционная деятельность", 4),
        (cf_inv, "Инвестицонная деятельность", 4),
        (cf_fin, "Финансовая деятельность", 4)]
    for pairs, header, level in sections:
        print(table(unpack(pairs), header, level))
        
        
def table_starts():
    print(newlined(table_body(PARSED_FIELDS, 
                     th=["Переменная", "Тип","Наименование показателя"])))       
