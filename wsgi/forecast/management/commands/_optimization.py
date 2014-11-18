import random

__author__ = 'Alexey Kutepov'


from currency.constants import CURRENCY_CLASSES
from forecast.management.commands._forekast_time_series import  *
import datetime

# Возвращает "стоимость" целевой функции прогнозирования
# Стоимость равна среднему значению модуля ошибки
def cost(alpha, phi, gamma, delta, days=100, steps=1, currency="USD"):
    currency_values_list = (
            CURRENCY_CLASSES[currency].objects
                .filter(date__gte=datetime.date.today()-datetime.timedelta(days=days))
                .order_by('date').values_list('value', flat=True)
        )
    # Настройка предсказателя
    forecast_class = ForecastTimeSeries(
        level=[],
        alpha=alpha,
        phi=phi,
        gamma=gamma,
        delta=delta,
        trend=[0.0,],
        forecast_error=[0.0,],
    )
    result_list = forecast_class.get_forecast(currency_values_list, steps)
    count = days - steps
    result = 0.0
    for i in range(count):
        result += abs(float(currency_values_list[i]) - result_list[i+steps])
    return result

def inc(x, d):
    res = x+0.01
    if (res) <= d:
        return res
    else:
        return x

def dec(x, d):
    res = x-0.01
    if (res) >= d:
        return res
    else:
        return x

# Алгоритм спуска с горы
def hill_climb():
    #Ограничения
    domain = [
        (0, 1),
        (0, 1),
        (0, 1),
        (0, 1),
    ]
    #Начальные значения для функции
    current_state = [
        random.random(),
        random.random(),
        random.random(),
        random.random(),
    ]
    print("current cost = ", cost(current_state[0], current_state[1], current_state[2], current_state[3]))
    while True:
        neighbors = []
        for i in range(len(domain)):
            state = current_state[:]
            state[i] = dec(state[i], domain[i][0])
            neighbors.append(
                state
            )
            state = current_state[:]
            state[i] = inc(state[i], domain[i][1])
            neighbors.append(
                state
            )
        current = cost(current_state[0], current_state[1], current_state[2], current_state[3])
        best = current
        for i in range(len(neighbors)):
            res = cost(neighbors[i][0], neighbors[i][1], neighbors[i][2], neighbors[i][3])
            if res < best:
                best = res
                current_state = neighbors[i][:]
        if best == current:
            print("result cost = ", best)
            return [best, current_state]