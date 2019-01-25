[![Build Status](https://travis-ci.com/ru-corporate/sandbox.svg?branch=master)](https://travis-ci.com/ru-corporate/sandbox)
[![Coverage Status](https://coveralls.io/repos/github/ru-corporate/sandbox/badge.svg?branch=master)](https://coveralls.io/github/ru-corporate/sandbox?branch=master)
[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/ru-corporate-talk/community) 
 
# Бухгалтерская отчетность организаций

Cкачиваем, причесываем и анализируем годовую бухгалтерскую (РСБУ) отчетность российских компаний.

## Исходные данные

Исходные данные [раскрывает Росстат][gks]. Примеры файлов:

| Год          |  Компаний  | Размер файла (Мб) |
|--------------|:----------:|:-----------------:|
| [2012][2012] |   765 813  |        525        |
| [2017][2017] | 2 358 756  |       1631        |

[gks]: http://www.gks.ru/opendata/dataset?q=%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C+%D0%BE%D1%80%D0%B3%D0%B0%D0%BD%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B9+&sort=score+desc%2C+metadata_modified+desc
[2012]: http://www.gks.ru/opendata/dataset/7708234640-bdboo2012
[2017]: http://www.gks.ru/opendata/dataset/7708234640-bdboo2017

## Установка пакета

```
git clone https://github.com/ru-corporate/sandbox.git
cd sandbox
pip install -r requirements.txt 
```
Для удобства также можно установить пакет `boo` локально:
```
pip install .
```

Пакет работает с версией Python не ниже 3.6

## Использование пакета

Загрузка и обработка данных может занять длительное время. 
Рекомендуем сначала освоиться с демонстрационным примером,
затем попробовать данные за 2012 год, где размер файлов 
минимальный. Если все работает, скачивайте последний доступный год. 

### Демонстрационный пример

Вы можете начать работу с коротким образцом данных
с условным названием `sample`:

```python
from boo import download, build, read_dataframe

download("sample")
build("sample")
df_0 = read_dataframe("sample")
print(df_0)
```
`df_0` содержит отчетность нескольких компаний за 2012 год
(быстро скачивается и преобразуется, используется для 
тестирования). 

### Фактические данные

[`example_start.py`](example_start.py) содержит следующий пример:

```python
from boo import download, build, read_dataframe

# download raw file from Rosstat
download(2012)

# create truncated version with fewer columns and rename columns 
build(2012)

# read trimmed version as dataframe
df = read_dataframe(2012)
```

После выполнения всей последовательности команд в переменной `df` будет 
сохранен датафрейм с фактическим данными за 2012 год. 

## Обзначения переменных

Датафрейм `df` имеет следующие колонки:

```
df.columns
Index(['ok1', 'ok2', 'ok3', 'org', 'title', 'region', 'inn', 'okpo', 'okopf',
       'okfs', 'unit', 'of', 'ta_fix', 'ta_nonfix', 'ta', 'tp_capital',
       'tp_long', 'debt_long', 'tp_short', 'debt_short', 'tp', 'sales',
       'profit_oper', 'exp_interest', 'profit_before_tax', 'of_lag',
       'ta_fix_lag', 'ta_nonfix_lag', 'ta_lag', 'tp_capital_lag',
       'tp_long_lag', 'debt_long_lag', 'tp_short_lag', 'debt_short_lag',
       'tp_lag', 'sales_lag', 'profit_oper_lag', 'exp_interest_lag',
       'profit_before_tax_lag', 'cf_oper', 'cf_inv', 'cf_fin', 'cf',
       'cash_in_oper_total', 'cash_in_oper_sales', 'paid_to_supplier',
       'paid_to_worker', 'paid_interest', 'paid_profit_tax',
       'paid_other_costs', 'paid_fa_investment'],
      dtype='object')
```

Эти колонки соответствуют идентификаторам компании и ключевым позициям бухгултерской отчетности.
Справочник по обозначениям переменных находится [тут][rename].

[rename]: boo/rename.py

| Код отчетности  |  Переменная       | Название         |
|:---------------:|:------------------|:-----------------|
| 1150 | of | Основные средства |
| 1100 | ta_fix | Итого внеоборотных активов |
| 1200 | ta_nonfix | Итого оборотных активов |
| 1250 | cash | Денежные средства и денежные эквиваленты |
| 1600 | ta | БАЛАНС (актив) |
| 1300 | tp_capital | ИТОГО капитал |
| 1400 | tp_long | ИТОГО долгосрочных обязательств |
| 1410 | debt_long | Долгосрочные заемные средства |
| 1500 | tp_short | ИТОГО краткосрочных обязательств |
| 1510 | debt_short | Краткосрочные заемные обязательства |
| 1700 | tp | БАЛАНС (пассив) |
| 2110 | sales | Выручка |
| 2200 | profit_oper | Прибыль (убыток) от продаж |
| 2330 | exp_interest | Проценты к уплате |
| 2300 | profit_before_tax | Прибыль (убыток) до налогообложения |
| 2400 | profit_after_tax | Чистая прибыль (убыток) |
| 4100 | cf_oper | Сальдо денежных потоков от текущих операций |
| 4200 | cf_inv | Сальдо денежных потоков от инвестиционных операций |
| 4300 | cf_fin | Сальдо денежных потоков от финансовых операций |
| 4400 | cf | Сальдо денежных потоков за отчетный период |
| 4110 | cash_in_oper_total | Поступления - всего |
| 4111 | cash_in_oper_sales | От продажи продукции, товаров, работ и услуг |
| 4121 | paid_to_supplier | Поставщикам (подрядчикам) за сырье, материалы, работы, услуги |
| 4122 | paid_to_worker | В связи с оплатой труда работников |
| 4123 | paid_interest | Проценты по долговым обязательствам |
| 4124 | paid_profit_tax | Налога на прибыль организаций |
| 4129 | paid_other_costs | Прочие платежи |
| 4221 | paid_fa_investment | В связи с приобретением, созданием, модернизацией, реконструкцией и подготовкой к использованию внеоборотны активов |


## Учебные задания 

### Текущие задания

1. Изучить используемые [названия переменных][rename]. 
   Из каких частей баланса они берутся? Как они взимосвязаны?
2. Получить данные за 2012 год ([example_start.py](example_start.py)).
3. Выбрать крупную компанию, найти на ее сайте отчетность по РСБУ за 2012 год,
   сравнить данные с сайта и из базы отчтености Росстата.  
4. Проверить правильность составления отчетности через равенства и неравенства
   (например `ta` = `tp`, `debt_long` < `tp_long`).
5. Вывести список крупнейших российских компаний по объему активов и по 
   объему продаж. Что не так с этим списком? Как его модифцировать?
   (задание - сначала сделать самостоятельно, затем посмотерть [play.py](play.py)).

### Будущие задания

- Чего в принципе нет в данных бухгалтерской отчетности. Какие подходы есть это оценить?  
