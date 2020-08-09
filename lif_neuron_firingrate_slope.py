import random
class Lif_neuron:

	def __init__(self, time_Lif, rate_Lif, v_Lif):
		self.time_Lif = time_Lif
		self.rate_Lif = rate_Lif
		self.v_Lif = v_Lif	  		
	def claculate(self):
		g = 0.09
		rest = 30
		threshold = 50
		reset = 30
		noise = 8
		current_Lif = 50
		time_count = 0
		spike_count = 0
		Lrate = 0
		vValue = rest
		firing = False
		while Lrate <= 200:
			vValue = -g * (vValue - rest) + current_Lif + random.randint(0, noise) - noise / 2 
			#self.v_Lif.append(vValue)
			#self.time_Lif.append(time_count)
			#self.rate_Lif.append(Lrate)
			if vValue >= threshold:
				firing = True
				spike_count += 1
				vValue = reset
				self.v_Lif.append(vValue)
			else:
				firing = False
				self.v_Lif.append(vValue)
			time_count += 1
			Lrate = spike_count
			self.time_Lif.append(time_count)
			self.rate_Lif.append(Lrate)
			#if len(self.rate_Lif) > 300:
				#break	
	def time(self):
		return self.time_Lif

	def rate(self):
		return self.rate_Lif

	def v(self):
		return self.v_Lif
	
