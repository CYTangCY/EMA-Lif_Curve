import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from EMA_curve import EMA
from Lif_rate import Lif_neuron

Lift = []
Lifr = []
v = []
FiringList = []
th_list = []
g_list = []
rest_list = []
reset_list = []
LifPt = []
maxfr_list = []
noise = 0
current = 0.5
rest = -65
reset = -68
g = 0.12
th = -50
c = 1

"""
for th in range (-50, -45, 1):
	for g in np.arange(0, 1, 0.001):
		_Lif = Lif_neuron(Lift, Lifr, v, FiringList, g, th, LifPt, rest, reset, current, noise)
		_Lif.claculate()
		if max(FiringList) <= 100 and max(FiringList) != 0:	
			maxfr_list.append(round(max(FiringList),3))
			reset_list.append(reset)
			rest_list.append(rest)
			g_list.append(g)
			th_list.append(th)
		
		#print('g: ',g)
		#print('th: ',th)
		#print('rest: ',rest)
		#print('reset: ',reset)
		#print('maxfr: ',max(FiringList))	
					
		FiringList.clear()
	dict_Lif = {"gValue":g_list, "thValue":th_list, "restValue":rest_list, "resetValue":reset_list, "maxfr":maxfr_list}
	df_Lif = pd.DataFrame(dict_Lif)
	print(df_Lif.info)	
df_Lif.to_csv('T0.1~1havetau.csv', index=False, header=False)
"""	
"""
_Lif = Lif_neuron(Lift, Lifr, v, FiringList, g, th, LifPt, rest, reset, current, noise)
_Lif.claculate()
fig =  plt.figure(figsize =(15,10))
plt.title('EMA')
plt.xlabel('time')
plt.ylabel('rate')
plt.plot(EMAt,EMAr, '--', label = 'EMA_curve_alpha=0.1')
plt.plot(Lift,FiringList, '--', label = 'Lif_curve')
plt.legend()
plt.grid(True)
fig.savefig('alpha0.11', format = 'jpg')
"""


_Lif = Lif_neuron(Lift, Lifr, v, FiringList, g, th, LifPt, rest, reset, noise, c)
_Lif.claculate()

fig1 = plt.figure(figsize = (10, 5))
plt.title('firing_rateLif')
plt.xlabel('time')
plt.ylabel('rate')
plt.plot(Lift, FiringList)
plt.grid(True)

fig2 = plt.figure(figsize = (10, 5))
plt.title('Lif_potential')
plt.xlabel('time')
plt.ylabel('potential')
plt.plot(LifPt, v)

plt.legend()
plt.grid(True)
#fig2.savefig('c=1', format = 'jpg')

plt.show()

