from numpy import *
import matplotlib.pyplot as p
import datetime

#filename = eval(raw_input('star('star#.txt'): ))
filename = 'acedata.txt'

def read_data():							# Function, gathering data from the 
	file = open(filename,'r')				# files and returning them as arrays, for computing
	Bz= [];
	for line in file:						# For-loop: Go through every line, one by one
		data = line.split()					# Split line in columns and store in array
		Bz.append(float(data[4]))			# Store the values in lists			
	file.close()
	Bz = array(Bz)						    # Lists are converted to arrays
	return Bz
B = read_data()

n = len(B)
time = zeros(n)
print n

for i in range(n):
    time[i] = 18. + (i*16.)/3600. 


p.plot(time,B)
p.ylabel('Mangetic Field Strength z-direction GSM [nT]')
p.xlabel('Time [Hours]')
p.grid(True)
p.show()




"""
################################################


p.plot(e, log(T))
p.show()

################################################
mi = 1.67*10**-27
kb =1.38*10**-23
const =(1.38/1.67)*10**4
cs = zeros(n)
gamma = 5/3.

for i in range(n):
    cs[i] = sqrt(gamma*const*T[i])/(10**3)


br = probe_data[11]
brr = br*distance**(3/2)
p.plot(distance,brr, 'ro')
p.show()

"""




















