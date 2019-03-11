# Updated 03-10-2019 - Translated from matlab to python - Justin Wasserman
import numpy as np
def gridworld_trans_HW(s_old,action,N_grid):
    # function s_new = gridworld_trans(s_old,action,params)
    # returns the next state in s_new given
    # old state in s_old and action in action, actions take on 5 values:
    # 1: null action, stay where you are
    # 2: go right
    # 3: go up
    # 4: go right
    # 5: go down
    # parameter N_grid contains the number of grids in the grid world
    #always step in the action intended
    dir = action
     # Get The Next State
    s_new = np.zeros((2,1))
    if(dir == 1):
        s_new[0] = s_old[0]
        s_new[1] = s_old[1]
    elif(dir == 2):
        s_new[0] = s_old[0] + 1
        s_new[1] = s_old[1]
    elif(dir == 3):
        s_new[0] = s_old[0]
        s_new[1] = s_old[1] + 1
    elif(dir == 4):
        s_new[0] = s_old[0] - 1
        s_new[1] = s_old[1]
    elif(dir == 5):
        s_new[0] = s_old[0]
        s_new[1] = s_old[1] - 1
    else:
        assert "[gridworld_trans_HW] invalid action given"
 # Saturate the states if on boundaries
    s_new[0] = max([1,min([N_grid,s_new[0]])])
    s_new[1] = max([1,min([N_grid,s_new[1]])])
    return s_new
