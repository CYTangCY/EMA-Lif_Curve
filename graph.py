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
g = 0.09
th = 40
timePo = []

_Lif = Lif_neuron(Lift, Lifr, _v, FiringStatus, g, th, timePo)
_Lif.claculate()
#_Lif.firing_rate()
#print(_v)

fig =  plt.figure(figsize =(15,10))
plt.title('Lif_firingrate')
plt.xlabel('time')
plt.ylabel('rate')
plt.plot(EMAr, '--')
plt.plot(Lift, FiringStatus, '--')
plt.grid(True)
#fig.savefig('th87', format = 'jpg')
print('gelak: ',g)
print('threshold: ',th)
"""
fig1 = plt.figure(figsize = (50, 30))
plt.title('???')
plt.xlabel('????')
plt.ylabel('rate')
plt.plot(_Lif.firing_status(), 'bo-')
plt.grid(True)
"""

fig2 = plt.figure(figsize = (15, 10))
plt.title('Lif_potential')
plt.xlabel('time')
plt.ylabel('potential')
plt.plot(timePo, _v)
plt.grid(True)


plt.show()

