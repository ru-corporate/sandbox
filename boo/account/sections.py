SECTION_NAMES_TEXT = """БУХГАЛТЕРСКИЙ БАЛАНС	1
ОТЧЕТ О ФИНАНСОВЫХ РЕЗУЛЬТАТАХ	2
ОТЧЕТ ОБ ИЗМЕНЕНИЯХ КАПИТАЛА	3
ОТЧЕТ О ДВИЖЕНИИ ДЕНЕЖНЫХ СРЕДСТВ	4
ПОЯСНЕНИЯ К БУХГАЛТЕРСКОМУ БАЛАНСУ И ОТЧЕТУ О ФИНАНСОВЫХ РЕЗУЛЬТАТАХ	5
ОТЧЕТ О ЦЕЛЕВОМ ИСПОЛЬЗОВАНИИ СРЕДСТВ	6"""


def _items(doc: str):
    for x in doc.split('\n'):
        y = x.split('\t')
        try:
            yield (y[0], y[1])
        except IndexError:
            raise ValueError(y)


SECTION_NAMES = {b: a for (a, b) in _items(SECTION_NAMES_TEXT)}


def account_section(code):
    """Return account section description by code."""
    return SECTION_NAMES.get(str(code)[0])
