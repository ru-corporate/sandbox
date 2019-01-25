class Company:
    def __init__(self, row):
        self.row = row

    @property
    def name(self):
        return f"{self.row.title} ({self.row.org})"

    @property
    def region(self):
        return f"Регион: {self.row.region}"

    @property
    def inn(self):
        return f"ИНН: {self.row.inn}"

    @property
    def okved(self):
        # FIXME: refactor
        return f"ОКВЭД: {str(self.row.ok1).zfill(2)}.{str(self.row.ok2).zfill(2)}.{str(self.row.ok3).zfill(2)}"

    @property
    def bal(self):
        return "\n".join([screen("Активы всего    ", self.row.ta),
                          screen("  оборотные     ", self.row.ta_nonfix),
                          screen("  внеоборотные  ", self.row.ta_fix),
                          screen("Пассивы всего   ", self.row.tp),
                          screen("  капитал       ", self.row.tp_capital),
                          screen("  краткосрочные ", self.row.tp_short),
                          screen("  долгосрочные  ", self.row.tp_long),
                          screen("Выручка         ", self.row.sales),
                          screen("Прибыль         ", self.row.profit_before_tax),
                          screen("Денежный поток  ", self.row.cf),
                          screen("  опер.         ", self.row.cf_oper),
                          screen("  фин.          ", self.row.cf_fin),
                          screen("  инв.          ", self.row.cf_inv),



                          ]

                         )

    def __str__(self):
        ids = "  ".join([self.inn, self.okved])
        return "\n".join([self.name, ids, self.bal])

    def __repr__(self):
        return str(self)


def screen(name, x):
    x = format(x, '_').replace("_", " ")
    return f"{name}    {x:>12}"


from random import randint
i = randint(0, 10000)


def ith(df, i):
    return df.iloc[i, :]


def rnd(df):
    i = randint(0, df.shape[0])
    return df.iloc[i, :]


if __name__ == "__main__":
    z = Company(rnd(df[df.cf != 0]))
    print(z)


"""
5409110820
ПРИХОД В ЧЕСТЬ ИКОНЫ БОЖИЕЙ МАТЕРИ "КАЗАНСКАЯ" ГОРОДА НОВОСИБИРСКА (ПЕРВОМАЙСКИЙ РАЙОН)" НОВОСИБИРСКОЙ ЕПАРХИИ РУССКОЙ ПРАВОСЛАВНОЙ ЦЕРКВИ (МЕСТНАЯ ПРАВОСЛАВНАЯ РЕЛИГИОЗНАЯ ОРГАНИЗАЦИЯ)

Ликвидационная комиссия
КЛЮЧЕВОЙ ЭЛЕМЕНТ (Ликвидационная комиссия ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ)

ФЕДЕРАЦИЯ БОКСА ГОРОДА САЯНСКА (ОБЩЕСТВЕННАЯ ОРГАНИЗАЦИЯ)

БЕЗОТКАТНЫЕ ПЕРЕВОЗКИ (ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ)
Регион 22
   ИНН 2221219242

КЛЕВЕР (Общество с ограниченной ответственностью)
Регион 59
   ИНН 5902014988

РОМАШКА (САДОВОДЧЕСКОЕ И ОГОРОДНИЧЕСКОЕ НЕКОММЕРЧЕСКОЕ ТОВАРИЩЕСТВО ГРАЖДАН)
   ИНН 0269009842


АВТОПРОМ (ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ)
   ИНН 7106068192
Регион 71
 ОКВЭД 45.11.2
Активы всего       453673
Пассивы всего      453673
Выручка            99319
Прибьль            858
Денежный поток     -6122
  опер.            0
  фин.             -14266
  инв.             8144

КОМПАНИЯ ВИТА-ЛАЙН (АКЦИОНЕРНОЕ ОБЩЕСТВО)
   ИНН 7710416207
Регион 77
 ОКВЭД 64.99.1
Активы всего       128558
Пассивы всего      128558
Выручка            0
Прибьль            -603
Денежный поток     -10
  опер.            -509
  фин.             -299
  инв.             798

ОКИНАВА (ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ)
   ИНН 5612085088
Регион 56
 ОКВЭД 45.1.0
Активы всего       119835
Пассивы всего      119835
Выручка            238374
Прибьль            -7975
Денежный поток     1723
  опер.            -9766
  фин.             11170
  инв.             319


ЭВЕРЕСТ (ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ)
   ИНН 7727707469
Регион 77
 ОКВЭД 93.29.0
Активы всего       47216
Пассивы всего      47216
Выручка            30981
Прибьль            2869
Денежный поток     4062
  опер.            4062
  фин.             0
  инв.             0


ДОМОСТРОИТЕЛЬНЫЙ КОМБИНАТ № 1 (АКЦИОНЕРНОЕ ОБЩЕСТВО)
   ИНН 7714046959
Регион 77
 ОКВЭД 41.20.0
Активы всего       33502133
Пассивы всего      33502133
Выручка            30942195
Прибьль            84777
Денежный поток     327902
  опер.            -56369
  фин.             -492808
  инв.             877079

АРХАНГЕЛЬСКИЙ РЕГИОНАЛЬНЫЙ РАДИОТЕЛЕВИЗИОННЫЙ ПЕРЕДАЮЩИЙ ЦЕНТР (ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ)
   ИНН 2926011074
Регион 29
 ОКВЭД 60.10.0
Активы всего       60002
Пассивы всего      60002
Выручка            0
Прибьль            -6
Денежный поток     -75
  опер.            -453
  фин.             0
  инв.             378

ОКТОБЛУ (ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ)
   ИНН 5029086747
Регион 50
 ОКВЭД 47.19.0
Активы всего       7855867
Пассивы всего      7855867
Выручка            18834367
Прибьль            783023
Денежный поток     116329
  опер.            976737
  фин.             -399077
  инв.             -461331


СПЕЦИАЛИЗИРОВАННАЯ ПЕРЕДВИЖНАЯ МЕХАНИЗИРОВАННАЯ КОЛОННА-ЗЕЯ (ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ)
ИНН: 2815014979  ОКВЭД: 52.29.0
Активы всего               2 412
  внеоборотные                 0
  оборотные                2 412
Пассивы всего              2 412
  долгосрочные                 0
  краткосрочные            2 412
Выручка                    6 724
Прибыль                      760
Денежный поток               301
  опер.                      216
  фин.                        85
  инв.                         0

ВТОРМАТЕРИАЛ (ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ)
ИНН: 7724404000  ОКВЭД: 46.77.0
Активы всего                 864
  оборотные                  457
  внеоборотные               407
Пассивы всего                864
  капитал                   -409
  краткосрочные               93
  долгосрочные             1 180
Выручка                       85
Прибыль                     -420
Денежный поток                76
  опер.                   -1 109
  фин.                     1 185
  инв.                         0

Научно-производственный Центр развития технологий природно-техногенной безопасности - ГЕОТЕХНОЛОГИИ (Общество с ограниченной ответственностью)
ИНН: 3666125368  ОКВЭД: 26.51.05
Активы всего             199 760
  оборотные              199 733
  внеоборотные                27
Пассивы всего            199 760
  капитал                 38 762
  краткосрочные          160 998
  долгосрочные                 0
Выручка                        0
Прибыль                      -12
Денежный поток            -1 098
  опер.                   -2 542
  фин.                     1 444
  инв.                         0

"""

# TODO: Что такое okpo, okopf, okfs? Чем полезны в анализе?
# TODO: словарь ОПУ, ОДДС
