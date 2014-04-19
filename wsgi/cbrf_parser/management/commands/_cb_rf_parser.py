__author__ = 'Alexey'

from cbrf_parser.management.commands._web_connector import web_connector
from cbrf_parser.management.commands._constants import WEB_ADDRESS_CB_RF
from currency_to_rub.constants import CURRENCY_CLASSES
from bs4 import *
import datetime

class CBRFParser:

    def __init__(self, login=None, password=None):
        self.web_connector = web_connector(login,password)


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
                        record = CURRENCY_CLASSES[key](units=units, value=value, date=date)
                        try:
                            old_value = CURRENCY_CLASSES[key].objects.get(date=date).value
                        except:
                            old_value = None
                        if old_value == None:
                            record.save()
                        count = 3
                        found = False
                        key = ""
                if value in CURRENCY_CLASSES.keys():
                    key = value
                    found = True

    def load_data(self, days=1):
        date = datetime.date.today() - datetime.timedelta(days=(days-1))
        date_f = date.strftime("%d.%m.%Y")
        for i in range(days):
            web_address = WEB_ADDRESS_CB_RF % (date_f[3:5], date.year, date_f)
            self.parse(web_address, date)
            date = date+datetime.timedelta(days=1)
            date_f = date.strftime("%d.%m.%Y")