class EMA:

	def __init__(self, time_EMA, rate_EMA):
		self.time_EMA = time_EMA
		self.rate_EMA = rate_EMA

	def claculate(self):
		current_EMA = 200
		alpha = 0.05
		new_firing_rate = 0
		old_firing_rate = self.rate_EMA[-1]
		time_count = 0
		time_ca = 0

		while new_firing_rate <= 199.9:
			new_firing_rate = (current_EMA*alpha) + (old_firing_rate * (1 - alpha))
			old_firing_rate = self.rate_EMA[-1]
			time_count +=1
			time_ca = time_count 
			self.rate_EMA.append(new_firing_rate)
			self.time_EMA.append(time_ca)

	def time(self):
		return self.time_EMA

	def rate(self):
		return self.rate_EMA



