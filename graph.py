import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from EMA_curve import EMA
from Lif_rate import Lif_neuron

EMAt = []
EMAr = []
_EMA = EMA(EMAt,EMAr)
_EMA.claculate()
#print(_EMA.time())
#print(_EMA.rate())

Lift = []
Lifr = []
v = []
FiringList = []
#th_list = []
g_list = []
#rest_list = []
#reset_list = []
LifPt = []
maxfr_list = []
noise = 0
current = 50
th = 200
rest = 50
reset = 10
for g in np.arange(0.311, 0.335, 0.0001):
	_Lif = Lif_neuron(Lift, Lifr, v, FiringList, g, th, LifPt, rest, reset, current, noise)
	_Lif.claculate()
	if max(FiringList) <= 290:	
		maxfr_list.append(round(max(FiringList),3))
		g_list.append(g)
	print('g: ',g)
	print('th: ',th)
	print('rest: ',rest)
	print('reset: ',reset)
	print('maxfr: ',max(FiringList))	
	dict_Lif = {"gValue":g_list, "maxfr":maxfr_list}
	df_Lif = pd.DataFrame(dict_Lif)
	print(df_Lif.info)
	FiringList.clear()
df_Lif.to_csv('test.csv', index=False, header=False)
	

			#_Lif.firing_rate()
			#print(_v)

				#fig =  plt.figure(figsize =(10,5))
				#plt.title('LifMaxrate')
				#plt.xlabel('g_Value')
				#plt.ylabel('Max_rate')
				#plt.plot(EMAr, '--', label = 'EMA_curve')
				#plt.plot(g_List,Lifr, 'ro', label = 'g1-0.01')
				#plt.legend()
				#plt.grid(True)
				#fig.savefig('g1-0.01', format = 'jpg')

"""
_Lif = Lif_neuron(Lift, Lifr, v, FiringList, g, th, LifPt, rest, reset, current, noise)
_Lif.claculate()

fig1 = plt.figure(figsize = (10, 5))
plt.title('firing_rateLif')
plt.xlabel('time')
plt.ylabel('rate')
plt.plot(Lift, FiringList, 'b-')
plt.grid(True)
print('gleak',g)
print('threshold',th)

fig2 = plt.figure(figsize = (10, 5))
plt.title('Lif_potential')
plt.xlabel('time')
plt.ylabel('potential')
plt.plot(LifPt, v)
plt.grid(True)
"""
#plt.show()

