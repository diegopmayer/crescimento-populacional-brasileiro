import matplotlib.pyplot as plt


# data from SUS
data = open('populacao-brasileira.csv').readlines()
x = []
y = []

for i in range(len(data)):
    if i != 0:
        line = data[i].split(';')
        x.append(int(line[0]))
        y.append(int(line[1]))

# labels
plt.title('Crescimento da População Brasileira 1980 - 2016')
plt.xlabel('Ano')
plt.ylabel('População x 100.000.000')

# plotation to graphic
plt.bar(x, y, color='#e4e4e4')
plt.plot(x, y, color='k', linestyle='--')

#print out of the screen
plt.show()

#to export in pdf or png, have to remove the show, in this case it's print out
#plt.savefig('growth_population_brazil.pdf')
#plt.savefig('growth_population_brazil.png', dpi=300)
