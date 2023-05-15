import numpy as np
import matplotlib.pyplot as plt
class Suncev_sustav:
    def __init__(self,au,v1,r1,v2,r2,t_kraj,dt):
        self.au=au*1.486*10**11#m
        self.Mz=5.9742*10**24#kg
        self.Ms=1.989*10**30#kg
        self.G=6.67408*10**(-11)#Nm^2/kg^2
        self.v1=[v1]
        self.r1=[r1]
        self.v2=[v2]
        self.r2=[r2]
        self.t_kraj=t_kraj
        self.dt=dt
        self.a1=[]
        self.a2=[]
    
    def VratInfo(self):
        print('a1={}'.format(self.a1))
        print('a2={}'.format(self.a2))
        print('r1={}'.format(self.r1))
        print('r2={}'.format(self.r2))
        print('v1={}'.format(self.v1))
        print('v2={}'.format(self.v2))
        print('au={}'.format(self.au))
        print('dt={}'.format(self.dt))

    def Izracun(self):
        for i in np.arange(0,self.t_kraj,self.dt):
            self.a1.append(-self.G*self.Mz*self.r1[-1]-self.r2[-1]/abs(self.r1[-1]-self.r2[-1])**3)
            self.v1.append(self.v1[-1]+self.a1[-1]*self.dt)
            self.r1.append(self.r1[-1]+self.v1[-1]*self.dt)
            self.a2.append(-self.G*self.Ms*self.r2[-1]-self.r1[-1]/abs(self.r2[-1]-self.r1[-1])**3)
            self.v2.append(self.v2[-1]+self.a2[-1]*self.dt)
            self.r2.append(self.r2[-1]+self.v2[-1]*self.dt)
    
    def Graf(self):
        Suncev_sustav.Izracun(self)
        plt.plot(self.r1,self.v1)
        plt.show()


n=Suncev_sustav(au=1,v1=np.array((0,0)),r1=np.array((0,0)),v2=np.array((107000,0)),r2=np.array((1.486*10**11,0)),t_kraj=365,dt=15)
n.Izracun()
n.Graf()