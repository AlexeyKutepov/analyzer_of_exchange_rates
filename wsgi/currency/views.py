from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from currency.constants import CURRENCY_DATA, CURRENCY_CLASSES
from chart_forecast.constants import FORECAST_CLASSES
from currency.currency import Currency
import datetime
import logging

log = logging.getLogger(__name__)

#Формируем список значений курсов валют за промежуток времени с from_date по to_date
def get_values_for_handler(currency_class, values, from_date, to_date):
    if from_date<datetime.datetime.strptime('2000-01-01', '%Y-%m-%d'):
        from_date = datetime.datetime.strptime('2000-01-01', '%Y-%m-%d')
    if to_date>datetime.datetime.today():
        to_date=datetime.datetime.today()
    while (from_date<=to_date):
        try:
            values.append(str(from_date.date())+', '+str(currency_class.objects.get(date=from_date).value)+r'\n')
        except:
            pass #ничего не делаем для того, чтобы получить корректный вывод
        from_date = from_date + datetime.timedelta(days=1)

# Формируем список значений курсов валют с текущим прогнозом за days дней
# для отображения графика
def prepare_currency_value_list(currency, days=100):
    values = []
    values.append(r'Дата, '+r'Прогноз '+currency+'/RUB, Курс '+currency+r'/RUB\n')
    for i in range(days):
        try:
            values.append(
                str(datetime.date.today()-datetime.timedelta(days=i))+', '+
                str(FORECAST_CLASSES[currency].objects.get(date=datetime.date.today()-datetime.timedelta(days=i)).forecast)+', '+
                str(CURRENCY_CLASSES[currency].objects.get(date=datetime.date.today()-datetime.timedelta(days=i)).value)+r'\n'
            )
        except:
            pass #ничего не делаем для того, чтобы получить корректный вывод
    return values

# Формируем прогноз для отображения в виде графика
def prepare_forecast_value_list(currency, days=30):
    values = []
    values.append(r'Дата, '+r'Прогноз '+currency+'/RUB')
    for i in range(days):
        try:
            values.append(
                str(datetime.date.today()+datetime.timedelta(days=i))+', '+
                str(FORECAST_CLASSES[currency].objects.get(date=datetime.date.today()+datetime.timedelta(days=i)).forecast)+r'\n'
            )
        except:
            pass #ничего не делаем для того, чтобы получить корректный вывод
    return values

#Определяем выросла или упала валюта в цене
def get_state(old_value, new_value):
    if old_value <= new_value: return True
    else: return False

#относительное изменение курса валют
def get_change(old_value, new_value):
    return new_value-old_value

#Формирует информацию по курсам валют
def prepare_currency_list(period, current_date=datetime.date.today()):
    if datetime.datetime.weekday(current_date) == 6:
        current_date = current_date - datetime.timedelta(days=1)
        period = period - datetime.timedelta(days=1)
    #список объектов currency
    currency_list = []
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
            currency_list.append(
                Currency(state=state, char_code=char_code, name=name, value=value, units=units, change=change, link=link)
            )
    if currency_list == []:
        return prepare_currency_list(period-datetime.timedelta(days=1), current_date-datetime.timedelta(days=1))
    else:
        return currency_list, current_date

#Формирует длительные промежутки времени и запрашивает информацию о валютах
def response(years):
    date = datetime.date.today()
    if str(date.month).__eq__('2') and str(date.day).__eq__('29'):
        date = date.replace(day=28)
    date = str(date.year-years)+"-"+str(date.month)+"-"+str(date.day)
    date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    [currency_list, current_date] = prepare_currency_list(date)
    return currency_list, current_date

#период 1 день
def period_1d(request):
    currency_values = prepare_currency_value_list("USD")
    forecast_values = prepare_forecast_value_list("USD")
    [currency_list, current_date] = prepare_currency_list(datetime.date.today()-datetime.timedelta(days=1))
    log.info("HTTP_HOST: "+request.META["HTTP_HOST"]+", Period 1 day, Current date: "+current_date.strftime("%d.%m.%Y"))
    return render_to_response(
        'currency/currency.html', {
            'title':'Курсы валют',
            'currency_name':'USD/RUB',
            'period_state':'period/1d.html',
            'current_date':current_date.strftime("%d.%m.%Y"),
            'currency_list':currency_list,
            'currency_values': currency_values,
            'forecast_values':forecast_values,
        }
    )

