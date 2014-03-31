"""
Парсер сайта http://www.cbr.ru/
"""
__author__ = 'kutepoval'

#Комманды парсера ЦБРФ:
#parse_cbrf USD n (где n - количество дней)
from django.core.management.base import BaseCommand, CommandError
from cbrf_parser.management.commands._cb_rf_parser import *

class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            days = int(args[0])
        except:
            raise CommandError('Command Error: incorrectly stated the number of days')
        command = input("Do you want to enter the username and password for the proxy server? (y/n): ")
        if command=='y':
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            parser = CBRFParser(username, password)
        else:
            parser = CBRFParser()
        parser.load_data(days)
