"""
Обработчик команд парсера ЦБРФ
Команды парсера ЦБРФ:
    parse_cbrf - Запускает парсер сайта ЦБРФ за определённое количество дней (по умолчанию 1)
Параметры:
    n - количество дней, за которое нужно получить информацию о курсах валют.
        Пример: parse_cbrf 100 - получить информацию за 100 дней
Опции:
    -el - Запускает автоматический сбор данных ежедневно, за период времени указанный в n или
          установленный по умолчанию
"""
__author__ = 'Alexey Kutepov'


from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from cbrf_parser.management.commands._cbrf_parser import CbrfParser

# Класс - обработчик команд
class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--el',
            action='store_true',
            dest='el',
            default=False,
            help='Event Loop start'),
        )


    #Метод для обработки введённых команд
    def handle(self, *args, **options):
        print(options.keys())
        if len(args) == 0:
            days = 1
        else:
            try:
                days = int(args[0])
            except:
                raise CommandError('Command Error: incorrectly stated the number of days')
        if options['el']:
            is_event_loop = True
        else:
            is_event_loop = False
        command = input("Do you want to enter the username and password for the proxy server? (y/n): ")
        if command=='y':
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            cbrf_parser = CbrfParser(username, password)
        else:
            cbrf_parser = CbrfParser()
        cbrf_parser.load_data(days, is_event_loop)
