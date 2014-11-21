"""
Обработчик комманд для запуска приложения построения прогнозов
"""

__author__ = 'Alexey Kutepov'

from django.core.management.base import BaseCommand, CommandError
from currency.constants import CURRENCY_CLASSES, CURRENCY_DATA
from forecast.constants import FORECAST_CLASSES
from forecast.management.commands._forekast_time_series import  *
import datetime

class Command(BaseCommand):

    # Запуск алгоритма прогнозирования временных рядов
    def ts_handler(self, currency, days=365):
        self.stdout.write("currency: "+str(currency)+", days: "+str(days))
        currency_values_list = (
            CURRENCY_CLASSES[currency].objects
                .filter(date__gte=datetime.date.today()-datetime.timedelta(days=days+1))
                .order_by('date').values_list('value', flat=True)
        )

        # Настройка предсказателя
        forecast_class = ForecastTimeSeries(
            level=[],
            alpha=0.7898781540523456,
            phi=0.0014315547808000616,
            gamma=0.26521182714746216,
            delta=0.7879944349159262,
            trend=[0.0,],
            forecast_error=[0.0,],
        )

        result_list = forecast_class.get_forecast(currency_values_list)
        print("forecast list = ", result_list)

        forecast_date = datetime.date.today() - datetime.timedelta(days=len(result_list)-1)
        for i in range(len(result_list)):
            FORECAST_CLASSES[currency](
                forecast=result_list[i],
                date=forecast_date + datetime.timedelta(days=i+1)
            ).save()

        # Прогноз на месяц вперёд
        for i in range(2, 30):
            # Настройка предсказателя
            forecast_class = ForecastTimeSeries(
                level=[],
                alpha=0.576538981791653,
                phi=0.002559493548395495,
                gamma=0.729581128925414,
                delta=0.8280377276707289,
                trend=[0.0,],
                forecast_error=[0.0,],
            )
            result_list = forecast_class.get_forecast(currency_values_list, i)
            print("forecast list 2 = ", result_list)
            FORECAST_CLASSES[currency](
                forecast=result_list[len(result_list)-1],
                date=datetime.date.today() + datetime.timedelta(days=i)
            ).save()



    def handle(self, *args, **options):
        if len(args) != 2:
            raise CommandError("Incorrect arguments")
        currency = str(args[0]).upper()
        try:
            days = int(args[1])
        except:
            raise CommandError("Incorrect arguments")
        else:
            if currency in CURRENCY_CLASSES:
                self.ts_handler(currency, days)
            elif currency == "ALL":
                for item in CURRENCY_DATA:
                    self.ts_handler(item["char_code"], days)
            else:
                raise CommandError("Incorrect arguments")


