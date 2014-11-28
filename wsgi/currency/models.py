from django.db import models

# Курсы валют к рублю:

#Доллар
class USD_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Евро
class EUR_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Австралийский доллар
class AUD_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Азербайджанский манат
class AZN_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Армянских драмов
class AMD_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Белорусских рублей
class BYR_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Болгарский лев
class BGN_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Бразильский реал
class BRL_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Венгерских форинтов
class HUF_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Вон Республики Корея
class KRW_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Датских крон
class DKK_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Индийских рупий
class INR_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Казахских тенге
class KZT_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Канадский доллар
class CAD_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Киргизских сомов
class KGS_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Китайских юаней
class CNY_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Латвийский лат
class LVL_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Литовский лит
class LTL_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Молдавских леев
class MDL_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Новых румынских леев
class RON_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Новый туркменский манат
class TMT_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Норвежских крон
class NOK_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Польских злотых
class PLN_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#СДР (специальные права заимствования)
class XDR_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Сингапурский доллар
class SGD_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Таджикских сомони
class TJS_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Турецкая лира
class TRY_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Узбекских сумов
class UZS_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Украинских гривен
class UAH_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Фунт стерлингов Соединенного королевства
class GBP_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Чешских крон
class CZK_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Шведских крон
class SEK_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Швейцарский франк
class CHF_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Южноафриканских рэндов
class ZAR_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Японских иен
class JPY_RUB(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField(primary_key=True)

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)