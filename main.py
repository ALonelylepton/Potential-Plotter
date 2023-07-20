#%%
import matplotlib.pyplot as plt
import numpy as np
import functions as func

#parameters
Nt=100  #ammount of time
dt= 0.1    #time step
plotRealTime=True
#total simulation length
tot=int(Nt/dt)
#initial conditions
chi_pos=2
chi_vel=0.01
#trajectory records
pos_save=np.zeros((tot,1))  #chi position record
pos_save[0]=chi_pos
pot_save=np.zeros((tot,1))  #potential record
pot_save[0]=func.potentialShape(chi_pos)
#calculate initial acceleration
chi_acc=func.getAcc(chi_pos,chi_vel,dt)

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
    pot_save[i]=func.potentialShape(chi_pos)
    #get acc
    chi_acc=func.getAcc(chi_pos, chi_vel, dt)
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
        #print maxima
    conditions=np.array([pot_save[i-1]>pot_save[i-2], pot_save[i-1]>pot_save[i], pot_save[i-1]>3])
    if conditions.all():
        print(pot_save[i], pot_save[i-1],pot_save[i+1])
        print('-----------------------------------------------------')
    plt.pause(0.01)
    
    
    #print(chi_vel)
    

# %%
