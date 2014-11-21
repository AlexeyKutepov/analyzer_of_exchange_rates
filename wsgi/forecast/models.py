"""
Описание моделей для алгоритма прогнозирования
"""

from django.db import models

class USD(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class EUR(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class AUD(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class AZN(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class AMD(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class BYR(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class BGN(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class BRL(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class HUF(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class KRW(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class DKK(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class INR(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class KZT(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class CAD(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class KGS(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class CNY(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class LVL(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class LTL(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class MDL(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class RON(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class TMT(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class NOK(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class PLN(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class XDR(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class SGD(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class TJS(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class TRY(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class UZS(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class UAH(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class GBP(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class CZK(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class SEK(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class CHF(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class ZAR(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

class JPY(models.Model):
    forecast = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)
    def __unicode__(self):
        return str(self.forecast)+" "+str(self.date)
    def __str__(self):
        return str(self.forecast)+" "+str(self.date)

