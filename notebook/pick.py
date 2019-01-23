from boo.read import row
from boo import read_dataframe

try:
    df
except NameError:
    df = read_dataframe(2017)


def is_financial(df):
    return df.ok1.isin([64, 65, 66, 67])


def operational(df):
    return df[(df['cf'] != 0) & (df['ta'] > 0)]


def dequote(df):
    df = df.copy()  # FIXME: may functions above should return a copy
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
