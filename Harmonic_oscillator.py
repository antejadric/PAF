#Vjezba 6
#Zdk1
import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:
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

    def Informacije(self):
        print('vremenski intervali: {}'.format(self.t))
        print('polozaji: {}'.format(self.x))
        print('brzina: {}'.format(self.v))
        print('akceleracija: {}'.format(self.a))


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