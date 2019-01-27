import matplotlib.pyplot as plt
from boo import read_dataframe
import pick

try:
    df
except NameError:
    df = read_dataframe(2017)

try:
    df0
except NameError:
    df0 = pick.filter0(df)

try:
    bs
except NameError:
    bs = pick.nlargest(df0, 'sales', 500)


def ab(t, n=20):
    return df[df.ok1 == t].head(n)


def bln(x):
    return str(round(x / 10**6, 0)).rjust(5)


# print as tables
for b in bs.itertuples():
    print(b.inn, str(b.ok1).rjust(2), bln(b.sales), bln(b.cf_oper),
          round(b.sales / b.ta, 1),
          b.title)


def annotate(cs, x='ta', y='sales'):
    cs = cs.set_index('title')
    fig, ax = plt.subplots()
    cs.plot('ta', 'sales', kind='scatter', ax=ax)
    if annotate:
        # https://stackoverflow.com/questions/15910019/annotate-data-points-while-plotting-from-pandas-dataframe/15911372#15911372
        for k, v in cs.iterrows():
            ax.annotate(k, v)

# ВЫРУЧКА/АКТИВЫ


def tas(bs, a=0, step=10, annotate=True):
    cs = bs[a:a + 20][['ta', 'sales', 'title']]
    annotate(cs)


# Что объясняет отношение объема продаж к активам?
def htas(bs):
    ds = bs.set_index('title')
    sa = (ds.sales / ds.ta).sort_values()
    sa.hist(bins=10)
    print(sa.head(10))
    print(sa.tail(10))


"""Показать связь между типовыми переменными в балансе.

- выручка-объем активов
- выручка-денежный поток от операционной деятельности-изменение
 дебиторки

"""

import boo
df = boo.read_dataframe(2012)

# без крупнейших
subset = df[df.cf != 0][df.ok1 != 67].sort_values('sales')[:-100]
subset.plot(x='sales', y='cash_in_oper_sales', kind='scatter')

# много малых компаний
lim = [0, 0.2 * 10 ** 7]
subset.plot(
    x='sales',
    y='cash_in_oper_sales',
    kind='scatter',
    xlim=lim,
    ylim=lim)

# TODO:
# abline()
