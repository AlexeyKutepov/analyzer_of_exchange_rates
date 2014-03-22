__author__ = 'kutepoval'
from currency_to_rub.models import USD, EUR, AUD, AZN, AMD, BYR, BGN, BRL, HUF, KRW, DKK, INR, KZT, CAD, KGS, CNY, LVL, JPY
from currency_to_rub.models import LTL, MDL, RON, TMT, NOK, PLN, XDR, SGD, TJS, TRY, UZS, UAH, GBP, CZK, SEK, CHF, ZAR

ROWS = 5 #кол-во строк для отображения валюты
COLUMNS = 7 #кол-во столбцов для отображения валюты

#Неизменяющиеся данные о валютах
CURRENCY_DATA = (
    {"class":USD, "char_code":"USD", "name":"Доллар США", "code":"840"},
    {"class":EUR, "char_code":"EUR", "name":"Евро", "code":"978"},
    {"class":AUD, "char_code":"AUD", "name":"Австралийский доллар", "code":"036"},
    {"class":AZN, "char_code":"AZN", "name":"Азербайджанский манат", "code":"944"},
    {"class":AMD, "char_code":"AMD", "name":"Армянский драм", "code":"051"},
    {"class":BYR, "char_code":"BYR", "name":"Белорусский рубль", "code":"974"},
    {"class":BGN, "char_code":"BGN", "name":"Болгарский лев", "code":"975"},
    {"class":BRL, "char_code":"BRL", "name":"Бразильский реал", "code":"986"},
    {"class":HUF, "char_code":"HUF", "name":"Венгерский форинт", "code":"348"},
    {"class":KRW, "char_code":"KRW", "name":"Вон Республики Корея", "code":"410"},
    {"class":DKK, "char_code":"DKK", "name":"Датская крона", "code":"208"},
    {"class":INR, "char_code":"INR", "name":"Индийский рупий", "code":"356"},
    {"class":KZT, "char_code":"KZT", "name":"Казахстанский тенге", "code":"398"},
    {"class":CAD, "char_code":"CAD", "name":"Канадский доллар", "code":"124"},
    {"class":KGS, "char_code":"KGS", "name":"Киргизский сом", "code":"417"},
    {"class":CNY, "char_code":"CNY", "name":"Китайский юань", "code":"156"},
    {"class":LVL, "char_code":"LVL", "name":"Латвийский лат", "code":"428"},
    {"class":LTL, "char_code":"LTL", "name":"Литовский лит", "code":"440"},
    {"class":MDL, "char_code":"MDL", "name":"Молдавский лей", "code":"498"},
    {"class":RON, "char_code":"RON", "name":"Румынский лей", "code":"946"},
    {"class":TMT, "char_code":"TMT", "name":"Туркменский манат", "code":"934"},
    {"class":NOK, "char_code":"NOK", "name":"Норвежская крона", "code":"578"},
    {"class":PLN, "char_code":"PLN", "name":"Польский злотый", "code":"985"},
    {"class":XDR, "char_code":"XDR", "name":"СДР", "code":"960"},
    {"class":SGD, "char_code":"SGD", "name":"Сингапурский доллар", "code":"702"},
    {"class":TJS, "char_code":"TJS", "name":"Таджикский сомони", "code":"972"},
    {"class":TRY, "char_code":"TRY", "name":"Турецкая лира", "code":"949"},
    {"class":UZS, "char_code":"UZS", "name":"Узбекский сум", "code":"860"},
    {"class":UAH, "char_code":"UAH", "name":"Украинская гривна", "code":"980"},
    {"class":GBP, "char_code":"GBP", "name":"Фунт стерлингов", "code":"826"},
    {"class":CZK, "char_code":"CZK", "name":"Чешская крона", "code":"203"},
    {"class":SEK, "char_code":"SEK", "name":"Шведская крона", "code":"752"},
    {"class":CHF, "char_code":"CHF", "name":"Швейцарский франк", "code":"756"},
    {"class":ZAR, "char_code":"ZAR", "name":"Южноафриканский ранд", "code":"710"},
    {"class":JPY, "char_code":"JPY", "name":"Японская иена", "code":"392"},
)
