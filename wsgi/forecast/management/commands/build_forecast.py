"""
Запуск скрипта для расчёта прогноза
"""

__author__ = 'Alexey Kutepov'

from django.core.management.base import BaseCommand, CommandError
from forecast.management.commands._constants import KNN_COMMAND, TS_COMMAND
from forecast.management.commands._forecast_knn import *
from chart_forecast.constants import FORECAST_CLASSES
from currency_to_rub.constants import CURRENCY_CLASSES
from forecast.management.commands._forekast_ts import ForecastTS

class Command(BaseCommand):

    def knn_handler(self, currency, period, days=365):
        self.stdout.write("currency: "+str(currency)+", period: "+str(period)+", days: "+str(days))
        for i in range(period):
            result = knn(currency, days, datetime.datetime.today()-datetime.timedelta(days=i))
            self.stdout.write("Forecast: "+str(result))
            try:
                old_value = FORECAST_CLASSES[currency].objects.get(date=datetime.date.today()-datetime.timedelta(days=i-1))
            except:
                old_value = None
            if old_value != None:
                old_value.forecast=result
                old_value.save()
            else:
                item = FORECAST_CLASSES[currency](forecast=result, date=datetime.date.today()-datetime.timedelta(days=i-1))
                item.save()

    def ts_handler(self, currency, days=365):
        self.stdout.write("currency: "+str(currency)+", days: "+str(days))
        try:
            current_value = CURRENCY_CLASSES[currency].objects.get(date=datetime.date.today()-datetime.timedelta(days=days)).value
        except:
            return
        prev_value = current_value
        forecast_class = ForecastTS([current_value,])
        for i in range(1, days):
            result = forecast_class.get_forecast(current_value, prev_value, 1, i)
            prev_value = current_value
            try:
                current_value = CURRENCY_CLASSES[currency].objects.get(date=datetime.date.today()-datetime.timedelta(days=days-i)).value
            except:
                break
            self.stdout.write("Forecast: "+str(result))
            try:
                old_value = FORECAST_CLASSES[currency].objects.get(date=datetime.date.today()-datetime.timedelta(days=days-i))
            except:
                old_value = None
            if old_value != None:
                old_value.forecast=result
                old_value.save()
            else:
                item = FORECAST_CLASSES[currency](forecast=result, date=datetime.date.today()-datetime.timedelta(days=days-i    ))
                item.save()


    def handle(self, *args, **options):
        try:
            if args[0] == KNN_COMMAND:
                self.knn_handler(args[1], int(args[2]), int(args[3]))
            elif args[0] == TS_COMMAND:
                self.ts_handler(args[1], int(args[2]))

        except:
            raise CommandError('Command Error')

