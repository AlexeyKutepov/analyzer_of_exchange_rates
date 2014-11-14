__author__ = 'kutepoval'

class Currency:

    def __init__(self, state, char_code, name, value, units, change, link):
        # Определяет выросла валюта в цене или упала
        self.state = state
        #Инициалы валюты (например USD или EUR)
        self.char_code = char_code
        #Подробное название валюты
        self.name = name
        #Цена
        self.value = value
        #Количество единиц валюты сумма которых равна value
        self.units = units
        #Значение на которое изменилась валюта
        self.change = change
        #Ссылка на страницу с подробными данными о данной валюте
        self.link = link