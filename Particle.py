#Vjezba 4
#1. Zadatak
#Θ
#import numpy as np
#import matplotlib.pyplot as plt
class Particle:
    def __init__(self,v_0,Θ,y,x):
        self.v_0=v_0
        self.Θ=np.radians(Θ)
        self.x_0=[x]
        self.y_0=[y]
        self.vy=[v_0*np.sin(self.Θ)]
        self.vx=[v_0*np.cos(self.Θ)]
    
    def reset(self):
        self.v_0=[]
        self.Θ=[]
        self.x_0=[]
        self.y_0=[]

    def __move(self, dt):
        g=9.81
        self.vy.append(self.vy[-1]-g*dt)
        self.vx.append(self.vx[-1])
        self.x_0.append(self.x_0[-1]+self.vx[-1]*dt)
        self.y_0.append(self.y_0[-1]+self.vy[-1]*dt)
  
    def range(self, dt=0.001):
        while self.y_0[-1] >= 0:
            self.__move(dt)
        return print('Domet =',self.x_0[-1])
    
    def plot_trajectory():
       plt.plot(self.x_0, self.y_0)
       plt.show


p = Particle(v_0=10, Θ=45, y=0, x=0)
p.range()