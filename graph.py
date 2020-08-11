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
_g_List = []
for _g in np.arange(3, 0.01, -0.01):
	_g_List.append(_g)
	_Lif = Lif_neuron(Lift, Lifr, _v, FiringStatus, _g, _th)
	_Lif.claculate()
#_Lif.firing_rate()
#print(_v)

	fig =  plt.figure(figsize =(10,5))
	plt.title('LifMaxrate')
	plt.xlabel('g_Value')
	plt.ylabel('Max_rate')
	#plt.plot(_EMA.rate(), '--', label = 'EMA_curve')
	plt.plot(_g_List,_Lif.rate(), 'ro', label = 'g0.001-0.0001')
	plt.legend()
	plt.grid(True)
	fig.savefig('g0.001-0.0001', format = 'png')

"""
fig1 = plt.figure(figsize = (50, 30))
plt.title('firing_rateLif')
plt.xlabel('time')
plt.ylabel('rate')
plt.plot(_Lif.firing_status(), 'bo-')
plt.grid(True)
"""
"""
fig2 = plt.figure(figsize = (30, 20))
plt.title('Lif_potential')
plt.xlabel('time')
plt.ylabel('potential')
plt.plot( _Lif.v())
plt.grid(True)
"""
#plt.show()

