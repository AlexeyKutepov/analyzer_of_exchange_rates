"""
Алгоритм прогнозирования временных рядов
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


class ForecastTimeSeries:
    def __init__(self, alpha=0.5, phi=0.5, gamma=0.5, delta=0.5,
                 trend=[0.0,], forecast_error=[0.0,], level=[],):
        self.alpha = alpha
        self.phi = phi
        self.gamma = gamma
        self.delta = delta
        self.trend = trend
        self.level = level
        self.forecast_error = forecast_error

    def __str__(self):
        return super().__str__()


    # Вычисление ошибки прогнозирования
    # current_value - forecast
    def __calculate_forecast_error(self, current_value, forecast):
        self.forecast_error.append(float(current_value)-float(forecast))

    # Вычисление сглаженного тренда
    # trend * phi + alpha * gamma * forecast_error
    def __calculate_trend(self):
        self.trend.append(
            float(
                self.trend[len(self.trend)-1] *
                self.phi +
                self.alpha * self.gamma *
                self.forecast_error[len(self.forecast_error)-1]
            )
        )

    # Вычисление сглаженного уровня последовательности
    # level + trend + alpha * forecast_error
    def __calculate_level(self):
        self.level.append(
            float(
                self.level[len(self.level)-1]) +
                self.trend[len(self.trend)-1] +
                self.alpha *
                float(self.forecast_error[len(self.forecast_error)-1])
            )

    # Вычисление прогноза
    # level + trend * sum_phi + season
    def __calculate_forecast(self, steps=1):
        sum_phi = 0.0
        for i in range(1, steps):
            sum_phi+=self.phi**i
        forecast = self.level[len(self.level)-1] + \
                   self.trend[len(self.trend)-1] * \
                   sum_phi
        return forecast

    # Метод получения прогноза:
    # currency_values_set - числовой ряд
    # steps - количество шагов вперед, на которое делается прогноз (по умолчанию = 1);
    def get_forecast(self, values_list, steps=1):
        result_list = []
        self.level=[values_list[0], ]
        prev_forecast = values_list[0]
        for item in values_list:
            self.__calculate_forecast_error(item, prev_forecast)
            self.__calculate_trend()
            self.__calculate_level()
            result_list.append(self.__calculate_forecast(steps))
            prev_forecast = result_list[len(result_list) - 1]
        return result_list



