import random
from forecast.neuron_web.layer import Layer
from forecast.neuron_web.neuron import Neuron

__author__ = 'Alexey Kutepov'


# Построение персептрона с заданными параметрами:
# neurons - список (количество нейронов в каждом слое)
def build_perceptron(neurons):
    neuron_web = NeuronWeb()
    for k in range(len(neurons)):
        layer = Layer()
        weights = []
        if k == 0:    # Входные веса для первого слоя
            for j in range(neurons[k]):
                weights.append(1)
        else:         # Входные веса для последующих слоёв
            for j in range(neurons[k-1]):
                weights.append(random.random())
        for i in range(neurons[k]):
            layer.put(Neuron(weights))
        neuron_web.add_item(layer)
    return neuron_web

# Обучение, алгоритм обратного распространения ошибки
def backpropagation(neuron_web, input_data, correct_data, eta=0.1):
    neuron_web.action(input_data)
    layers = neuron_web.get_items()
    sigma_k = []
    for l in reversed(range(len(layers))):
        if l == len(layers) - 1:    # Выходной слой
            layer = layers[l].layer
            for i in range(len(layer)):
                sigma = layer[i].y * (1 - layer[i].y) * (correct_data[i] - layer[i].y)
                sigma_k.append(sigma)
                for j in range(len(layers[l].layer[i].weights)):
                    layer[i].weights[j] = layer[i].weights[j] + eta * sigma * layer[i].x[j]
        else:   # Скрытый слой
            sigma_buf = []
            for i in range(len(layers[l].layer)):
                s = 0.0
                for n in range(len(sigma_k)):
                    s += sigma_k[n] * layers[l+1].layer[n].weights[i]
                sigma = layers[l].layer[i].y * (1 - layers[l].layer[i].y) * s
                sigma_buf.append(sigma)
                for j in range(len(layers[l].layer[i].weights)):
                    layers[l].layer[i].weights[j] = layers[l].layer[i].weights[j] + eta * sigma * layers[l].layer[i].x[j]
            sigma_k = sigma_buf[:]



# Структура нейронной сети
class NeuronWeb():
    def __init__(self):
        super().__init__()
        self.items = []

    def add_item(self, item):
        if not isinstance(item, Layer):
            raise AttributeError("ERROR: item is not Layer")
        self.items.append(item)

    def get_items(self):
        return self.items

    # Возвращает результат работы нейронной сети
    def action(self, x):
        y = x
        for item in self.items:
            y = item.action(y)
        return y



if __name__ == "__main__":
    neuron_web = build_perceptron([10, 20, 20, 1])
    result = neuron_web.action([1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0])
    print("before learn: ", result)
    for i in range(100):
        backpropagation(neuron_web, [1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0], [0.5,], 0.8)
        result = neuron_web.action([1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0])
        print("after learn: ", result)

