import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


def height(x):
    '''sample height'''
    return 0.015 - 0.005*(L-x)

def width(x):
    '''sample width'''
    return 0.015

def area(x):
    '''calculated cross-sectional area'''
    return width(x) * height(x)

def area_moment(x):
    return (width(x) * height(x)**3)/12


# Model parameters

T = 1            # Thrust in N
rho = 1000        # Density in kg/m^3
L = 0.5           # Length in m
stress_y = 30e6   # Yield strength in Pa

N = 20                   # Number of segments to divide the slab for calculation
x = np.linspace(0,L,N)    # Generate N evenly-spaced data points from 0 to L
dx = x[1]                 # Spacing between each x-location

moment = np.zeros(N)            
stress = np.zeros(N)     
mass = 0                 

# Calculate moment and stress for each point and also sum up the mass
for i in range(N):
    moment[i] = T*(L - x[i])    
    stress[i] = - moment[i]*(height(x[i])/2)/area_moment(x[i])
    mass += rho*dx*area(x[i])


# largest bending stress along the length of the beam
stress_max = max(abs(stress)) 

print ("Mass = {:.3f} kg".format(mass))  
print ("Maximum stress = {:.2f}  MPa".format(stress_max/1e6))

# Check factor of safety
safety = stress_y/stress_max
print ("Factor of safety = {:.3f} ".format(safety))
if (safety < 2):
    print ('Your factor of safety is less than 2! Redesign and try again.')
else:
    print ('Good! Your factor of safety is greater or equal to 2.')

# Plot data
plt.figure(1)
plt.plot(x,moment)
plt.ylabel('moment (Nm)')
plt.xlabel('position x (m)')
plt.title('Moment along the beam')

plt.figure(2)
plt.plot(x,stress/1e6)
plt.ylabel('stress (MPa)')
plt.xlabel('position x (m)')
plt.title('Bending stress along the beam')
