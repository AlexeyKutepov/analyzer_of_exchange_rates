"""
Запуск скрипта для расчёта прогноза
"""

__author__ = 'Alexey Kutepov'

from django.core.management.base import BaseCommand, CommandError
from forecast.management.commands._constants import KNN_COMMAND
from forecast.management.commands._forecast_knn import *
from chart_forecast.constants import FORECAST_CLASSES

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


    def handle(self, *args, **options):
        #try:
            if args[0] == KNN_COMMAND:
                self.knn_handler(args[1], int(args[2]), int(args[3]))
            else:
                raise CommandError('Command Error')
        #except:
        #    raise CommandError('Command Error')

