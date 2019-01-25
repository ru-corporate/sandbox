from boo.read import row
from boo import read_dataframe

try:
    df
except NameError:
    df = read_dataframe(2017)

COLUMNS_1 = ['title', 'ok1', 'region', 'inn']
COLUMNS_RUB = ['ta', 'sales', 'cf', 'cf_oper']
SHORT_NAMES_BY_INN = {
    '2460066195': "РусГидро",
    '4716016979': "ФСК ЕЭС",
    '7702038150': "Московский метрополитен",
    '7721632827': "Концерн Росэнергоатом",
    '7706664260': "Атомэнергопром"
}

def report(df, divide_by, sort_key):
    x = df[COLUMNS_1+COLUMNS_RUB] \
          [is_operational(df)]  \
          .set_index('inn') 
    x = rename(x)
    x.loc[:,COLUMNS_RUB] = x.loc[:,COLUMNS_RUB].divide(divide_by).round(1)
    return x.sort_values(sort_key, ascending=False)


def is_financial(df):
    return df.ok1.isin([64, 65, 66, 67])


def is_operational(df):
    return (df.cf != 0) & (df.ta > 0)


def dequote(df):
    df = df.copy()  # FIXME: may functions above should return a copy
    df.loc[:, 'title'] = df.loc[:, 'title'].apply(
        lambda x: row.dequote(str(x))[1])
    return df



def by_title(df, includes):
    mask = df.title.map(lambda s: includes.lower() in s.lower())
    return df[mask]


def reverse(df):
    return df[::-1]


def nlargest(df, key, n):
    return df.sort_values([key], ascending=False).head(n)

def rename(df, rename_dict=SHORT_NAMES_BY_INN):
    """Rename some titles."""
    ix = df.index.isin(list(rename_dict.keys()))
    df.loc[ix,['title']] = df.loc[ix].index.map(lambda inn: rename_dict[inn])
    return df

