__author__ = 'Alexey Kutepov'

import math

# Класс описывает нейрон
class Neuron:
    def __init__(self, weigths, a=0.5):
        super().__init__()
        self.a = a
        self.weights = weigths # Входные веса
        self.y = None # Выходной сигнал
        self.x = None # Входной сигнал


    # Вычисляет текущее состояние нейрона (взвешенная сумма входных сигналов)
    def _state(self, x):
        state = 0
        for i in range(len(x)):
            state += x[i] * self.weights[i]
        return state

    # Функция состояния нейрона
    def _f(self, state):
        return 1 / (1 + math.exp(- self.a * state))

    # Активирует нейрон и возвращает результирующее значение
    def action(self, x):
        if not isinstance(x, list) or not isinstance(self.weights, list):
            raise AttributeError("ERROR: x or weights is not list")
        if len(x) != len(self.weights):
            raise ValueError("ERROR: len(x) != len(weights)")
        self.x = x
        state = self._state(x)
        self.y = self._f(state)
        return self.y
