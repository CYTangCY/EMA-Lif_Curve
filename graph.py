import numpy as np
import matplotlib.pyplot as plt
from EMA_2 import EMA
from lif_neuron_firingrate_slope import Lif_neuron

EMAt = []
EMAr = []
_EMA = EMA(EMAt,EMAr)
_EMA.claculate()
#print(_EMA.time())
#print(_EMA.rate())

Lift = []
Lifr = []
_v = []
FiringStatus = []
_th = 50
#_g = 0.09
_g_List = []
LifPt = []

for _g in np.arange(3, 0.01, -0.01):
	_g_List.append(_g)
	_Lif = Lif_neuron(Lift, Lifr, _v, FiringStatus, _g, _th, LifPt)
	_Lif.claculate()
#_Lif.firing_rate()
#print(_v)

	fig =  plt.figure(figsize =(10,5))
	plt.title('LifMaxrate')
	plt.xlabel('g_Value')
	plt.ylabel('Max_rate')
	#plt.plot(_EMA.rate(), '--', label = 'EMA_curve')
	plt.plot(_g_List,_Lif.rate(), 'ro', label = 'g3-0.01')
	plt.legend()
	plt.grid(True)
	fig.savefig('g3-0.01', format = 'jpg')

"""
_Lif = Lif_neuron(Lift, Lifr, _v, FiringStatus, _g, _th, LifPt)
_Lif.claculate()
#print(LifPt)
#print(Lift)

fig1 = plt.figure(figsize = (10, 5))
plt.title('firing_rateLif')
plt.xlabel('time')
plt.ylabel('rate')
plt.plot(Lift, FiringStatus, 'bo-')
plt.grid(True)
"""
"""
fig2 = plt.figure(figsize = (10, 5))
plt.title('Lif_potential')
plt.xlabel('time')
plt.ylabel('potential')
plt.plot(LifPt, _Lif.v())
plt.grid(True)
"""
#plt.show()

