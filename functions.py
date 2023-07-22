import numpy as np


def potentialShape(chi):
    chi_zero=1
    potential=(chi**2-chi_zero**2)**2
    return(potential)

def localPotential(chi_pos, chi_vel, phi_pos, phi_vel, dt):
    chi_zero=1
    local_chi=np.array([chi_pos-dt/2,chi_pos,chi_pos+dt/2])
    local_phi=np.array([phi_pos-dt/2,phi_pos,phi_pos+dt/2])
    
    chi_mesh, phi_mesh = np.meshgrid(local_chi, local_phi)
    
    potential=(chi_mesh**2-chi_zero**2)**2 + phi_mesh**2 +phi_mesh**2*chi_mesh**2
    return(potential)

def getAcc(chi_pos, chi_vel, phi_pos, phi_vel, dt):
    #get local potential shape
    potential=localPotential(chi_pos, chi_vel, phi_pos, phi_vel, dt)
    #get hubble parameter
    H=np.sqrt((potential+chi_vel**2/2)/3)
    #get acceleration
    acc=np.gradient(potential)
    phi_acc=acc[0][1][1]*-1
    chi_acc=acc[1][1][1]*-1
    '''
    need to add -3*H*vel
    '''
    
    return(chi_acc, phi_acc)