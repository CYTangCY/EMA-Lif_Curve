import random
import numpy as np
import time
class Lif_neuron:

	def __init__(self, time_Lif, rate_Lif, v_Lif, firingList_Lif):
		self.time_Lif = time_Lif
		self.rate_Lif = rate_Lif
		self.v_Lif = v_Lif
		self.firingList_Lif = firingList_Lif	  		
	def claculate(self):
		g = 0.009
		rest = 100
		threshold = 200
		reset = 30
		noise = 0
		current_Lif = 50
		##time_count = 0
		##spike_count = 0
		##Lrate = 0
		vValue = rest
		is_firing = False
		unit_count = 1499
		time_count = 0
		spike_count = 0
		fireRateValue = 0
		while time_count <= 1500:
			#vValue = rest
			#self.v_Lif.append(vValue)
			vValue += -g * (vValue - rest) + current_Lif + random.randint(0, noise) - noise / 2	
			time_count = unit_count /50
			unit_count += 1
			self.v_Lif.append(vValue) 	
			##self.rate_Lif.append(Lrate)
			#self.time_Lif.append(time_count)
			#self.rate_Lif.append(Lrate)
			if vValue >= threshold and is_firing == False:	
				is_firing = True
				spike_count += 1
				vValue = reset
				fireRateValue = spike_count / time_count
				self.firingList_Lif.append(fireRateValue)
				#self.v_Lif.append(vValue)
			if vValue < threshold and is_firing == True:
				is_firing = False
				#self.v_Lif.append(vValue)
				
			##Lrate = spike_count
			self.v_Lif.append(vValue)
			"""
			if Lrate >= 1:
				self.rate_Lif.append(None)
			else:
				self.rate_Lif.append(Lrate)
			"""	
			#if time_count >= 3000:
			#	break
			

	def time(self):
		return self.time_Lif

	def rate(self):
		return self.rate_Lif

	def v(self):
		return self.v_Lif
	
	def firing_status(self):
		return self.firingList_Lif
