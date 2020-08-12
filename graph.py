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
v = []
FiringList = []
#g_List = []
LifPt = []
noise = 0
current = 50
th = 225
g = 0.285
rest = 50
reset = 30

"""
for g in np.arange(0.35, 0.2, -0.001):
	g_List.append(_g)
	_Lif = Lif_neuron(Lift, Lifr, v, FiringList, g, th, LifPt, rest, reset, current, noise)
	_Lif.claculate()
#_Lif.firing_rate()
#print(_v)

	fig =  plt.figure(figsize =(10,5))
	plt.title('LifMaxrate')
	plt.xlabel('g_Value')
	plt.ylabel('Max_rate')
	#plt.plot(EMAr, '--', label = 'EMA_curve')
	plt.plot(g_List,Lifr, 'ro', label = 'g1-0.01')
	plt.legend()
	plt.grid(True)
	fig.savefig('g1-0.01', format = 'jpg')
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

plt.show()

