import numpy as np


def potentialShape(pos):
    chi_zero=1
    potential=(pos[0]**2-chi_zero**2)**2+pos[1]**2 + pos[1]**2*pos[0]**2
    return(potential)

def localPotential(chi_pos, chi_vel, phi_pos, phi_vel, dt):
    chi_zero=1
    local_chi=np.array([chi_pos-dt/2,chi_pos,chi_pos+dt/2])
    local_phi=np.array([phi_pos-dt/2,phi_pos,phi_pos+dt/2])
    
    phi_mesh, chi_mesh = np.meshgrid(local_phi, local_chi)
    
    potential=(chi_mesh**2-chi_zero**2)**2 + phi_mesh**2 +phi_mesh**2*chi_mesh**2
    return(potential)

def getAcc(pos, vel, dt):
    #get local potential shape
    potential=localPotential(pos[0], vel[0], pos[1], vel[1], dt)
    #get hubble parameter
    H=np.sqrt((potential+vel[0]**2/2)/3)
    #get acceleration 0 is chi, 1 is phi
    acc=np.gradient(potential)
    acc[0]=acc[0]*-1
    acc[1]=acc[1]*-1
    acc_local=np.array([acc[0][1][1], acc[1][1][1]])
    '''
    need to add -3*H*vel
    '''
    return(acc_local)

def potentialShape2d(pos):
    c=10
    #potential = pos**2
    potential=(1-np.exp(-pos*c))*np.heaviside(pos+1, 1)
    return(potential)

def getAcc2d(pos, vel, dt):
    #get local potential shape
    potential=localPotential2d(pos, vel, dt)
    #get hubble parameter
    H=np.sqrt((potential+vel**2/2)/3)
    #get acceleration 0 is chi, 1 is phi
    acc_local=np.gradient(potential)*-1
    '''
    need to add -3*H*vel
    '''
    return(acc_local[1])

def localPotential2d(pos, vel, dt):
    c=10
    pos=np.array([pos-dt/2,pos,pos+dt/2])
    #potential = pos**2
    potential= (1-np.exp(-pos*c))*np.heaviside(pos+1, 1)
    return(potential)
