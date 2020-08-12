import random
import numpy as np
import time
class Lif_neuron:

	def __init__(self, time_Lif, rate_Lif, v_Lif, firingList_Lif, g_Lif, threshold_Lif, potential_timecount):
		self.time_Lif = time_Lif
		self.rate_Lif = rate_Lif
		self.v_Lif = v_Lif
		self.firingList_Lif = firingList_Lif
		self.g_Lif = g_Lif	  		
		self.threshold_Lif = threshold_Lif
		self.potential_timecount = potential_timecount
	def claculate(self):
		rest = 0
		reset = 0
		noise = 0
		current_Lif = 50
		##time_count = 0
		##spike_count = 0
		##Lrate = 0
		vValue = rest
		is_firing = False
		unit_count = 1.666
		time_count = 0
		spike_count = 0
		fireRateValue = 0
		while time_count < 500:
			#vValue = rest
			#self.v_Lif.append(vValue)
			vValue += -self.g_Lif * (vValue - rest) + current_Lif + random.randint(0, noise) - noise / 2	
			time_count = unit_count * (3/5)
			unit_count += 1
			self.v_Lif.append(vValue)
			self.potential_timecount.append(time_count) 	
			##self.rate_Lif.append(Lrate)
			#self.time_Lif.append(time_count)
			#self.rate_Lif.append(Lrate)
			if vValue >= self.threshold_Lif and is_firing == False:	
				is_firing = True
				spike_count += 1
				vValue = reset
				#self.v_Lif.append(vValue)
			if vValue < self.threshold_Lif and is_firing == True:
				is_firing = False
				#self.v_Lif.append(vValue)
				
			##Lrate = spike_count
			if fireRateValue > 100:
				break
			self.v_Lif.append(vValue)
			self.potential_timecount.append(time_count)
			self.time_Lif.append(time_count)
			fireRateValue = spike_count / time_count
			#print(fireRateValue)
			self.firingList_Lif.append(fireRateValue)

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
	
	def firing_status(self):
		return self.firingList_Lif
		
	def th(self):
		return self.threshold_Lif

	def g(self):
		return self.g_Lif
