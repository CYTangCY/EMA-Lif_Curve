class EMA:

	def __init__(self, time_EMA, rate_EMA):
		self.time_EMA = time_EMA
		self.rate_EMA = rate_EMA

	def claculate(self):
		current_EMA = 0.5
		alpha = 0.5
		new_firing_rate = 0
		old_firing_rate = 0
		time_count = 0
		unit_count = 0
		time_ca = 0
		

		while time_ca <= 1:
			new_firing_rate = (current_EMA*alpha) + (old_firing_rate * (1 - alpha))
			self.rate_EMA.append(new_firing_rate)
			old_firing_rate = self.rate_EMA[-1]
			unit_count += 1
			time_ca = unit_count / 30 	
			self.time_EMA.append(time_ca)
			print(time_ca)
	def time(self):
		return self.time_EMA

	def rate(self):
		return self.rate_EMA





