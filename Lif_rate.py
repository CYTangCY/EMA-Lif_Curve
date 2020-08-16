import random
import numpy as np
import time
from numba import jit
class Lif_neuron:

	def __init__(self, time_Lif, rate_Lif, v_Lif, firingList_Lif, g_Lif, threshold_Lif, potential_timecount, rest_Lif, reset_Lif, current_Lif, noise_Lif):
		self.time_Lif = time_Lif
		self.rate_Lif = rate_Lif
		self.v_Lif = v_Lif
		self.firingList_Lif = firingList_Lif
		self.g_Lif = g_Lif	  		
		self.rest_Lif = rest_Lif
		self.reset_Lif = reset_Lif
		self.current_Lif = current_Lif
		self.threshold_Lif = threshold_Lif
		self.noise_Lif = noise_Lif
		self.potential_timecount = potential_timecount

	@jit
	def claculate(self):
		vValue = self.rest_Lif
		is_firing = False
		unit_count = 50
		time_count = 0
		spike_count = 0
		fireRateValue = 0
		
		while time_count <= 1:

			vValue += -self.g_Lif * (vValue - self.rest_Lif) + self.current_Lif + random.randint(0, self.noise_Lif) - self.noise_Lif / 2	
			time_count = unit_count / 1500
			unit_count += 1
			self.v_Lif.append(vValue)
			self.potential_timecount.append(time_count) 	

			if vValue >= self.threshold_Lif and is_firing == False:	
				is_firing = True
				spike_count += 1
				vValue = self.reset_Lif
				fireRateValue = spike_count / time_count

			if vValue < self.threshold_Lif and is_firing == True:
				is_firing = False
				
			self.v_Lif.append(vValue)
			self.firingList_Lif.append(fireRateValue)
			self.potential_timecount.append(time_count)
			self.time_Lif.append(time_count)
	
#		print('MaxRate: ',round(self.firingList_Lif[-1],1))
#		print('MaxTime: ',len(self.firingList_Lif))	

	@jit
	def time(self):
		return self.time_Lif
	@jit
	def rate(self):
		return self.rate_Lif
	@jit
	def v(self):
		return self.v_Lif
	@jit
	def firing_List(self):
		return self.firingList_Lif
	@jit	
	def th(self):
		return self.threshold_Lif
	@jit
	def g(self):
		return self.g_Lif
	@jit
	def rest(self):
		return self.rest_Lif
	@jit
	def reset(self):
		return self.reset_Lif
	@jit
	def current(self):
		return self.current_Lif
	@jit
	def noise(self):
		return self.noise_Lif
	@jit
	def Pt(self):
		return self.potential_timecount
