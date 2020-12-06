
# Importing the math and plotting functions 

import math 
import matplotlib.pyplot as plt 

# For number of iterations of theta 1 and theta2

n_theta = 10

# To calculate Initial values for theta1 & theta2 

theta_start = 0
theta_end = (math.pi)/2

# To store values for theta1 and theta2 

theta1 = []
theta2 = []


for i in range(0,n_theta):
	temp = theta_start + i*(theta_end- theta_start)/(n_theta - 1)
	theta1.append(temp)
	theta2.append(temp)

# inputs in meters :

l1 = 1
l2 = 0.5 

# Base of Robot: Considering the initial poisitions as (0,0) for (x0,y0)

x0 = 0
y0 = 0

# Counter variable for image name count

ct = 1

# For loop for managing the values for t1 and t2 from list theta1 and theta2

for t1 in theta1:
	for t2 in theta2:
		
# Co-ordinates  for Link 1, Link 2 connector

		x1= l1*math.cos(t1)
		y1= l1*math.sin(t1)
 
# Co-ordinates of the manipulator

		x2= x1 + l2*math.cos(t2)
		y2= y1 + l2*math.sin(t2)

# For Output images from counter with unique filename 
		
		filename = str(ct) + '.png'
		ct = ct + 1

# For Plotting the graph for Forward kinametics

		plt.figure()
		plt.plot([x0,x1],[y0,y1])
		plt.plot([x1,x2],[y1,y2])

# Limiting the Co-ordinates x & y
		
		plt.xlim([0,2])
		plt.ylim([0,2])

		plt.savefig(filename)






