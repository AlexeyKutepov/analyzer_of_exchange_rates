__author__ = 'Alexey Kutepov'

# Структура нейронной сети
class NeuronWeb():
    def __init__(self):
        super().__init__()
        self._items = []

    def add_item(self, item):
        if not isinstance(item, NeuronWebItem):
            raise AttributeError("ERROR: item is not NeuronWebItem")
        self._items.append(item)

    def get_items(self):
        return self._items

    # Возвращает результат работы нейронной сети
    def action(self, x):
        y = x
        for item in self._items:
            layer = item.get_layer()
            y = layer.action(y, item.get_weights())
            item.set_result(y)
        return y

# Элемент нейронной сети содержащий одн слой и матрицу весов
class NeuronWebItem:
    def __init__(self, layer, weights):
        super().__init__()
        self._layer = layer
        self._weights = weights
        self._result = []

    def set_weights(self, weights):
        self._weights = weights

    def set_result(self, y):
        self._result = y

    def get_layer(self):
        return self._layer

    def get_weights(self):
        return self._weights

    def get_result(self):
        return self._result