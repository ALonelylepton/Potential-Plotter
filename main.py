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
#initial conditions (0 is chi, 1 is phi)
pos=np.array([2.,3.])
vel=np.array([0.01,0.01])
#trajectory records
pos_save=np.zeros((tot,2))  #chi position record
pos_save[0] =pos
pot_save=np.zeros((tot,1))  #potential record
pot_save[0]=func.potentialShape(pos)
#calculate initial acceleration (0 is chi, 1 is phi)
acc=func.getAcc(pos,vel, dt)
#%%
#set up figure
fig=plt.figure(dpi=80)
grid=plt.GridSpec(3,1,wspace=0.0,hspace=0.03)
ax=plt.subplot(grid[:,0], projection='3d')
for i in range(tot):
    '''update fields'''
    #kick
    vel+=acc*dt/2
    #update
    pos+=vel*dt
    pos_save[i]=pos
    pot_save[i]=func.potentialShape(pos)
    #get acc
    acc=func.getAcc(pos, vel, dt)
    #kick
    vel+=acc*dt/2
    
    #run plot updater
    if plotRealTime or (i==tot-1):
        plt.sca(ax)
        plt.cla()
        x=pos_save[i][0]
        y = pos_save[i][1]
        z=pot_save[i]
        print(z)
        ax.scatter(x,y,z)
        ax.set(xlim=(-5,5), ylim=(-5,5), zlim=(0, 50))
        
        #print maxima
    conditions=np.array([pot_save[i-1]>pot_save[i-2], pot_save[i-1]>pot_save[i], pot_save[i-1]>3])
    if conditions.all():
        print(pot_save[i], pot_save[i-1],pot_save[i+1])
        print('-----------------------------------------------------')
    plt.pause(0.1)
    
    
    #print(chi_vel)
    

# %%
