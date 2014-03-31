"""
Алгоритм прогнозирования "k ближайших соседей"
"""

__author__ = 'kutepoval'

import math
import datetime
from currency_to_rub.constants import CURRENCY_DATA, CURRENCY_CLASSES

#Эвклидово расстояние
def euclidean(vector1, vector2):
    distance = 0.0
    for i in range(len(vector1)):
        distance += float((vector1[i]-vector2[i])**2)
    return math.sqrt(distance)

#Формирование сортированного массива со значениями эвклидового расстояния
def get_distance(vector1, currency, days, date):
    distance_list = []
    for i in range(days):
        vector2 = []
        for item in CURRENCY_DATA:
            try:
                if item['char_code']!=currency:
                    vector2.append(
                        item['class'].objects.get(date=date-datetime.timedelta(days=i)).value
                    )
                    distance_list.append((euclidean(vector1,vector2), date-datetime.timedelta(days=i)))
            except:
                continue
    distance_list.sort()
    return distance_list

#Получаем вектор из значений курсов валют на дату, предшествующей дате прогноза
def get_input_vector(currency, date=datetime.date.today()):
    vector = []
    for item in CURRENCY_DATA:
        try:
            if item['char_code']!=currency:
                vector.append(
                    item['class'].objects.get(date=date).value
                )
        except:
            continue
    return vector

#Запуск алгоритма
def knn(currency, days, date, k=5):
    vector = get_input_vector(currency, date)
    distance_list = get_distance(vector, currency, days, date-datetime.timedelta(days=1))
    result = 0.0
    for i in range(k):
        result += float(CURRENCY_CLASSES[currency].objects.get(date=distance_list[i][1]).value)
    result = result/k
    return result