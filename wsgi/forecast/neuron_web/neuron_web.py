import random
from forecast.neuron_web.layer import Layer
from forecast.neuron_web.neuron import Neuron

__author__ = 'Alexey Kutepov'


# Построение персептрона с заданными параметрами:
# layers - количество слоёв
# neurons - список (количество нейронов в каждом слое)
def build_perceptron(layers, neurons):
    if len(neurons) != layers:
        raise AttributeError("ERROR: len(neurons) != layers")
    neuron_web = NeuronWeb()
    for k in range(layers):
        layer = Layer()
        weights = []
        if k == 0:
            n = neurons[k]
        else:
            n = neurons[k-1]
        for j in range(n):
            weights.append(random.random())
        for i in range(neurons[k]):
            layer.put(Neuron(weights))
        neuron_web.add_item(
            layer
        )

    return neuron_web

# Структура нейронной сети
class NeuronWeb():
    def __init__(self):
        super().__init__()
        self._items = []

    def add_item(self, item):
        if not isinstance(item, Layer):
            raise AttributeError("ERROR: item is not Layer")
        self._items.append(item)

    def get_items(self):
        return self._items

    # Возвращает результат работы нейронной сети
    def action(self, x):
        y = x
        for item in self._items:
            y = item.action(y)
        return y




