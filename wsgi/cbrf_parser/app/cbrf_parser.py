"""
Парсер сайта http://www.cbr.ru/
"""

__author__ = 'Alexey Kutepov'

import datetime

from bs4 import *

from cbrf_parser.app.web_connector import web_connector
from cbrf_parser.app.constants import WEB_ADDRESS_CB_RF
from currency_to_rub.constants import CURRENCY_CLASSES


# Парсер сайта ЦБРФ
class CbrfParser:

    def __init__(self, login=None, password=None):
        self.web_connector = web_connector(login,password)

    # Метод-парсер. Читает данные с сайта и актуализирует информацию в БД
    def parse(self, web_address, date=datetime.date.today()):
        page = self.web_connector.open_page(web_address)
        if page!=None:
            soup_page = BeautifulSoup(page.read())
            table = soup_page('td')
            found = False
            count = 3
            units = 0
            key = ""
            for record in table:
                value = record.string
                if not value: continue
                value = value.strip()
                if found:
                    count = count-1
                    if count == 2:
                        units = int(value)
                    if count == 0:
                        value = value.replace(",",".")
                        value = float(value)
                        print(key, units, value, date)
                        CURRENCY_CLASSES[key](units=units, value=value, date=date).save()
                        count = 3
                        found = False
                        key = ""
                elif value in CURRENCY_CLASSES.keys():
                    key = value
                    found = True

    # Приватный метод, который запускает парсер n - раз и передаёт ему страницу, с которой нужно прочитать курсы валют
    # n - количество дней
    def __run_parser(self, days, date_from, formated_date_from):
        for i in range(days):
            web_address = WEB_ADDRESS_CB_RF % (formated_date_from[3:5], date_from.year, formated_date_from)
            self.parse(web_address, date_from)
            date_from = date_from+datetime.timedelta(days=1)
            formated_date_from = date_from.strftime("%d.%m.%Y")

    # Фасадный метод. Может запустить как разовое чтение данных, так и регулярное обновление каждое утро
    def load_data(self, days=1, is_event_loop=False):
        date_from = datetime.date.today() - datetime.timedelta(days=(days-1))
        formated_date_from = date_from.strftime("%d.%m.%Y")
        if is_event_loop:
            handled = False
            while True:
                if datetime.datetime.today().hour==1:
                    handled = False
                if datetime.datetime.today().hour==10:
                    if (not handled):
                        self.__run_parser(days, date_from, formated_date_from)
                        handled = True
        else:
            self.__run_parser(days, date_from, formated_date_from)

