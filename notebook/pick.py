# Goal:
#    make canonical dataset for further reuse
#
# Solution:
#    import pick
#    pick.make_df()
#
# Risks:
#    truncates too many companies
#    some functions may change state of global variable
#    import boo needs tweaks if boo not installed lacally
#    looks unstable with jupyter notebook

from boo import row
from boo import read_dataframe
from boo.classify.okved import OKVEDv2

BLN = 10 ** 6  # based on thousands
COLUMNS_NONRUB = ['title', 'ok1', 'ok2']
# FIXME: must use all numeric columns
COLUMNS_RUB = ['ta', 'sales', 'cf']
SMALL_SHOW = ['title', 'ok1', 'ok2', 'ta', 'sales']
SHORT_NAMES_BY_INN = {
    '2460066195': "РусГидро",
    '4716016979': "ФСК ЕЭС",
    '7702038150': "Московский метрополитен",
    '7721632827': "Концерн Росэнергоатом",
    '7706664260': "Атомэнергопром"
}


def make_df0(year):
    df = read_dataframe(year)
    n_dups = inn_duplicates(df)
    print(f"Cleared {n_dups} duplicates from dataset. All rows unique.")
    return df.set_index('inn')

# FIXME: very restrictive about columns


def make_df1(year):
    return base_report(make_df0(year))


def inn_duplicates(df, _keep='first'):
    return df[df.duplicated('inn', keep=_keep)].sort_values('inn')[
        ['title', 'inn']]

# FIXME: to_bln() hardcoded


def base_report(df):
    _df = df[COLUMNS_NONRUB + COLUMNS_RUB][is_operational(df)]
    return rename(dequote(to_bln(_df)))


def divide(df, m=1):
    x = df.copy()
    x.loc[:, COLUMNS_RUB] = x.loc[:, COLUMNS_RUB].divide(other=m).round(1)
    return x


def to_bln(df):
    return divide(df, BLN)


def sort(df, key):
    return df.sort_values(key, ascending=False)


def sort_sales(df):
    return sort(df, 'sales')


def sort_ta(df):
    return sort(df, 'ta')


def is_financial(df):
    return df.ok1.isin([64, 65, 66, 67])


def is_operational(df):
    return (df.cf != 0) & (df.ta > 0)


def dequote(df):
    df = df.copy()  # FIXME: may functions above should return a copy
    df.loc[:, 'title'] = df.loc[:, 'title'].apply(
        lambda x: row.dequote(str(x))[1])
    return df


def by_title(df, text):
    mask = df.title.map(lambda s: text.lower() in str(s).lower())
    return df[mask]


def reverse(df):
    return df[::-1]


def nlargest(df, key, n):
    return df.sort_values([key], ascending=False).head(n)


def rename(df, rename_dict=SHORT_NAMES_BY_INN):
    """Rename some titles."""
    ix = df.index.isin(list(rename_dict.keys()))
    df.loc[ix, ['title']] = df.loc[ix].index.map(lambda inn: rename_dict[inn])
    return df


def industry(df, ok1):
    return df[df.ok1 == ok1]


def industry2(df, ok1, ok2):
    return df[(df.ok1 == ok1) & (df.ok2 == ok2)]


def sales_df(df):
    return sort_sales(df)[SMALL_SHOW]


def ta_df(df):
    return sort_sales(df)[SMALL_SHOW]


if __name__ == "__main__":
    try:
        df
    except NameError:
        df = read_dataframe(2017).set_index('inn')

    # 1. Показать крупнейшие компании по продажам и объему активов
    # ============================================================

    base_df = base_report(df)
    sf = sort_sales(base_df)[SMALL_SHOW]
    af = sort_ta(base_df)[SMALL_SHOW]
    n = 5
    print("\nКрупнейшие компании по выручке:")
    print(sf.head(n))
    print("\nКрупнейшие компании по активам:")
    print(af.head(n))

    # - не вычищены финановые компании, у которых большая выручка
    # - есть компании-призраки
    # - не ясно кто сдает ОДДС, а кто нет

    # 2. Сгруппировать по отраслям
    # ============================

    # warnign: this will not hold true for 2012!
    assert set(df.ok1.unique()) == set(OKVEDv2.keys())

    # Напечатать в файл:
    k = 20
    with open("sample.txt", 'w') as f:
        print(f'{k} крупнейших компаний по объему активов', file=f)
        for i in OKVEDv2.keys():
            print("", file=f)
            print(i, OKVEDv2[i], file=f)
            print(industry(af, i).head(k).to_string(line_width=120), file=f)

    # 3. Создать сводный файл по отраслям
    # ================================

    af['n'] = 1
    i = af.groupby('ok1').sum()
    i['industry'] = i.index.map(lambda x: OKVEDv2[x])
    # Фондоотдача
    i['fo'] = i.sales / i.ta
    print(i.sort_values('fo', ascending=False).head(10))
    print(industry(af, 64).head(20))
    i.to_excel("industry.xls")

    # 4. Интересные кейсы
    # ===================

    # все лизинговые компании
    print(industry2(af, 64, 91).head(20))

    # Призраки:
    # 3321019680                                          БРИЗ
    # https://synapsenet.ru/searchorganization/organization/1043301401186-ooo-briz

    # Непонятно:
    # 7708729065                                     ТРЕНД
    # https://www.kommersant.ru/top-100/trend

    # Одна компания в ликвидации
    #

    # 5. Дополнительные данные
    # =======================

    # Налоги
    # https://www.nalog.ru/opendata/7707329152-paytax/
    # https://www.rbc.ru/economics/01/08/2018/5b5f03359a7947d8452f7816
    # Крупнейшие компании
    # http://economy.gov.ru/minec/about/structure/depsectoreconom/2015020801

    # 6. Ликвидационные комиссии
    likv_df = sort(by_title(df, "ликвидационная"), "ta")[
        ["title", "ta"]].head(10)
