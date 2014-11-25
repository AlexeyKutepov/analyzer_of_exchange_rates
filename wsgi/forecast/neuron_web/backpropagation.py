"""
Обучение нейронной сети
Метод обратного распространения ошибки.
"""

__author__ = 'Alexey Kutepov'

from forecast.neuron_web.layer import Layer
from forecast.neuron_web.neuron import Neuron
import random

# Построение сети с одним скрытым и одним внешним слоем и с произвольными весовыми коэффициентами
def build_neuron_web(hidden_layer_neurons=10, out_layer_neurons=5):
    # Скрытый слой
    hidden_layer = Layer()
    for i in range(hidden_layer_neurons):
        hidden_layer.put(Neuron())

    hidden_weights = []
    for i in range(hidden_layer_neurons):
        weights = []
        for j in range(hidden_layer_neurons):
            weights.append(random.random())
        hidden_weights.append(weights)

    # Внешний выходной слой
    out_layer = Layer()
    for i in range(out_layer_neurons):
        out_layer.put(Neuron())