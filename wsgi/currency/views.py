from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from currency.constants import ROWS, COLUMNS, CURRENCY_DATA
from currency.currency import Currency
import datetime
import logging

log = logging.getLogger(__name__)


#Определяем выросла или упала валюта в цене
def get_state(old_value, new_value):
    if old_value <= new_value: return True
    else: return False

#относительное изменение курса валют
def get_change(old_value, new_value):
    return new_value-old_value

#формирование информации для отображения курсов валют на сайте
@DeprecationWarning
def get_currency(period, current_date=datetime.date.today()):
    if datetime.datetime.weekday(current_date) == 6:
        current_date = current_date - datetime.timedelta(days=1)
        period = period - datetime.timedelta(days=1)
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
                state = get_state(
                    item["class"].objects.get(date=period).value, item["class"].objects.get(date=current_date).value
                )
                char_code = item["char_code"]
                name = item["name"]
                value = item["class"].objects.get(date=current_date).value
                units = item["class"].objects.get(date=current_date).units
                change = get_change(
                    item["class"].objects.get(date=period).value, item["class"].objects.get(date=current_date).value
                )
                link = "build_chart/?currency="+str(item["char_code"]);
            except ObjectDoesNotExist:
                j -= 1
                error = True
            if not error:
                currency_row.append(
                    Currency(state=state, char_code=char_code, name=name, value=value, units=units, change=change, link=link)
                )
        if currency_row != []:
            currency.append(currency_row)
    if currency == []:
        return get_currency(period-datetime.timedelta(days=1), current_date-datetime.timedelta(days=1))
    else:
        return currency, current_date

#Формирует информацию по курсам валют
def prepare_currency(period, current_date=datetime.date.today()):
    if datetime.datetime.weekday(current_date) == 6:
        current_date = current_date - datetime.timedelta(days=1)
        period = period - datetime.timedelta(days=1)
    #список объектов currency
    currency = []
    iterator = iter(CURRENCY_DATA)
    for item in iterator:
        try:
            state = get_state(
                item["class"].objects.get(date=period).value, item["class"].objects.get(date=current_date).value
            )
            char_code = item["char_code"]
            name = item["name"]
            value = item["class"].objects.get(date=current_date).value
            units = item["class"].objects.get(date=current_date).units
            change = get_change(
                item["class"].objects.get(date=period).value, item["class"].objects.get(date=current_date).value
            )
            link = "build_chart/?currency="+str(item["char_code"])
        except ObjectDoesNotExist:
            pass
        else:
            currency.append(
                Currency(state=state, char_code=char_code, name=name, value=value, units=units, change=change, link=link)
            )
    if currency == []:
        return prepare_currency(period-datetime.timedelta(days=1), current_date-datetime.timedelta(days=1))
    else:
        return currency, current_date

#Формирует длительные промежутки времени и запрашивает информацию о валютах
def response(years):
    date = datetime.date.today()
    if str(date.month).__eq__('2') and str(date.day).__eq__('29'):
        date = date.replace(day=28)
    date = str(date.year-years)+"-"+str(date.month)+"-"+str(date.day)
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    [currency, current_date] = prepare_currency(date)
    return currency, current_date

#период 1 день
def period_1d(request):
    [currency, current_date] = prepare_currency(datetime.date.today()-datetime.timedelta(days=1))
    log.info("HTTP_HOST: "+request.META["HTTP_HOST"]+", Period 1 day, Current date: "+current_date.strftime("%d.%m.%Y"))
    return render_to_response(
        'currency/currency.html', {'title':'Курсы валют', 'period_state':'period/1d.html', "current_date":current_date.strftime("%d.%m.%Y"), "currency":currency}
    )

#период 1 неделя
def period_1w(request):
    [currency, current_date]  = prepare_currency(datetime.date.today()-datetime.timedelta(weeks=1))
    log.info("HTTP_HOST: "+request.META["HTTP_HOST"]+", Period 1 week, Current date: "+current_date.strftime("%d.%m.%Y"))
    return render_to_response(
        'currency/currency.html', {'title':'Курсы валют', 'period_state':'period/1w.html', "current_date":current_date.strftime("%d.%m.%Y"), "currency":currency}
    )

#период 1 месяц
def period_1m(request):
    [currency, current_date]  = prepare_currency(datetime.date.today()-datetime.timedelta(days=30))
    log.info("HTTP_HOST: "+request.META["HTTP_HOST"]+", Period 1 month, Current date: "+current_date.strftime("%d.%m.%Y"))
    return render_to_response(
        'currency/currency.html', {'title':'Курсы валют', 'period_state':'period/1m.html', "current_date":current_date.strftime("%d.%m.%Y"), "currency":currency}
    )

#период 3 месяца
def period_3m(request):
    [currency, current_date]  = prepare_currency(datetime.date.today()-datetime.timedelta(days=90))
    log.info("HTTP_HOST: "+request.META["HTTP_HOST"]+", Period 3 month, Current date: "+current_date.strftime("%d.%m.%Y"))
    return render_to_response(
        'currency/currency.html', {'title':'Курсы валют', 'period_state':'period/3m.html', "current_date":current_date.strftime("%d.%m.%Y"), "currency":currency}
    )

#период 6 месяцев
def period_6m(request):
    [currency, current_date]  = prepare_currency(datetime.date.today()-datetime.timedelta(days=180))
    log.info("HTTP_HOST: "+request.META["HTTP_HOST"]+", Period 6 month, Current date: "+current_date.strftime("%d.%m.%Y"))
    return render_to_response(
        'currency/currency.html', {'title':'Курсы валют', 'period_state':'period/6m.html', "current_date":current_date.strftime("%d.%m.%Y"), "currency":currency}
    )

#период 1 год
def period_1y(request):
    [currency, current_date]  = response(years=1)
    log.info("HTTP_HOST: "+request.META["HTTP_HOST"]+", Period 1 year, Current date: "+current_date.strftime("%d.%m.%Y"))
    return render_to_response(
        'currency/currency.html', {'title':'Курсы валют', 'period_state':'period/1y.html', "current_date":current_date.strftime("%d.%m.%Y"), "currency":currency}
    )

#период 5 лет
def period_5y(request):
    [currency, current_date]  = response(years=5)
    log.info("HTTP_HOST: "+request.META["HTTP_HOST"]+", Period 5 years, Current date: "+current_date.strftime("%d.%m.%Y"))
    return render_to_response(
        'currency/currency.html', {'title':'Курсы валют', 'period_state':'period/5y.html', "current_date":current_date.strftime("%d.%m.%Y"),  "currency":currency}
    )

#период 10 лет
def period_10y(request):
    [currency, current_date]  = response(years=10)
    log.info("HTTP_HOST: "+request.META["HTTP_HOST"]+", Period 10 years, Current date: "+current_date.strftime("%d.%m.%Y"))
    return render_to_response(
        'currency/currency.html', {'title':'Курсы валют', 'period_state':'period/10y.html', "current_date":current_date.strftime("%d.%m.%Y"), "currency":currency}
    )

