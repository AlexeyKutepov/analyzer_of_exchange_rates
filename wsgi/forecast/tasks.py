from __future__ import absolute_import

from celery.task import periodic_task
from datetime import timedelta
import datetime
from currency.constants import CURRENCY_DATA
from chart_forecast.constants import FORECAST_CLASSES
from forecast.management.commands._forekast_time_series import ForecastTimeSeries

@periodic_task(run_every = timedelta(seconds = 3600))
def parse_cbrf():
    print("Forecast is started")
    days = 100
    for item in CURRENCY_DATA:
        print("currency:", item["class"], "days:", days)
        currency_values_list = (
            item["class"].objects
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

        for i in range(len(result_list)):
            FORECAST_CLASSES[
                item["char_code"]
            ](
                forecast=result_list[i],
                date=datetime.date.today() - datetime.timedelta(days=days-(i-1))
            ).save()


