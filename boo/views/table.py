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


def data_variables(header_level=3):
    sections = [
        (balance, "Баланс", header_level),
        (opu, "Отчет о финансовых результатах", header_level),
        (cf_total, "Отчет о движении денежных средств", header_level),
        (cf_oper, "Операционная деятельность", header_level),
        (cf_inv, "Инвестицонная деятельность", header_level),
        (cf_fin, "Финансовая деятельность", header_level)]
    output = []
    for pairs, text, level in sections:
        output.append(header(text, level))
        output.append(table(unpack(pairs), HEADER))
    return newlined(output)
        
       
def registration_variables():
     gen = [(k, whatis(k)) for k in make_text_keys()]
     return(newlined(table_body(gen,
                    th=["Переменная", "Наименование показателя"],
                    midrow=[" :---: ", " :--- "])       
                    )
    )

class Reference:
    reported = data_variables()
    registration = registration_variables()
    
    def __init__(self, *arg, **kwarg):
        pass
    
    def __str__(self):
        return registration_variables() + "\n" + data_variables() 
        

# WONTFIX: may add tables between TABLE and END TABLE    
#from mako.template import Template
#print(Template("hello ${data}!").render(data="world"))    
    