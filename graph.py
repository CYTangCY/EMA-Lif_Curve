import numpy as np
import matplotlib.pyplot as plt
from EMA_2 import EMA
from lif_neuron_firingrate_slope import Lif_neuron

EMAt = [0]
EMAr = [0]
_EMA = EMA(EMAt,EMAr)
_EMA.claculate()
#print(_EMA.time())
#print(_EMA.rate())

Lift = []
Lifr = []
_v = []
_Lif = Lif_neuron(Lift, Lifr, _v)
_Lif.claculate()
#print(_v)

fig =  plt.figure(figsize =(30,20))
plt.title('Lif vs EMA')
plt.xlabel('time')
plt.ylabel('rate')
plt.plot(_EMA.time(), _EMA.rate(), 'ro-')
plt.plot(_Lif.time(), _Lif.rate(), 'go-')
plt.grid(True)

fig1 = plt.figure(figsize = (20, 10))
plt.title('Lif_pontential')
plt.xlabel('time')
plt.ylabel('pontential')
plt.plot(_Lif.time(), _Lif.v())
plt.grid(True)

plt.show()

