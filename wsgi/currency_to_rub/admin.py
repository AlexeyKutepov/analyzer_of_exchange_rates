from django.contrib import admin
from currency_to_rub.models import USD, EUR, AUD, AZN, AMD, BYR, BGN, BRL, HUF, KRW, DKK, INR, KZT, CAD, KGS, CNY, LVL, JPY
from currency_to_rub.models import LTL, MDL, RON, TMT, NOK, PLN, XDR, SGD, TJS, TRY, UZS, UAH, GBP, CZK, SEK, CHF, ZAR

# Register your models here.
admin.site.register(USD) #Доллар США
admin.site.register(EUR) #Евро
admin.site.register(AUD) #Австралийский доллар
admin.site.register(AZN) #Азербайджанский манат
admin.site.register(AMD) #Армянских драмов
admin.site.register(BYR) #Белорусских рублей
admin.site.register(BGN) #Болгарский лев
admin.site.register(BRL) #Бразильский реал
admin.site.register(HUF) #Венгерских форинтов
admin.site.register(KRW) #Вон Республики Корея
admin.site.register(DKK) #Датских крон
admin.site.register(INR) #Индийских рупий
admin.site.register(KZT) #Казахских тенге
admin.site.register(CAD) #Канадский доллар
admin.site.register(KGS) #Киргизских сомов
admin.site.register(CNY) #Китайских юаней
admin.site.register(LVL) #Латвийский лат
admin.site.register(LTL) #Литовский лит
admin.site.register(MDL) #Молдавских леев
admin.site.register(RON) #Новых румынских леев
admin.site.register(TMT) #Новый туркменский манат
admin.site.register(NOK) #Норвежских крон
admin.site.register(PLN) #Польских злотых
admin.site.register(XDR) #СДР (специальные права заимствования)
admin.site.register(SGD) #Сингапурский доллар
admin.site.register(TJS) #Таджикских сомони
admin.site.register(TRY) #Турецкая лира
admin.site.register(UZS) #Узбекских сумов
admin.site.register(UAH) #Украинских гривен
admin.site.register(GBP) #Фунт стерлингов Соединенного королевства
admin.site.register(CZK) #Чешских крон
admin.site.register(SEK) #Шведских крон
admin.site.register(CHF) #Швейцарский франк
admin.site.register(ZAR) #Южноафриканских рэндов
admin.site.register(JPY) #Японских иен