import random
import numpy as np
import time
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
	
		if len(self.firingList_Lif) > 0:
				self.rate_Lif.append(max(self.firingList_Lif))	

		if len(self.firingList_Lif) <= 0:
				self.rate_Lif.append(0)
			#if len(self.v_Lif) >= 30:
			#	break
#		print('MaxRate: ',round(self.firingList_Lif[-1],1))
#		print('MaxTime: ',len(self.firingList_Lif))	

	def time(self):
		return self.time_Lif

	def rate(self):
		return self.rate_Lif

	def v(self):
		return self.v_Lif
	
	def firing_List(self):
		return self.firingList_Lif
		
	def th(self):
		return self.threshold_Lif

	def g(self):
		return self.g_Lif

	def rest(self):
		return self.rest_Lif

	def reset(self):
		return self.reset_Lif

	def current(self):
		return self.current_Lif

	def noise(self):
		return self.noise_Lif

	def Pt(self):
		return self.potential_timecount
