## Kalman filter for problem set 1 of ABE 598
# Author: Girish Chowdhary
# Updated 03-10-2019 - Translated from matlab to python - Justin Wasserman
# I can not guarantee python2 compatibility, but you should be using python3 anyways.

#this file is intended to be a simple demonstration of a Kalman Filter for a linear system

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm
from numpy.random import randn

## parameters of the linear system: x_dot=Ax+Bu; y= Cx
# Students: Try different linear systems, try higher dimensional linear systems

A=np.matrix('-1 -5;6,-1')
B=np.matrix('1;0')
x=np.matrix('1,0').T #initial value of the state vector
u=0 #initial input
C=np.matrix('0 1')
y=C*x

##integration parameters
dt=0.01
tf=int(10/dt)
t=0

#This is a discrete implementation, so the following line makes the system discrete
# by taking the matrix exponential: Ad=expm(A*dt)
# so now our system becomes: x(k+1)=Ad*x_k+ Bd*u_k
Ad=expm(A*dt)


#noise parameters (you can change these and see how it affects the filter)
w=0.01#process noise covariance
v=0.1#measurement noise covariance
x_tilde=np.matrix('0;0') #This is where we initialize the state estimate, note how it is different from
               #the actual initial state (x=[1,0]), you can see how changing this affects the filter
x_hat=x_tilde #just setting the inital values

Q=np.eye(2)*w #Q matrix captures the process noise covariance
R=np.eye(1)*v # R matrix captuers the measurement noise covariance

P=np.eye(2)*1 # initial state error covariance matrix (P)

# storage variables
X_HAT_STORE= np.zeros((2,tf))
X_STORE= np.zeros((2,tf))
Y_REC = np.zeros((tf,1))
T_REC = np.zeros((tf,1))

y = np.zeros((tf+1))
## main loop
for k in range(tf):
    ## system intergration
    u=np.sin(0.01*k)*0.1 #The input to the system can be changed here
    x=Ad*x+B*u+randn(2,1)*w #note the discrete propagation, and the addition of process noise
    y[k+1]=C*x+randn(1,1)*v #the measurement noise adds here

    t=t+dt
    ## Add your code here

    ## store
    X_HAT_STORE[:,k]= np.zeros((2,))
    X_STORE[:,k]=x.flatten()
    Y_REC[k]=y[k]
    T_REC[k]= t


## plotting

plt.figure(1)
plt.subplot(211)
plt.plot(T_REC,X_STORE[0,:], label = 'real')
plt.plot(T_REC,X_HAT_STORE[0,:],label = 'estimated')
plt.subplot(212)
plt.plot(T_REC,X_STORE[1,:],label='real')
plt.plot(T_REC,X_HAT_STORE[1,:],label='estimated')

plt.legend()
plt.title('state estimate')

plt.figure(2)
plt.plot(T_REC,Y_REC,label='real')
plt.plot(T_REC,X_HAT_STORE[1,:],label='estimated')
plt.legend()
plt.title('output')

plt.show()