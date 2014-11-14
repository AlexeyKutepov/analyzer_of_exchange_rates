"""
Построение диаграммы прогнозирования
"""

import datetime

from django.shortcuts import render_to_response

from currency.constants import CURRENCY_CLASSES
from chart_forecast.constants import FORECAST_CLASSES



def build_chart(from_date, to_date, currency):
    values = []
    values.append(r'Дата, '+r'Прогноз '+currency+'/RUB, '+currency+r'/RUB\n')
    if from_date<datetime.datetime.strptime('2000-01-01', '%Y-%m-%d'):
        from_date = datetime.datetime.strptime('2000-01-01', '%Y-%m-%d')
    if to_date>datetime.datetime.today():
        to_date=datetime.datetime.today()
    while (from_date<=to_date):
        try:
            values.append(
                str(from_date.date())+', '+
                str(FORECAST_CLASSES[currency].objects.get(date=from_date).forecast)+', '+
                str(CURRENCY_CLASSES[currency].objects.get(date=from_date).value)+r'\n'
            )
        except:
            pass #ничего не делаем для того, чтобы получить корректный вывод
        from_date = from_date + datetime.timedelta(days=1)
    return values


def build_forecast(request, currency='USD'):
    if 'currency' in request.GET:
        currency = request.GET['currency']
        currency = currency[0:3]
    if currency not in FORECAST_CLASSES.keys():
        currency='USD'
    values = build_chart(
        datetime.datetime.today()-datetime.timedelta(days=366), datetime.datetime.today(), currency
    )
    try:
        tommorow = str(FORECAST_CLASSES[currency].objects.get(date=datetime.datetime.today()).forecast)
    except:
        tommorow = "<недоступно>"
    return render_to_response('chart.html', {
        'title':'Котировки',
        'chart_options':'forecast_options.html',
        'title_content':"Прогноз "+currency+"/RUB",
        'forecast_content':"Прогноз на завтра: "+tommorow+" RUB",
        'values':values
    })


