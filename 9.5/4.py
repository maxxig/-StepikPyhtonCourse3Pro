from datetime import date
def date_formatter(country_code):
    cntrs = {'ru': '%d.%m.%Y',
     'us': '%m-%d-%Y',
     'ca': '%Y-%m-%d',
     'br': '%d/%m/%Y',
     'fr': '%d.%m.%Y',
     'pt': '%d-%m-%Y',}
    def wrapper(d):
        return d.strftime(cntrs[country_code])
    return wrapper

date_ru = date_formatter('fr')
today = date(2025, 1, 5)
print(date_ru(today))