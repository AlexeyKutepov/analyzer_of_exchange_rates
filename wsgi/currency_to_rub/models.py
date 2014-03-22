from django.db import models

# Курсы валют к рублю:

#Доллар
class USD(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Евро
class EUR(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Австралийский доллар
class AUD(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Азербайджанский манат
class AZN(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Армянских драмов
class AMD(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Белорусских рублей
class BYR(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Болгарский лев
class BGN(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Бразильский реал
class BRL(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Венгерских форинтов
class HUF(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Вон Республики Корея
class KRW(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Датских крон
class DKK(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Индийских рупий
class INR(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Казахских тенге
class KZT(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Канадский доллар
class CAD(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Киргизских сомов
class KGS(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Китайских юаней
class CNY(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Латвийский лат
class LVL(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Литовский лит
class LTL(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Молдавских леев
class MDL(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Новых румынских леев
class RON(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Новый туркменский манат
class TMT(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Норвежских крон
class NOK(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Польских злотых
class PLN(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#СДР (специальные права заимствования)
class XDR(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Сингапурский доллар
class SGD(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Таджикских сомони
class TJS(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Турецкая лира
class TRY(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Узбекских сумов
class UZS(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Украинских гривен
class UAH(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Фунт стерлингов Соединенного королевства
class GBP(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Чешских крон
class CZK(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Шведских крон
class SEK(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Швейцарский франк
class CHF(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Южноафриканских рэндов
class ZAR(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

#Японских иен
class JPY(models.Model):
    units = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5)
    date = models.DateField()

    def __unicode__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)

    def __str__(self):
        return str(self.units)+" "+str(self.value)+" "+str(self.date)