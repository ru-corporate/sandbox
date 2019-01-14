import matplotlib.pyplot as plt
from sandbox import Dataset

# Начать загрузку если нет
d17 = Dataset(2017)

try:    
  df
except NameError:
  df = d17.dataframe()

try:    
  bs
except NameError:
    bs = df[~df.ok1.isin([64,65,66,67])] \
           [(df.cf != 0) & (df.ta != 0)] \
           .sort_values(['sales'], ascending=False) \
           .head(100) \
           [['title','sales', 'ok1','inn', 'ta', 'unit', 'cf_oper']]

def bln(x):
    return round(x/10**6, 0)
    
# print as tables     
for b in bs.itertuples():
    print (b.inn, str(b.ok1).rjust(2), bln(b.sales), bln(b.cf_oper), 
           round(b.sales/b.ta,1), 
           b.title)

exclude = [
    "7707089648", # КОНЦЕРН "ЛЕВИН"
    "7724204347", # КИТОН 21 ВЕК
    "7710244903", # Межрегиональный общественный Фонд содействия национальной безопасности
    "9717033969", # ИНВЕСТИЦИОНАЯ КОМПАНИЯ ХРОНОС И К
    "7708729065", # ТРЕНД
    "3321019680", # БРИЗ
    "7703428191", # СУХБА
    "7727851751", # ОЛЕФИНИНВЕСТ
    "7723849543", # ЛОГОС
    "5029202249", # ИНОВА
    "0603281577", # ЮГ-ЛЕС
    "5032260402", # СНС-ХОЛДИНГ
    "7709954828", # БИЗНЕСТРАСТ
    "5029202249", # ИНОВА
    "0603281577", # ЮГ-ЛЕС
    ]

# АГРОТОРГ
# https://sbis.ru/contragents/7825706086
# https://www.list-org.com/company/19562
# https://egrul.nalog.ru/index.html


# СТРОИМ ГРАФИКИ

# https://stackoverflow.com/questions/15910019/annotate-data-points-while-plotting-from-pandas-dataframe/15911372#15911372
k = 60
cs = bs[k:k+10][['ta', 'sales','title']]
cs = cs.set_index('title')

fig, ax = plt.subplots()
cs.plot('ta', 'sales', kind='scatter', ax=ax)


for k, v in cs.iterrows():
    ax.annotate(k, v)

# НЕТ ЛИ АНОМАЛИЙ ВЫРУЧКА/АКТИВЫ?
# Что объясняет отношение объема продаж к активам?
ds = bs.set_index('title')
sa = (ds.sales / ds.ta).sort_values()
sa.hist()
print(sa.head(7))
print(sa.tail(7))

# РАЗБИРАЕМ КРУПНЕЙШИЕ ПО ОТРАСЛЯМ
#

