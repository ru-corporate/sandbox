"""Download and truncate Rosstat corporate dataset."""

from boo import download, build, read_dataframe

print("Please be prepared download and build operations "
      "can take several minutes!")

year = 2012

# download raw file from Rosstat
try:
   download(year)
except FileExistsError:
   print("Raw file already downloaded")

# create truncated version with fewer columns and good column names 
try:
   build(year)
except FileExistsError:
   print("Work file already created")    

# read trimmed version of data as dataframe
df = read_dataframe(year)

print(year, "dataset:", df.shape[0], "rows and", df.shape[1], "columns")


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
