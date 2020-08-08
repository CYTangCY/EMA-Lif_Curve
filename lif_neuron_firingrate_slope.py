import random
class Lif_neuron:

	def __init__(self, time_Lif, rate_Lif):
		self.time_Lif = time_Lif
		self.rate_Lif = rate_Lif
			  		
	def claculate(self):
		g = 2
		rest = 50
		threshold = 30
		reset = 10
		noise = 8
		current_Lif = 50
		time_count = 0
		v = rest
		spike_count = 0
		Lrate = 0
		while Lrate <= 200:
			v = -g * (v - rest) + current_Lif + random.randint(0, noise) - noise / 2 
		
			if v > threshold:
				spike_count += 1
				v = reset
			time_count += 1
			Lrate += spike_count / time_count
			self.time_Lif.append(time_count)
			self.rate_Lif.append(Lrate)
			if len(self.rate_Lif) > 300:
				break	
	def time(self):
		return self.time_Lif

	def rate(self):
		return self.rate_Lif
	
