<<<<<<< HEAD
#harmonic_oscillator
#Zdk 1.
=======
#Vjezba 6
#Zdk1
>>>>>>> 254fd02b2d0495ed7d27ea9b8496cb00216a04b8
import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:
<<<<<<< HEAD
    def __init__(self, x, v, k, dt, m):
        self.m = m
        self.k = k
        self.t = [0] # početno vrijeme
        self.x = [x] # početni položaj
        self.v = [v] # početna brzina
        self.a = [-self.k * self.x[-1] / self.m]
        self.dt=dt

    def Izracun(self,t):
        while self.t[-1] < t:
            self.a.append(-self.k / self.m * self.x[-1])
            self.v.append(self.v[-1] + self.a[-1] * self.dt)
            self.x.append(self.x[-1] + self.v[-1] * self.dt)
            self.t.append(self.t[-1] + self.dt)

=======
    def __init__(self, x0, v0, omega, t_end, dt, m):
        self.t = []
        self.x = []
        self.v = []
        self.a = []
        self.m = m
        self.x.append(x0)
        self.v.append(v0)
        self.omega = omega
        self.k = m * omega ** 2
        self.T = 2 * np.pi / self.omega

        
        for i in np.arange(0, t_end, dt):
            self.t.append(i)
            self.a.append(-self.k / self.m * self.x[-1])
            self.v.append(self.v[-1] + self.a[-1] * dt)
            self.x.append(self.x[-1] + self.v[-1] * dt)
>>>>>>> 254fd02b2d0495ed7d27ea9b8496cb00216a04b8

    def Informacije(self):
        print('vremenski intervali: {}'.format(self.t))
        print('polozaji: {}'.format(self.x))
        print('brzina: {}'.format(self.v))
        print('akceleracija: {}'.format(self.a))

<<<<<<< HEAD
    def plot_trajectory(self, t):
        HarmonicOscillator.Izracun(self, t)
        
        fig, ax = plt.subplots(nrows=3, ncols=1)

        ax[0].plot(self.t, self.x)
        ax[0].set_title('x-t graf')
        ax[0].set_xlabel('t [s]')
        ax[0].set_ylabel('x [m]')

        ax[1].plot(self.t, self.v)
        ax[1].set_title('v-t graf')
        ax[1].set_xlabel('t [s]')
        ax[1].set_ylabel('v [m/s]')

        ax[2].plot(self.t, self.a)
        ax[2].set_title('a-t graf')
        ax[2].set_xlabel('t [s]')
        ax[2].set_ylabel('a [m/s^2]')

    
=======

    def plot_xt(self):
        plt.plot(self.t, self.x[:-1])
        plt.xlabel('t')
        plt.ylabel('x')
        plt.title('x-t graf')
        plt.show()

    def plot_vt(self):
        plt.plot(self.t, self.v[:-1])
        plt.xlabel('t')
        plt.ylabel('v')
        plt.title('v-t graf')
        plt.show()

    def plot_at(self):
        plt.plot(self.t, self.a)
        plt.xlabel('t')
        plt.ylabel('a')
        plt.title('a-t graf')
        plt.show()

ho = HarmonicOscillator(x0=0.3, v0=0, omega=3, t_end=10, dt=0.01, m=2)
ho.plot_vt()
ho.plot_at()
ho.plot_xt()
print("Period oscilacije: ", ho.T)
>>>>>>> 254fd02b2d0495ed7d27ea9b8496cb00216a04b8
