import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 2, s=200) #Отобразить точку в этом месте, s - size

#Назначение заголовка диаграммы и меток осей
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Назначение размера шрифта делений на осях
#ax.tick_params(axis='both', which='major', labelsize=14)

x_values = [i for i in range(1, 1001)]
y_values = [i**2 for i in x_values]
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)#c='red' or c=(0, 0.8, 0)

#Назначение диапазона для каждой оси
ax.axis([0, 1000, 0, 1000000])

plt.show()
fig.savefig('images/squares_plot.jpg', bbox_inches='tight')#2 - обрезает лишнее