from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from currency.constants import CURRENCY_DATA, CURRENCY_CLASSES
from forecast.constants import FORECAST_CLASSES
from currency.currency import Currency
import datetime
import logging

log = logging.getLogger(__name__)

#Формируем список значений курсов валют за промежуток времени с from_date по to_date
def _get_values_for_handler(currency_class, values, from_date, to_date):
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
def _prepare_currency_value_list(currency, days=100):
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
def _prepare_forecast_value_list(currency, days=30):
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
def _get_state(old_value, new_value):
    if old_value <= new_value: return True
    else: return False

#относительное изменение курса валют
def _get_change(old_value, new_value):
    return new_value-old_value

#Формирует информацию по курсам валют
def _prepare_currency_list(period, current_date=datetime.date.today()):
    if datetime.datetime.weekday(current_date) == 6:
        current_date = current_date - datetime.timedelta(days=1)
        period = period - datetime.timedelta(days=1)
    #список объектов currency
    currency_list = []
    iterator = iter(CURRENCY_DATA)
    for item in iterator:
        try:
            state = _get_state(
                item["class"].objects.get(date=period).value, item["class"].objects.get(date=current_date).value
            )
            char_code = item["char_code"]
            name = item["name"]
            value = item["class"].objects.get(date=current_date).value
            units = item["class"].objects.get(date=current_date).units
            change = _get_change(
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
        return _prepare_currency_list(period-datetime.timedelta(days=1), current_date-datetime.timedelta(days=1))
    else:
        return currency_list, current_date

#получить курсы валют
def get_quotation_of_currency(request):
    currency_values = _prepare_currency_value_list("USD")
    forecast_values = _prepare_forecast_value_list("USD")
    [currency_list, current_date] = _prepare_currency_list(datetime.date.today()-datetime.timedelta(days=1))
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

