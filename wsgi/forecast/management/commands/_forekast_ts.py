"""
alpha – параметр сглаживания уровня последовательности, [0:1];
gamma – параметр сглаживания тренда, [0:1];
delta – параметр сглаживания сезонных индексов, [0:1];
phi – параметр демпфирования, [0:1];
level – сглаженный уровень последовательности, вычисленный в момент времени t после поступления значения ;
trend – сглаженный аддитивный тренд, вычисленный в момент времени t;
season – сглаженный сезонный индекс, вычисленный в момент времени t;
x[t] – значение последовательности в момент времени t;
steps – количество шагов вперед, на которое делается прогноз;
periods    – количество периодов в сезонном цикле;
forecast – прогноз на m шагов вперед сделанный в момент времени t;
forecast_error – ошибка прогнозирования на один шаг вперед на момент времени t, .
"""

__author__ = 'Alexey Kutepov'

class ForecastTS:
    def __init__(self, level=[], alpha=0.5, phi=0.5, gamma=0.5, delta=0.5,
                 trend=[0.0,], forecast_error=[0.0,], season=[0.0,], periods=1):
        self.alpha = alpha
        self.phi = phi
        self.gamma = gamma
        self.delta = delta
        self.trend = trend
        self.level = level
        self.forecast_error = forecast_error
        self.season = season
        self.periods = periods

    # Вычисление ошибки прогнозирования
    def calculate_forecast_error(self, current_value, forecast):
        self.forecast_error.append(float(current_value)-float(forecast))

    # Вычисление сглаженного тренда
    def calculate_trend(self, index):
        self.trend.append(
            float(self.trend[index-1]*self.phi + self.alpha*self.gamma*self.forecast_error[index])
        )

    # Вычисление сглаженного уровня последовательности
    def calculate_level(self, index):
        self.level.append(
            float(self.level[index-1]) + self.trend[index-1] + self.alpha*float(self.forecast_error[index])
        )

    # Вычисление сглаженного сезонного индекса
    def calculate_season_index(self, index):
        self.season.append(
            float(self.season[index-self.periods] + self.delta*(1-self.alpha)*self.forecast_error[index])
        )

    # Вычисление прогноза
    def calculate_forecast(self, steps, index):
        sum_phi = 0.0
        for i in range(1, steps):
            sum_phi+=self.phi**i
        forecast = self.level[index] + self.trend[index]*sum_phi + self.season[index-self.periods+steps]
        return forecast

    def get_forecast(self, value, prev_forecast, steps, index):
        self.calculate_forecast_error(value, prev_forecast)
        self.calculate_trend(index)
        self.calculate_level(index)
        self.calculate_season_index(index)
        return self.calculate_forecast(steps, index)


