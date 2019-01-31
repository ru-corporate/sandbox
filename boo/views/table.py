from boo.account.names import account_name
from boo.account.variables import balance, opu, cf_total, cf_oper, cf_inv, cf_fin


HEADER = ["Код отчетности", "Переменная", "Наименование показателя"]
MIDROW = [":------------:", ":--------:", ":----------------------"]

# May use https://github.com/thombashi/pytablewriter#get-rendered-tabular-text-as-str

def add_pipes(items):
    return " ".join(["|", " | ".join(items), "|"])


def table_body(gen, th=HEADER):
    return [add_pipes(x) for x in [th] + [MIDROW] + list(gen)]


def header(text, level):
    return "\n%s %s" % ("#" * level, text)


def newlined(gen):
    return "\n".join(gen)


def table(gen, th):
    return newlined(table_body(gen, th))


# TODO: get account name by abbreviation
def unpack(pairs):
    return [(p[0], p[1], account_name(p[0])) for p in pairs]


def table_numeric():
    sections = [
        (balance, "Баланс", 3),
        (opu, "Отчет о финансовых результатах", 3),
        (cf_total, "Отчет о движении денежных средств", 3),
        (cf_oper, "Операционная деятельность", 4),
        (cf_inv, "Инвестицонная деятельность", 4),
        (cf_fin, "Финансовая деятельность", 4)]
    for pairs, text, level in sections:
        print(header(text, level))
        print(table(unpack(pairs), HEADER))
        

# TODO: must relate to rows.make_text_keys()        
# def table_starts():
#     print(newlined(table_body(PARSED_FIELDS[''], 
#           th=["Переменная", "Тип", "Наименование показателя"])))       
