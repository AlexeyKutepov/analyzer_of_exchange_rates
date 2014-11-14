from django.shortcuts import render_to_response
from currency.models import USD
from currency.constants import CURRENCY_DATA
import datetime

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

def get_values(currency_class, values, days):
    for i in range(days):
        try:
            values.append(
                str(datetime.date.today()-datetime.timedelta(days=i))+', '+
                str(currency_class.objects.get(date=datetime.date.today()-datetime.timedelta(days=i+1)).value)+r'\n'
            )
        except:
            pass #ничего не делаем для того, чтобы получить корректный вывод

def chart_handler(request):
    values = []
    currency_class = None
    currency = None
    is_have_period = True
    if 'currency' in request.GET:
        currency = request.GET['currency']
        for item in CURRENCY_DATA:
            try:
                if currency[0:3] == item["char_code"]:
                    currency_class = item["class"]
            except:
                continue
        if currency_class==None or currency==None:
            currency_class = USD
            currency = 'USD'
        values.append(r'Дата, '+currency[0:3]+r'/RUB\n')
        get_values(currency_class, values, 365)
        return render_to_response('chart.html', {
        'title':'Котировки', 'chart_options':'chart_options.html', 'title_content':currency[0:3]+'/RUB', 'values':values
        })

    if 'select_currency' in request.GET:
        currency = request.GET['select_currency']
    try:
        if 'from_date' in request.GET:
            from_date = datetime.datetime.strptime(request.GET['from_date'], '%Y-%m-%d')
        if 'to_date' in request.GET:
            to_date = datetime.datetime.strptime(request.GET['to_date'], '%Y-%m-%d')
    except:
        is_have_period = False
    values.append(r'Дата, '+currency+r'\n')
    for item in CURRENCY_DATA:
        try:
            if currency[0:3] == item["char_code"]:
                currency_class = item["class"]
        except:
            continue
    if currency_class==None:
        currency_class=USD
    if is_have_period:
        get_values_for_handler(currency_class, values, from_date, to_date)
    else:
        get_values(currency_class, values, 365)
    return render_to_response('chart.html', {
        'title':'Котировки', 'chart_options':'chart_options.html', 'title_content':currency, 'values':values
    })

