import matplotlib.pyplot as plt

values = [i for i in range(1, 1001)]
cubes = [i**2 for i in values]

plt.style.use('dark_background')

fig, ax = plt.subplots()
ax.set_title("Cubes Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubes of Value", fontsize=14)

ax.scatter(values, cubes, c=cubes, cmap=plt.cm.Blues, s=20)
ax.axis([0, 1000, 0, 1000000])
plt.show()
fig.savefig('images/cubes_plot.png', bbox_inches='tight')#2 - обрезает лишнее