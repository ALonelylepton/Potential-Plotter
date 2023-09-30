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
pos=2.
vel=-0.2
#trajectory records
pos_save=np.zeros(tot)  #chi position record
pos_save[0] =pos
pot_save=np.zeros(tot)  #potential record
pot_save[0]=func.potentialShape2d(pos)
#calculate initial acceleration (0 is chi, 1 is phi)
acc=func.getAcc2d(pos,vel, dt)
#%%
#set up figure
fig=plt.figure(dpi=80)
grid=plt.GridSpec(3,1,wspace=0.0,hspace=0.03)
ax=plt.subplot(grid[:,0])

c=10
a= np.linspace(-2, 2, 50)
b = (1-np.exp(-a*c))*np.heaviside(a+1, 1)
#ax.plot(a,b)

for i in range(tot):
    '''update fields'''
    #kick
    vel+=acc*dt/2
    #update
    pos+=vel*dt
    pos_save[i]=pos
    pot_save[i]=func.potentialShape2d(pos)
    #get acc
    acc=func.getAcc2d(pos, vel, dt)
    #kick
    vel+=acc*dt/2
    
    #run plot updater
    if plotRealTime or (i==tot-1):
        plt.sca(ax)
        plt.cla()
        x=pos_save[i]

        y=pot_save[i]
        print(x, y)
        ax.scatter(x,y)
        ax.set(xlim=(-5,5), ylim=(0,5))
        
    #print maxima
    conditions=True#np.array([pot_save[i-1]>pot_save[i-2], pot_save[i-1]>pot_save[i], pot_save[i-1]>3])
    if conditions:
        print(pot_save[i], pot_save[i-1],pot_save[i+1])
        print('-----------------------------------------------------')
    plt.pause(0.1)
    
    
    #print(chi_vel)



# %%
