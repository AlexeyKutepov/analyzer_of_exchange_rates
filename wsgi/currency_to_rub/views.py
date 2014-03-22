from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from currency_to_rub.constants import ROWS, COLUMNS, CURRENCY_DATA
from currency_to_rub.currency import Currency
import datetime


#Определяем выросла или упала валюта в цене
def get_state(old_value, new_value):
    if old_value <= new_value: return True
    else: return False

#относительное изменение курса валют
def get_change(old_value, new_value):
    return new_value-old_value

#формирование информации для отображения курсов валют на сайте
def get_currency(period):
    currency = [] #список объектов currency
    iterator = iter(CURRENCY_DATA)
    columns = COLUMNS
    rows = ROWS
    for i in range(rows):
        currency_row = []
        j = 1
        while j <= columns:
            error = False
            j += 1
            try:
                item = iterator.__next__()
            except StopIteration:
                continue
            try:
                state = get_state(item["class"].objects.get(date=period).value, item["class"].objects.get(date=datetime.date.today()).value)
                char_code = item["char_code"]
                name = item["name"]
                value = item["class"].objects.get(date=datetime.date.today()).value
                units = item["class"].objects.get(date=datetime.date.today()).units
                change = get_change(item["class"].objects.get(date=period).value, item["class"].objects.get(date=datetime.date.today()).value)
                link = "build_chart/?currency="+str(item["char_code"]);
            except ObjectDoesNotExist:
                j -= 1
                error = True
            if not error:
                currency_row.append(
                    Currency(state=state, char_code=char_code, name=name, value=value, units=units, change=change, link=link)
                )
        currency.append(currency_row)
    return currency

def response(years):
    date = datetime.date.today()
    if str(date.month).__eq__('2') and str(date.day).__eq__('29'):
        date = date.replace(day=28)
    date = str(date.year-years)+"-"+str(date.month)+"-"+str(date.day)
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    currency = get_currency(date)
    return currency

#период 1 день
def period_1d(request):
    currency = get_currency(datetime.date.today()-datetime.timedelta(days=1))
    return render_to_response('currency.html', {'title':'Котировки', 'quotes':'Курсы валют', 'period_state':'period/1d.html', "currency":currency})

#период 1 неделя
def period_1w(request):
    currency = get_currency(datetime.date.today()-datetime.timedelta(weeks=1))
    return render_to_response('currency.html', {'title':'Котировки', 'quotes':'Курсы валют', 'period_state':'period/1w.html', "currency":currency})

#период 1 месяц
def period_1m(request):
    currency = get_currency(datetime.date.today()-datetime.timedelta(days=30))
    return render_to_response('currency.html', {'title':'Котировки', 'quotes':'Курсы валют', 'period_state':'period/1m.html', "currency":currency})

#период 3 месяца
def period_3m(request):
    currency = get_currency(datetime.date.today()-datetime.timedelta(days=90))
    return render_to_response('currency.html', {'title':'Котировки', 'quotes':'Курсы валют', 'period_state':'period/3m.html', "currency":currency})

#период 6 месяцев
def period_6m(request):
    currency = get_currency(datetime.date.today()-datetime.timedelta(days=180))
    return render_to_response('currency.html', {'title':'Котировки', 'quotes':'Курсы валют', 'period_state':'period/6m.html', "currency":currency})

#период 1 год
def period_1y(request):
    currency = response(years=1)
    return render_to_response('currency.html', {'title':'Котировки', 'quotes':'Курсы валют', 'period_state':'period/1y.html', "currency":currency})

#период 5 лет
def period_5y(request):
    currency = response(years=5)
    return render_to_response('currency.html', {'title':'Котировки', 'quotes':'Курсы валют', 'period_state':'period/5y.html', "currency":currency})

#период 10 лет
def period_10y(request):
    currency = response(years=10)
    return render_to_response('currency.html', {'title':'Котировки', 'quotes':'Курсы валют', 'period_state':'period/10y.html', "currency":currency})
