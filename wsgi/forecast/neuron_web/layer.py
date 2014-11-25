__author__ = 'Alexey Kutepov'

from forecast.neuron_web.neuron import Neuron

# Слой для хранения нейронов
class Layer:
    def __init__(self):
        super().__init__()
        self.layer = []

    # Метод добавления нейрона в слой
    def put(self, neuron):
        if not neuron is Neuron:
            raise AttributeError("ERROR: argument 'neuron' is not Neuron")
        self.layer.append(neuron)

    #Возвращает список нейронов слоя
    def get_neuron_list(self):
        return self.layer

    # Активирует слой нейронов и возвращает список знечений
    def action(self, x, weights):
        result = []
        for item in self.layer:
            result.append(
                item.action(x, weights)
            )
        return result