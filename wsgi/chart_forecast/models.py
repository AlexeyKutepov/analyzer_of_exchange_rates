"""
Описание моделей для алгоритма прогнозирования
"""

from django.db import models

# Create your models here.

class Forecast_of_USD(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_EUR(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_AUD(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_AZN(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_AMD(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_BYR(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_BGN(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_BRL(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_HUF(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_KRW(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_DKK(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_INR(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_KZT(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_CAD(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_KGS(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_CNY(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_LVL(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_LTL(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_MDL(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_RON(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_TMT(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_NOK(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_PLN(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_XDR(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_SGD(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_TJS(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_TRY(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_UZS(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_UAH(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_GBP(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_CZK(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_SEK(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_CHF(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_ZAR(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class Forecast_of_JPY(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

