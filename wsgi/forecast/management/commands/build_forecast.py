"""
Обработчик комманд для запуска приложения построения прогнозов
"""

__author__ = 'Alexey Kutepov'

from django.core.management.base import BaseCommand, CommandError
from currency_to_rub.constants import CURRENCY_CLASSES
from forecast.management.commands._forekast_time_series import  *
import datetime

class Command(BaseCommand):

    # Запуск алгоритма прогнозирования временных рядов
    def ts_handler(self, currency, days=365):
        self.stdout.write("currency: "+str(currency)+", days: "+str(days))
        currency_values_list = (
            CURRENCY_CLASSES[currency].objects
                .filter(date__gte=datetime.date.today()-datetime.timedelta(days=days))
                .order_by('date').values_list('value', flat=True)
        )

        # Настройка предсказателя
        forecast_class = ForecastTimeSeries(
            level=[],
            alpha=0.5,
            phi=0.5,
            gamma=0.5,
            delta=0.5,
            trend=[0.0,],
            forecast_error=[0.0,],
            season=[0.0,],
            periods=1
        )

        result_list = forecast_class.get_forecast(currency_values_list)
        print("forecast list = ", result_list)

            # self.stdout.write("Forecast: "+str(result)+" "+str(datetime.date.today()-datetime.timedelta(days=days-(i-1))))
            # try:
            #     old_value = FORECAST_CLASSES[currency].objects.get(date=datetime.date.today()-datetime.timedelta(days=days-(i-1)))
            # except:
            #     old_value = None
            # if old_value != None:
            #     old_value.forecast=result
            #     old_value.save()
            # else:
            #     item = FORECAST_CLASSES[currency](forecast=result, date=datetime.date.today()-datetime.timedelta(days=days-(i-1)))
            #     item.save()
            # try:
            #     current_value = CURRENCY_CLASSES[currency].objects.get(date=datetime.date.today()-datetime.timedelta(days=days-i)).value
            # except:
            #     break
            # self.stdout.write("Next value: "+str(current_value)+" "+str(datetime.date.today()-datetime.timedelta(days=days-(i))))



    def handle(self, *args, **options):
        if len(args) != 2:
            CommandError("Incorrect arguments")
        if args[0] in CURRENCY_CLASSES:
            self.ts_handler(args[0], int(args[1]))
        else:
            CommandError("Incorrect arguments")


