import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

fig = plt.figure(figsize = (20, 10))
plt.title('moving_average')
plt.xlabel('time')
plt.ylabel('firing_rate')

current = 200
alpha = 0.95
time = [0,0]
firing_rate = [0,0]
new_firing_rate = 0
old_firing_rate = firing_rate[-1]

while new_firing_rate <= 199.99:
	new_firing_rate = (current*alpha)+(old_firing_rate*(1-alpha))
	firing_rate.append(new_firing_rate)
	old_firing_rate = firing_rate[-1]
	time.append(time[-1]+1)
##############################################################################
alpha_2 = 0.9
time_2 = [0,0]
firing_rate_2 = [0,0]
new_firing_rate_2 = 0
old_firing_rate_2 = firing_rate_2[-1]

while new_firing_rate_2 <= 199.99:
	new_firing_rate_2 = (current*alpha_2)+(old_firing_rate_2*(1-alpha_2))
	firing_rate_2.append(new_firing_rate_2)
	old_firing_rate_2 = firing_rate_2[-1]
	time_2.append(time_2[-1]+1)
##############################################################################	
alpha_3 = 0.85
time_3 = [0,0]
firing_rate_3 = [0,0]
new_firing_rate_3 = 0
old_firing_rate_3 = firing_rate_3[-1]

while new_firing_rate_3 <= 199.99:
	new_firing_rate_3 = (current*alpha_3)+(old_firing_rate_3*(1-alpha_3))
	firing_rate_3.append(new_firing_rate_3)
	old_firing_rate_3 = firing_rate_3[-1]
	time_3.append(time_3[-1]+1)
##############################################################################
alpha_4 = 0.8
time_4 = [0,0]
firing_rate_4 = [0,0]
new_firing_rate_4 = 0
old_firing_rate_4 = firing_rate_4[-1]

while new_firing_rate_4 <= 199.99:
	new_firing_rate_4 = (current*alpha_4)+(old_firing_rate_4*(1-alpha_4))
	firing_rate_4.append(new_firing_rate_4)
	old_firing_rate_4 = firing_rate_4[-1]
	time_4.append(time_4[-1]+1)
##############################################################################
alpha_5 = 0.75
time_5 = [0,0]
firing_rate_5 = [0,0]
new_firing_rate_5 = 0
old_firing_rate_5 = firing_rate_5[-1]

while new_firing_rate_5 <= 199.99:
	new_firing_rate_5 = (current*alpha_5)+(old_firing_rate_5*(1-alpha_5))
	firing_rate_5.append(new_firing_rate_5)
	old_firing_rate_5 = firing_rate_5[-1]
	time_5.append(time_5[-1]+1)
##############################################################################
alpha_6 = 0.7
time_6 = [0,0]
firing_rate_6 = [0,0]
new_firing_rate_6 = 0
old_firing_rate_6 = firing_rate_6[-1]

while new_firing_rate_6 <= 199.99:
	new_firing_rate_6 = (current*alpha_6)+(old_firing_rate_6*(1-alpha_6))
	firing_rate_6.append(new_firing_rate_6)
	old_firing_rate_6 = firing_rate_6[-1]
	time_6.append(time_6[-1]+1)
##############################################################################
alpha_7 = 0.65
time_7 = [0,0]
firing_rate_7 = [0,0]
new_firing_rate_7 = 0
old_firing_rate_7 = firing_rate_7[-1]

while new_firing_rate_7 <= 199.99:
	new_firing_rate_7 = (current*alpha_7)+(old_firing_rate_7*(1-alpha_7))
	firing_rate_7.append(new_firing_rate_7)
	old_firing_rate_7 = firing_rate_7[-1]
	time_7.append(time_7[-1]+1)
##############################################################################
alpha_8 = 0.6
time_8 = [0,0]
firing_rate_8 = [0,0]
new_firing_rate_8 = 0
old_firing_rate_8 = firing_rate_8[-1]

