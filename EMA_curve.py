class EMA:

	def __init__(self, currentList_EMA):
		self.currentList_EMA = currentList_EMA
	def claculate(self):
		current_EMA = 0.5
		old_current_EMA = 0
		alpha = 0.3
		time_count = 0
		unit_count = 1
		time_ca = 0

		while time_ca <= 2:
			new_current_EMA = (current_EMA*alpha) + (old_current_EMA * (1 - alpha))
			self.currentList_EMA.append(round(new_current_EMA,5))
			old_current_EMA = new_current_EMA
			unit_count += 1
			time_ca = unit_count / 30 	

	

	def current(self):
		return self.current_EMA

	def currentlist(self):
		return self.currentList_EMA





