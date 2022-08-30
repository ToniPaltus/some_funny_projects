from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

#Создание двух кубиков D6
die_1 = Die()
die_2 = Die(10)

#Моделирование результатов бросков и сохранение их в списке
results = []
for roll_num in range(1000):
    results.append(die_1.roll() + die_2.roll())
#print(results)

#Анализ результатов
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequencies.append(results.count(value))
#print(frequencies)

#Визуализация результатов
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Result of Rolling two D6 dice 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='pages/d6_d6.html')