#период 1 неделя
def period_1w(request):
    currency_values = prepare_currency_value_list("USD", 7)
    [currency_list, current_date]  = prepare_currency_list(datetime.date.today()-datetime.timedelta(weeks=1))
    log.info("HTTP_HOST: "+request.META["HTTP_HOST"]+", Period 1 week, Current date: "+current_date.strftime("%d.%m.%Y"))
    return render_to_response(
        'currency/currency.html', {
            'title':'Курсы валют',
            'currency_name':'USD/RUB',
            'period_state':'period/1w.html',
            'current_date':current_date.strftime("%d.%m.%Y"),
            'currency_list':currency_list,
            'currency_values': currency_values,
        }
    )

#период 1 месяц
def period_1m(request):
    currency_values = prepare_currency_value_list("USD", 30)
    [currency_list, current_date]  = prepare_currency_list(datetime.date.today()-datetime.timedelta(days=30))
    log.info("HTTP_HOST: "+request.META["HTTP_HOST"]+", Period 1 month, Current date: "+current_date.strftime("%d.%m.%Y"))
    return render_to_response(
        'currency/currency.html', {
            'title':'Курсы валют',
            'currency_name':'USD/RUB',
            'period_state':'period/1m.html',
            'current_date':current_date.strftime("%d.%m.%Y"),
            'currency_list':currency_list,
            'currency_values': currency_values,
        }
    )

#период 3 месяца
def period_3m(request):
    currency_values = prepare_currency_value_list("USD", 90)
    [currency_list, current_date]  = prepare_currency_list(datetime.date.today()-datetime.timedelta(days=90))
    log.info("HTTP_HOST: "+request.META["HTTP_HOST"]+", Period 3 month, Current date: "+current_date.strftime("%d.%m.%Y"))
    return render_to_response(
        'currency/currency.html', {
            'title':'Курсы валют',
            'currency_name':'USD/RUB',
            'period_state':'period/3m.html',
            'current_date':current_date.strftime("%d.%m.%Y"),
            'currency_list':currency_list,
            'currency_values': currency_values,
        }
    )

#период 6 месяцев
def period_6m(request):
    currency_values = prepare_currency_value_list("USD", 180)
    [currency_list, current_date]  = prepare_currency_list(datetime.date.today()-datetime.timedelta(days=180))
    log.info("HTTP_HOST: "+request.META["HTTP_HOST"]+", Period 6 month, Current date: "+current_date.strftime("%d.%m.%Y"))
    return render_to_response(
        'currency/currency.html', {
            'title':'Курсы валют',
            'currency_name':'USD/RUB',
            'period_state':'period/6m.html',
            'current_date':current_date.strftime("%d.%m.%Y"),
            'currency_list':currency_list,
            'currency_values': currency_values,
        }
    )

#период 1 год
def period_1y(request):
    currency_values = prepare_currency_value_list("USD", 365)
    [currency_list, current_date]  = response(years=1)
    log.info("HTTP_HOST: "+request.META["HTTP_HOST"]+", Period 1 year, Current date: "+current_date.strftime("%d.%m.%Y"))
    return render_to_response(
        'currency/currency.html', {
            'title':'Курсы валют',
            'currency_name':'USD/RUB',
            'period_state':'period/1y.html',
            'current_date':current_date.strftime("%d.%m.%Y"),
            'currency_list':currency_list,
            'currency_values': currency_values,
        }
    )

#период 5 лет
def period_5y(request):
    currency_values = prepare_currency_value_list("USD", 1825)
    [currency_list, current_date]  = response(years=5)
    log.info("HTTP_HOST: "+request.META["HTTP_HOST"]+", Period 5 years, Current date: "+current_date.strftime("%d.%m.%Y"))
    return render_to_response(
        'currency/currency.html', {
            'title':'Курсы валют',
            'currency_name':'USD/RUB',
            'period_state':'period/5y.html',
            'current_date':current_date.strftime("%d.%m.%Y"),
            'currency_list':currency_list,
            'currency_values': currency_values,
        }
    )

#период 10 лет
def period_10y(request):
    currency_values = prepare_currency_value_list("USD", 3650)
    [currency_list, current_date]  = response(years=10)
    log.info("HTTP_HOST: "+request.META["HTTP_HOST"]+", Period 10 years, Current date: "+current_date.strftime("%d.%m.%Y"))
    return render_to_response(
        'currency/currency.html', {
            'title':'Курсы валют',
            'currency_name':'USD/RUB',
            'period_state':'period/10y.html',
            'current_date':current_date.strftime("%d.%m.%Y"),
            'currency_list':currency_list,
            'currency_values': currency_values,
        }
    )

