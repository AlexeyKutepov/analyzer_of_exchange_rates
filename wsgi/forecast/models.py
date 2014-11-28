"""
Описание моделей для алгоритма прогнозирования
"""

from django.db import models

class USD_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class EUR_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class AUD_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class AZN_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class AMD_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class BYR_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class BGN_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class BRL_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class HUF_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class KRW_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class DKK_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class INR_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class KZT_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class CAD_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class KGS_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class CNY_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class LVL_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class LTL_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class MDL_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class RON_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class TMT_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class NOK_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class PLN_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class XDR_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class SGD_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class TJS_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class TRY_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class UZS_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class UAH_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class GBP_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class CZK_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class SEK_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class CHF_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class ZAR_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class JPY_RUB(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

