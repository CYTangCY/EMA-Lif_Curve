import numpy as np
import matplotlib.pyplot as plt
from EMA_2 import EMA
from lif_neuron_firingrate_slope import Lif_neuron

EMAt = [0]
EMAr = [0]
_EMA = EMA(EMAt,EMAr)
_EMA.__init__(EMAt, EMAr)
_EMA.claculate()
#print(_EMA.time())
#print(_EMA.rate())

Lift = [0]
Lifr = [0]
_Lif = Lif_neuron(Lift, Lifr)
_Lif.__init__(Lift, Lifr)
_Lif.claculate()
print(Lifr)

fig =  plt.figure(figsize =(20,10))
plt.title('Lif vs EMA')
plt.xlabel('time')
plt.ylabel('rate')
plt.plot(_EMA.time(), _EMA.rate(), 'ro-')
plt.plot(_Lif.time(), _Lif.rate(), 'go-')
plt.grid(True)
plt.show()