while new_firing_rate_8 <= 199.99:
	new_firing_rate_8 = (current*alpha_8)+(old_firing_rate_8*(1-alpha_8))
	firing_rate_8.append(new_firing_rate_8)
	old_firing_rate_8 = firing_rate_8[-1]
	time_8.append(time_8[-1]+1)
##############################################################################
alpha_9 = 0.55
time_9 = [0,0]
firing_rate_9 = [0,0]
new_firing_rate_9 = 0
old_firing_rate_9 = firing_rate_9[-1]

while new_firing_rate_9 <= 199.99:
	new_firing_rate_9 = (current*alpha_9)+(old_firing_rate_9*(1-alpha_9))
	firing_rate_9.append(new_firing_rate_9)
	old_firing_rate_9 = firing_rate_9[-1]
	time_9.append(time_9[-1]+1)
##############################################################################
alpha_10 = 0.5
time_10 = [0,0]
firing_rate_10 = [0,0]
new_firing_rate_10 = 0
old_firing_rate_10 = firing_rate_10[-1]

while new_firing_rate_10 <= 199.99:
	new_firing_rate_10 = (current*alpha_10)+(old_firing_rate_10*(1-alpha_10))
	firing_rate_10.append(new_firing_rate_10)
	old_firing_rate_10 = firing_rate_10[-1]
	time_10.append(time_10[-1]+1)
##############################################################################
alpha_11 = 0.45
time_11 = [0,0]
firing_rate_11 = [0,0]
new_firing_rate_11 = 0
old_firing_rate_11 = firing_rate_11[-1]

while new_firing_rate_11 <= 199.99:
	new_firing_rate_11 = (current*alpha_11)+(old_firing_rate_11*(1-alpha_11))
	firing_rate_11.append(new_firing_rate_11)
	old_firing_rate_11 = firing_rate_11[-1]
	time_11.append(time_11[-1]+1)
##############################################################################
alpha_12 = 0.4
time_12 = [0,0]
firing_rate_12 = [0,0]
new_firing_rate_12 = 0
old_firing_rate_12 = firing_rate_12[-1]

while new_firing_rate_12 <= 199.99:
	new_firing_rate_12 = (current*alpha_12)+(old_firing_rate_12*(1-alpha_12))
	firing_rate_12.append(new_firing_rate_12)
	old_firing_rate_12 = firing_rate_12[-1]
	time_12.append(time_12[-1]+1)
##############################################################################
alpha_13 = 0.35
time_13 = [0,0]
firing_rate_13 = [0,0]
new_firing_rate_13 = 0
old_firing_rate_13 = firing_rate_13[-1]

while new_firing_rate_13 <= 199.99:
	new_firing_rate_13 = (current*alpha_13)+(old_firing_rate_13*(1-alpha_13))
	firing_rate_13.append(new_firing_rate_13)
	old_firing_rate_13 = firing_rate_13[-1]
	time_13.append(time_13[-1]+1)
##############################################################################
alpha_14 = 0.3
time_14 = [0,0]
firing_rate_14 = [0,0]
new_firing_rate_14 = 0
old_firing_rate_14 = firing_rate_14[-1]

while new_firing_rate_14 <= 199.99:
	new_firing_rate_14 = (current*alpha_14)+(old_firing_rate_14*(1-alpha_14))
	firing_rate_14.append(new_firing_rate_14)
	old_firing_rate_14 = firing_rate_14[-1]
	time_14.append(time_14[-1]+1)
##############################################################################
alpha_15 = 0.25
time_15 = [0,0]
firing_rate_15 = [0,0]
new_firing_rate_15 = 0
old_firing_rate_15 = firing_rate_15[-1]

while new_firing_rate_15 <= 199.99:
	new_firing_rate_15 = (current*alpha_15)+(old_firing_rate_15*(1-alpha_15))
	firing_rate_15.append(new_firing_rate_15)
	old_firing_rate_15 = firing_rate_15[-1]
	time_15.append(time_15[-1]+1)
