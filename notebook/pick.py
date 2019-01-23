from boo.read import row


def is_financial(df):
    return df.ok1.isin([64, 65, 66, 67])


def operational(df):
    return df[(df['cf'] != 0) & (df['ta'] > 0)]


def dequote(df):
    df = df.copy()  # FIXME: may function above should return a copy
    df.loc[:, 'title'] = df.loc[:, 'title'].apply(
        lambda x: row.dequote(str(x))[1])
    return df


SHORT_NAMES_BY_INN = {
    '2460066195': "РусГидро",
    '4716016979': "ФСК ЕЭС",
    '7702038150': "Московский метрополитен",
    '7721632827': "Концерн Росэнергоатом",
    '7706664260': "Атомэнергопром"
}


def by_title(df, includes_text, excludes_text=None):
    mask = df.title.map(lambda s: includes_text.lower() in s.lower())
    return df[mask]


def reverse(df):
    return df[::-1]


def nlargest(df, key, n):
    return df.sort_values([key], ascending=False).head(n)




# -----------------------------------------------------------------

# df[df.inn == '6320002223'].transpose()

# TODO: сделать текстовую строку с информацией о компании
#       АВТОВАЗ (Открытое акционерное общество)
#       ИНН: 6320002223
#       Регион: 63
#       ОКВЭД:

# TODO: Что такое okpo, okopf, okfs? Чем полезны в анализе?

"""
ok1                                               34
ok2                                               10
ok3                                                2
org                    Открытое акционерное общество
title                                        АВТОВАЗ
region                                            63
inn                                       6320002223
okpo                                        00232934
okopf                                             47
okfs                                              31
unit                                             385
"""


# TODO: сделать представление баланса, ОПУ, ОДДС
#       Каких переменных не хватате для анализа?

# Пример (ОПУ):
"""
sales                                      183217000
profit_oper                                  2736000
exp_interest                                  234000
profit_before_tax                             518000
"""

# TODO: словарь ОПУ, ОДДС

