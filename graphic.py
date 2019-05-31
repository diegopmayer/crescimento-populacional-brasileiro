import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 4, 6, 8, 10]
z = [3, 7, 11, 15, 19]

plt.plot(x, y, z, label='Name_Label')
plt.bar(x, y)
plt.show()