##############################################################################
alpha_16 = 0.2
time_16 = [0,0]
firing_rate_16 = [0,0]
new_firing_rate_16 = 0
old_firing_rate_16 = firing_rate_16[-1]

while new_firing_rate_16 <= 199.99:
	new_firing_rate_16 = (current*alpha_16)+(old_firing_rate_16*(1-alpha_16))
	firing_rate_16.append(new_firing_rate_16)
	old_firing_rate_16 = firing_rate_16[-1]
	time_16.append(time_16[-1]+1)
##############################################################################
alpha_17 = 0.15
time_17 = [0,0]
firing_rate_17 = [0,0]
new_firing_rate_17 = 0
old_firing_rate_17 = firing_rate_17[-1]

while new_firing_rate_17 <= 199.99:
	new_firing_rate_17 = (current*alpha_17)+(old_firing_rate_17*(1-alpha_17))
	firing_rate_17.append(new_firing_rate_17)
	old_firing_rate_17 = firing_rate_17[-1]
	time_17.append(time_17[-1]+1)
##############################################################################
alpha_18 = 0.1
time_18 = [0,0]
firing_rate_18 = [0,0]
new_firing_rate_18 = 0
old_firing_rate_18 = firing_rate_18[-1]

while new_firing_rate_18 <= 199.99:
	new_firing_rate_18 = (current*alpha_18)+(old_firing_rate_18*(1-alpha_18))
	firing_rate_18.append(new_firing_rate_18)
	old_firing_rate_18 = firing_rate_18[-1]
	time_18.append(time_18[-1]+1)
##############################################################################
alpha_19 = 0.05
time_19 = [0,0]
firing_rate_19 = [0,0]
new_firing_rate_19 = 0
old_firing_rate_19 = firing_rate_19[-1]

while new_firing_rate_19 <= 199.99:
	new_firing_rate_19 = (current*alpha_19)+(old_firing_rate_19*(1-alpha_19))
	firing_rate_19.append(new_firing_rate_19)
	old_firing_rate_19 = firing_rate_19[-1]
	time_19.append(time_19[-1]+1)
##############################################################################


plt.plot(time, firing_rate,'--', label = 'alpha= 0.95')
plt.plot(time_2, firing_rate_2,'--', label = 'alpha= 0.9')
plt.plot(time_3, firing_rate_3,'--', label = 'alpha= 0.85')
plt.plot(time_4, firing_rate_4,'--', label = 'alpha= 0.8')
plt.plot(time_5, firing_rate_5,'--', label = 'alpha= 0.75')
plt.plot(time_6, firing_rate_6,'--', label = 'alpha= 0.7')
plt.plot(time_7, firing_rate_7,'--', label = 'alpha= 0.65')
plt.plot(time_8, firing_rate_8,'--', label = 'alpha= 0.6')
plt.plot(time_9, firing_rate_9,'--', label = 'alpha= 0.55')
plt.plot(time_10, firing_rate_10,'--', label = 'alpha= 0.5')
plt.plot(time_11, firing_rate_11,'--', label = 'alpha= 0.45')
plt.plot(time_12, firing_rate_12,'--', label = 'alpha= 0.4')
plt.plot(time_13, firing_rate_13,'--', label = 'alpha= 0.35')
plt.plot(time_14, firing_rate_14,'--', label = 'alpha= 0.3')
plt.plot(time_15, firing_rate_15,'--', label = 'alpha= 0.25')
plt.plot(time_16, firing_rate_16,'--', label = 'alpha= 0.2')
plt.plot(time_17, firing_rate_17,'--', label = 'alpha= 0.15')
plt.plot(time_18, firing_rate_18,'--', label = 'alpha= 0.1')
plt.plot(time_19, firing_rate_19,'--', label = 'alpha= 0.05')
plt.grid(True)
plt.legend()
plt.show()
fig.savefig('EMA.png')
