"""Показать связь между типовыми переменными в балансе."""

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
