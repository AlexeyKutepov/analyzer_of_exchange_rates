"""
Обучение нейронной сети
Метод обратного распространения ошибки.
"""

__author__ = 'Alexey Kutepov'

from forecast.neuron_web.layer import Layer
from forecast.neuron_web.neuron import Neuron
from forecast.neuron_web.neuron_web import NeuronWebItem, NeuronWeb
import random

# Построение персептрона с заданными параметрами:
def build_perceptron(layers, neurons):
    if len(neurons) != layers:
        raise AttributeError("ERROR: len(neurons) != layers")
    neuron_web = NeuronWeb()
    for k in range(layers):
        layer = Layer()
        for i in range(neurons[k]):
            layer.put(Neuron())
        weights = []
        for i in range(neurons[k]):
            weights_in = []
            if k == 0:
                n = neurons[k]
            else:
                n = neurons[k-1]
            for j in range(n):
                weights_in.append(random.random())
            weights.append(weights_in)
        neuron_web.add_item(
            NeuronWebItem(layer, weights)
        )

    return neuron_web


# Обучение
# def learn(neuron_web, input_data, correct_data, eta=0.1, alpha=0.5):
#     neuron_web.action(input_data)
#     web_items = neuron_web.get_items()
#     sigma = []
#     for i in reversed(range(len(web_items))):
#         layer_result = web_items[i].get_result()
#         if sigma == []:
#             for j in range(len(layer_result)):
#                 sigma.append(
#                     layer_result[j]*(1 - layer_result[j])*(correct_data[j] - layer_result[j])
#                 )
#         else:
#             sigma_j = []
#             for j in range(len(layer_result)):
#                 summ = 0.0
#                 for k in range(len(sigma)):
#                     summ += sigma[k] * web_items[i].get_weights()[j][k]
#                 sigma_j.append(
#                     layer_result[j] * (1 - layer_result[j]) + summ
#                 )
#                 delta = (1 - alpha) * eta*sigma_j[j]*layer_result[j]
#                 for k in range(len(web_items[i].get_weights()[j])):
#                     web_items[i].get_weights()[j][k] += delta
#     result = neuron_web.action(input_data)
#     return result



if __name__ == "__main__":
    neuron_web = build_perceptron(3, [10, 15, 1])
    result = neuron_web.action([1, 0.2, 0.3, 0.4, 0.5, 0.1, 0.2, 0.3, 0.4, 0])
    print("before learn: ", result)
    # for i in range(10000):
    #     print(
    #         learn(neuron_web, [1, 0.2, 1, 0.4, 0, 0.1, 0.2, 0.3, 0.4, 0], [0.3,])
    #     )