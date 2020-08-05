import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

fig = plt.figure(figsize = (20, 10))
plt.title('moving_average')
plt.xlabel('time')
plt.ylabel('firing_rate')

current = 200
alpha = float(input("inpur alpha: "))
time = [0,0]
firing_rate = [0,0]
new_firing_rate = 0
old_firing_rate = firing_rate[-1]

while new_firing_rate <= 199.999:
	new_firing_rate = (current*alpha)+(old_firing_rate*(1-alpha))
	firing_rate.append(new_firing_rate)
	old_firing_rate = firing_rate[-1]
	time.append(time[-1]+1)

print(firing_rate)
plt.grid(True)
plt.plot(time, firing_rate,'ro-')
plt.show()
