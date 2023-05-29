#Seminar
#Tema 4
# Tekst zadataka: Razvijte vlastiti modul koji ce korisniku omoguciti numericko racunanje polozaja, brzine i akceleracije za
#jednodimenzionalno gibanje. Neka modul radi za bilo koju silu koju korisnik moze definirati kao proizvoljnu
#funkciju brzine, polozaja i vremena (F = f(v, x, t)). Testirajte modul u slucajevima konstante sile (F =
#const) i harmonickog oscilatora (F = −kx).
import numpy as np
import matplotlib.pyplot as plt

class Num_racunanje:
    def __init__(self, x, v, m, dt,t):
        self.m = m
        self.dt = dt
        self.t=t
        self.x=[x]
        self.v=[v]
        self.a=[f(self.x[-1],self.v[-1],self.t)/ self.m]
        self.vr=[0]



    def VratInfo(self):
        print('x={}'.format(self.x))
        print('v={}'.format(self.v))
        print('a={}'.format(self.a))


    def Euler(self, f):
        
        for i in np.arange(0,self.t,self.dt):
            self.a.append(f(self.x[-1],self.v[-1],self.t)/ self.m)
            self.v.append(self.v[-1] + self.a[-1] * self.dt)
            self.x.append(self.x[-1] + self.v[-1] * self.dt)
            self.vr.append(self.t+self.dt)


    def Graf(self):
        Num_racunanje.Euler(self,f)
        fig, ax = plt.subplots(nrows=3, ncols=1)

        ax[0].plot(self.vr, self.x)
        ax[0].set_title('x-t graf')
        ax[0].set_xlabel('t [s]')
        ax[0].set_ylabel('x [m]')

        ax[1].plot(self.vr, self.v)
        ax[1].set_title('v-t graf')
        ax[1].set_xlabel('t [s]')
        ax[1].set_ylabel('v [m/s]')

        ax[2].plot(self.vr, self.a)
        ax[2].set_title('a-t graf')
        ax[2].set_xlabel('t [s]')
        ax[2].set_ylabel('a [m/s^2]')
        
        plt.show()
    


def f(v, x, t):
    return 5

u=Num_racunanje(2,3,4,0.01,20)
u.Graf()
