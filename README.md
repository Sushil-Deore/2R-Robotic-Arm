# 2R-Robotic-Arm

To create a simulation of forward Kinematic motion of 2R robotic arm using python 3 

Aim: To create a simulation of forward Kinematic motion of 2R robotic arm using python 3 

Description:
1.	Kinematics: A Branch of mechanics that describe the motion of bodies without considering forces.
2.	Forward kinematics: The Forward kinematics of a robot is the position and orientation of manipulator from its joint values.
 
`θ1`: Angle made by link 1 with the base of the Robot
`θ2`: Angle made by link 2 with respect to X-Axis
 'L1' : Length of link 1 
 'L2' : Length of link 2

 Procedure: 
•	Position of link 1 considering the starting point is fixed to the origin with coordinates (x1=0, y1=0) 

endpoints of link 1: 
x1 = L1 * cos (θ1) 
y1 = L1 * sin (θ1)
•	Position of link 2 considering endpoints of link 1 as starting points of link 2 (x1, y1)

endpoints of link 2:
x2 = x1 + L2 * cos (θ2)
y2 = y1 + L2 * sin (θ2)

•	For different values 'θ1' and 'θ2', the different simulations will be plotted. 
By saving simulation frames for different values of 'θ1' and 'θ2'. 
Stitching will be done on frames byusing ImageMagick, simulation for 2R Robotic Arm will be created. 
