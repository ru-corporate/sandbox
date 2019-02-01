from boo.account.names import account_name
from boo.account.variables import balance, opu, cf_total, cf_oper, cf_inv, cf_fin
from boo.row import make_text_keys
from boo.views.whatis import whatis

HEADER = ["Код отчетности", "Переменная", "Наименование показателя"]
MIDROW = [":------------:", ":--------:", ":----------------------"]

# May use https://github.com/thombashi/pytablewriter#get-rendered-tabular-text-as-str

def add_pipes(items):
    return " ".join(["|", " | ".join(items), "|"])


def table_body(gen, th=HEADER, midrow=MIDROW):
    return [add_pipes(x) for x in [th] + [midrow] + list(gen)]


def header(text, level):
    return "\n%s %s" % ("#" * level, text)


def newlined(gen):
    return "\n".join(gen)


def table(gen, th):
    return newlined(table_body(gen, th))


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
        
       
def table_starts():
     gen = [(k, whatis(k)) for k in make_text_keys()]
     print(newlined(table_body(gen,
                    th=["Переменная", "Наименование показателя"],
                    midrow=[" :---: ", " :--- "])       
                    )
    )
