import matplotlib.pyplot as plt
import numpy as np


def potentialShape(chi):
    chi_zero=1
    potential=(chi**2-chi_zero**2)**2
    return(potential)

def localPotential(pos, vel, dt):
    chi_zero=1
    local=np.array([pos-dt/3,pos,pos+dt/3])

    potential=(local**2-chi_zero**2)**2
    return(potential)

def getAcc(position, vel, dt):
    #get local potential shape
    potential=localPotential(position, vel, dt)
    #get hubble parameter
    H=np.sqrt((potential+vel**2/2)/3)
    #get acceleration
    acc=-np.gradient(potential)-3*H*vel
    acc_local=acc[1]
    
    return(acc_local)