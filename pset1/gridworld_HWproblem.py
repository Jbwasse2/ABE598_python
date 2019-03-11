# Updated 03-10-2019 - Translated from matlab to python - Justin Wasserman
import matplotlib.pyplot as plt
import numpy as np
from gridworld_trans_HW import gridworld_trans_HW

#Gridworld Simulation with GPs for Q learning
#Gridworld Parameters
N_grid = 5 # Number of grids on one direction
N_state = N_grid*N_grid # Square Gridworld
N_act = 5 # 4 directions + null action

n_state_dim=2
s_init = np.matrix('1;1') # Start in the top left corner
a_init=2
s_goal = np.matrix(str(N_grid)+';'+str(N_grid)) # Goal is at the upper right corner [end,end]
N_eps_length =100 # Length of an episode
#storage variables
STATE_STORE = np.zeros((N_eps_length,2))


#Algorithm Execution
s_old = s_init
for k in range(N_eps_length):
    ## This is the main part of the code
    # As the code stands, it computes the next state given an
    # action for N_eps_length iterations,
    # there are 5 actions, they are described in
    # gridworld_trans_HW
    # the purpose of this code is to show you how to use the
    # gridworld_trans_HW function and plot the results
    # in the current code the action has been fixed
    # your job is to write a search algorithm that gets you from
    # s_init to s_goal

    # Next State computation
    action = 2

    s_new = gridworld_trans_HW(s_old,action,N_grid)

    s_old=s_new

    ## storage
    STATE_STORE[k,:]=s_new.T

#Plots
plt.figure(1)
plt.plot(STATE_STORE[:,0],STATE_STORE[:,1],'o')
plt.xlabel('x state')
plt.ylabel('y state')
plt.show()
