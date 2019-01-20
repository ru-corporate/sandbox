[![Build Status](https://travis-ci.com/ru-corporate/sandbox.svg?branch=master)](https://travis-ci.com/ru-corporate/sandbox)
[![Coverage Status](https://coveralls.io/repos/github/ru-corporate/sandbox/badge.svg?branch=master)](https://coveralls.io/github/ru-corporate/sandbox?branch=master)
[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/ru-corporate-talk/community) 
 
# Бухгалтерская отчетность организаций

Пакет `boo` позволяет скачать и использовать годовую бухгалтерскую отчетность 
российских компаний, которую [Росстат публикует][gks] начиная с 2012 года.

[gks]: http://www.gks.ru/opendata/dataset?q=%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C+%D0%BE%D1%80%D0%B3%D0%B0%D0%BD%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D0%B9+&sort=score+desc%2C+metadata_modified+desc

Название `boo` - сокращение от "бухгалтерская отчетность организаций".


## Начало работы

```
git clone https://github.com/ru-corporate/sandbox
cd sandbox
pip install -r requirements.txt 
python -i start.py
```

`start.py` содержит следующий пример:

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
датафрейм с данными отчтености компаний за 2012 год. Выполнение команд может
занять длительное время.

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

Эти колонки соответствуют ключевым позициям бухгултерской отчетности.
Справочник по обозначениям переменных можно посмотреть [тут][rename].

[rename]: boo/rename.py

## Учебные задания 

### Текущие задания

1. Изучить используемые [названия переменных][rename]. 
   Из каких частей баланса они берутся? Как они взимосвязаны?
2. Получить данные за 2012 год ([start.py](start.py)).
3. Выбрать крупную компанию, найти на ее сайте отчетность по РСБУ за 2012 год,
   сравнить данные с сайта и из базы отчтености Росстата.  
4. Проверить правильность составления отчетности через равенства и неравенства
   (например `ta` = `tp`, `debt_long` < `tp_long`).
5. Вывести список крупнейших российских компаний по объему активов и по 
   объему продаж. Что не так с этим списком? Как его модифцировать?
   (задание - сначала сделать самостоятельно, затем посмотерть [play.py](play.py)).

### Будущие задания

- Чего в принципе нет в данных бухгалтерской отчетности. Какие подходы есть это оценить?  
      
  
## Дополнительные ссылки

### Официальные источники

- [Сервис Росстата по получению отчетности](http://www.gks.ru/accounting_report)
- [Выписки из ЕГРЮЛ](https://egrul.nalog.ru/index.html)

### Он-лайн доступ к тем же данным 

- [sbis](https://sbis.ru/contragents/7825706086)
- [list-org](https://www.list-org.com/company/19562)

### Крупные провайдеры (тех же и других данных)

- [Спарк (Интерфакс)](http://www.spark-interfax.ru/ru/about)
- [БИР-Аналитик](https://bir.1prime.ru)
- [Скрин](https://kontragent.skrin.ru)
- [Фира-Про](https://pro.fira.ru)
