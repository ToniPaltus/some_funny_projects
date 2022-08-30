import matplotlib.pyplot as plt

input_values = [i for i in range(1, 6)]
squares = [i ** 2 for i in input_values]

plt.style.use('seaborn')
fig, ax = plt.subplots() #Позволяет сгенерировать 1 или несколько поддиаграм на одной диаграмме. fig - весь рисунок, ax - поддиаграмма

ax.plot(input_values, squares, linewidth=3)

#Назначение заголовка диаграммы и меток осей
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Назначение размера шрифта делений на осях
ax.tick_params(axis='both', labelsize=14)

plt.show()
fig.savefig('images/squares.png')