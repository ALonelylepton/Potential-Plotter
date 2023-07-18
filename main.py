#%%
import matplotlib.pyplot as plt
import numpy as np

def potentialShape(chi):
    chi_zero=1
    potential=(chi**2-chi_zero**2)**2
    return(potential)

def localPotential(pos):
    chi_zero=1
    positive=np.arange(pos, pos+0.1, 0.01)
    negative = np.arange(pos-0.1, pos, 0.01)
    local=np.append(np.flip(negative),positive)
    
    potential=(local**2-chi_zero**2)**2
    return(potential)

def getAcc(position):
    #get local potential shape
    potential=localPotential(position)

    acc=-np.gradient(potential)
    acc_local=acc[int(len(acc)/2)]
    return(acc_local)

#parameters
Nt=10    #ammount of time
dt= 0.05    #time step
plotRealTime=True
#total simulation length
tot=int(Nt/dt)
#initial conditions
chi_pos=2
chi_vel=0
#trajectory records
pos_save=np.zeros((tot,1))  #chi position record
pos_save[0]=chi_pos
pot_save=np.zeros((tot,1))  #potential record
pot_save[0]=potentialShape(chi_pos)
#calculate initial acceleration
chi_acc=getAcc(chi_pos)

#set up figure
fig=plt.figure(dpi=80)
grid=plt.GridSpec(3,1,wspace=0.0,hspace=0.03)
ax=plt.subplot(grid[:,0])
for i in range(tot):
    #kick
    chi_vel+=chi_acc*dt/2
    #update
    chi_pos+=chi_vel*dt
    pos_save[i]=chi_pos
    pot_save[i]=potentialShape(chi_pos)
    
    #get acc
    chi_acc=getAcc(chi_pos)
    #kick
    chi_vel+=chi_acc*dt/2
    #run plot updater
    if plotRealTime or (i==tot-1):
        plt.sca(ax)
        plt.cla()
        x=pos_save[i]
        y=pot_save[i]
        plt.scatter(x,y)
        ax.set(xlim=(-5,5), ylim=(0,10))
        ax.set_aspect('equal','box')
        plt.pause(0.001)

print(pot_save)
# %%
