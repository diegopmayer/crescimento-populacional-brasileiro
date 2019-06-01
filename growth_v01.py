import matplotlib.pyplot as plt

#Variables with label's name
title_name = 'Crescimento da População Brasileira 1980-2016'
x_name = 'Ano'
y_name = 'População x 100.000.000'

#Functions to label's name
plt.title(title_name)
plt.xlabel(x_name)
plt.ylabel(y_name)
plt.legend()

#data to graphic
ano = [year for year in range(1980, 2016+1)]
pop = [119011052, 121154159, 123774229, 126403352, 129025577, 131639272, 
    134228492, 136780739, 139280140, 141714953, 144090756, 146825475,
    148684120, 151556521, 153726463, 155822296, 157070163, 159636297,
    161790182, 163947436, 169799170, 172385776, 174632932, 176876251,
    179108134, 184184074, 186770613, 189335191, 189612814, 191481045,
    190755799, 192379287, 193976530, 201062789, 202799518, 204482459,
    206114067
]

#plotation from data
plt.bar(ano, pop, color='#e3eee6')
plt.plot(ano, pop, linestyle='dashed', color='k')

#print screen the graphic
plt.show()