__author__ = 'Alexey Kutepov'

import math

# Класс описывает нейрон
class Neuron:
    def __init__(self, a=0.5):
        super().__init__()
        self.a = a

    # Вычисляет текущее состояние нейрона
    def _state(self, x, weights):
        state = 0
        for i in range(len(x)):
            state += x[i] * weights[i]
        return state

    # Функция состояния нейрона
    def _f(self, state):
        return 1 / (1 + math.exp(- self.a * state))

    # Активирует нейрон и возвращает результирующее значение
    def action(self, x, weights):
        if not isinstance(x, list) or not isinstance(weights, list):
            raise AttributeError("ERROR: x or weights is not list")
        if len(x) != len(weights):
            raise ValueError("ERROR: len(x) != len(weights)")
        state = self._state(x, weights)
        return self._f(state)
