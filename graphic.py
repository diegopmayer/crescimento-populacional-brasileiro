import matplotlib.pyplot as plt


title_name = 'Brazil Population Growth'
x_name = 'Axis X'
y_name = 'Axis Y'

plt.title(title_name)
plt.xlabel(x_name)
plt.ylabel(y_name)

x = [1, 3, 5, 7, 9]
y = [2, 4, 6, 8, 10]
z = [3, 7, 11, 15, 19]

plt.plot(x, y, color='k')
plt.plot(z, color='r')
plt.bar(x, y)
plt.scatter(x, y, label='Points Plot', color='g', marker='h', s=150)

plt.legend()
plt.show()