"""
Обработчик комманд для запуска приложения построения прогнозов
Команды парсера Предсказателя:
    parse_cbrf - Запускает парсер сайта ЦБРФ за определённое количество дней (по умолчанию 1)
Параметры:
    n - количество дней, за которое нужно получить информацию о курсах валют.
        Пример: parse_cbrf 100 - получить информацию за 100 дней
Опции:
    -el - Запускает автоматический сбор данных ежедневно, за период времени указанный в n или
          установленный по умолчанию
"""

__author__ = 'Alexey Kutepov'

from django.core.management.base import BaseCommand, CommandError
from currency.constants import CURRENCY_CLASSES
from chart_forecast.constants import FORECAST_CLASSES
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

        for i in range(days):
            FORECAST_CLASSES[currency](
                forecast=result_list[i],
                date=datetime.date.today() - datetime.timedelta(days=days-(i-1))
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
            else:
                raise CommandError("Incorrect arguments")


