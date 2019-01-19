# 
# Описания полей отчетности можно посмотреть например в:
# http://info.avtovaz.ru/files/avtovaz_ras_fs_2012_rus_secured.pdf
# 
# Более подробно:
# http://www.consultant.ru/document/cons_doc_LAW_103394/b990bf4a13bd23fda86e0bba50c462a174c0d123/#dst100515
# 

# TODO: проставить названия полей
FIELDS = [
 ('1150', 'of',                 'Основные фонды'),
 ('1100', 'ta_fix',             ''),
 ('1200', 'ta_nonfix',          ''),
 ('1600', 'ta',                 ''),
 ('1300', 'tp_capital',         ''),
 ('1400', 'tp_long',            ''),
 ('1410', 'debt_long',          ''),
 ('1500', 'tp_short',           ''),
 ('1510', 'debt_short',         ''),
 ('1700', 'tp'                  ''),


 ('2110', 'sales',              ''),
 ('2200', 'profit_oper',        ''),
 ('2330', 'exp_interest',       ''),
 ('2300', 'profit_before_tax',  ''), 


 ('4100', 'cf_oper',            ''),
 ('4200', 'cf_inv',             ''),
 ('4300', 'cf_fin',             ''),
 ('4400', 'cf',                 ''),                 
 ('4110', 'cash_in_oper_total', ''),
 ('4111', 'cash_in_oper_sales', ''),
 ('4121', 'paid_to_supplier',   ''),
 ('4122', 'paid_to_worker',     ''),
 ('4123', 'paid_interest',      ''),
 ('4124', 'paid_profit_tax',    ''),
 ('4129', 'paid_other_costs',   ''),
 ('4221', 'paid_fa_investment', '')]

DEFAULT_LOOKUP_DICT = {t[0]:t[1] for t in FIELDS)