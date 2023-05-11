import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Nabijene_cestice:
    def __init__(self, E, B, v, m, q, x, dt, t_kr):
        self.E = E
        self.B = B
        self.v = [v]
        self.x = [x]
        self.m = m
        self.q = q
        self.dt = dt
        self.t_kr = t_kr        
        self.a = []

    def PrintInfo(self):
        print('E={}'.format(self.E))
        print('B={}'.format(self.B))
        print('v={}'.format(self.v))
        print('q={}'.format(self.q))
        print('dt={}'.format(self.dt))
        print('a={}'.format(self.a))
        print('x={}'.format(self.x))

    def Euler(self):
        for i in np.arange(0, self.t_kr, self.dt):
            self.a = (self.q / self.m) * (self.E + np.cross(self.v[-1], self.B))
            self.v.append(self.v[-1] + self.a * self.dt)
            self.x.append(self.x[-1] + self.v[-1] * self.dt)

    def Runge_Kutta(self):
        tim = np.arange(0, self.t_kr, self.dt)
        for i in tim:
            kvx = [(-np.sign(self.v[-1][0]) * (self.q * self.B[2] / self.m) * self.v[-1][1]) * self.dt]
            kvy = [(np.sign(self.v[-1][0]) * (self.q * self.B[2] / self.m) * self.v[-1][0]) * self.dt]
            kvz = [0.0]
            kx = [self.v[-1][0] * self.dt]
            ky = [self.v[-1][1] * self.dt]
            kz = [self.v[-1][2] * self.dt]

            for j in range(len(tim) - 1):
                kvx.append((-np.sign(self.v[-1][0]) * (self.q * self.B[2] / self.m) * (self.v[-1][1] + kvy[-1])) * self.dt)
                kvy.append((np.sign(self.v[-1][0]) * (self.q * self.B[2] / self.m) * (self.v[-1][0] + kvx[-1])) * self.dt)
                kvz.append((np.sign(self.v[-1][0]) * (self.q * self.B[1] / self.m) * (self.v[-1][0] + kvx[-1]) - np.sign(self.v[-1][0]) * (self.q * self.B[0] / self.m) * (self.v[-1][1] + kvy[-1])) * self.dt)
                kx.append((self.v[-1][0] + kvx[-1]) * self.dt)
                ky.append((self.v[-1][1] + kvy[-1]) * self.dt)
                kz.append((self.v[-1][2] + kvz[-1]) * self.dt)

            self.v.append([self.v[-1][0] + (kvx[0] + 2 * kvx[1] + 2 * kvx[2] + kvx[3]) / 6,
                        self.v[-1][1] + (kvy[0] + 2 * kvy[1] + 2 * kvy[2] + kvy[3]) / 6,
                        self.v[-1][2] + (kvz[0] + 2 * kvz[1] + 2 * kvz[2] + kvz[3]) / 6])
            self.x.append([self.x[-1][0] + (kx[0] + 2 * kx[1] + 2 * kx[2] + kx[3]) / 6,
                        self.x[-1][1] + (ky[0] + 2 * ky[1] + 2 * ky[2] + ky[3]) / 6,
                        self.x[-1][2] + (kz[0] + 2 * kz[1] + 2 * kz[2] + kz[3]) / 6])

    def Simulacija(self, *args):
        for obj in [self, *args]:
            obj.Euler()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Prikaz svih grafova
        for obj, name, color in zip([self, *args], ['Elektron','Pozitron'], ['blue', 'red']):
            x = []
            y = []
            z = []
            for pos in obj.x:
                x.append(pos[0])
                y.append(-pos[1])
                z.append(pos[2])
            ax.plot(x, y, z, color=color, label=name)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()

    
    def Usporedba(self):
        Nabijene_cestice.Euler(self)
        color_euler = 'blue'
        label_euler = 'Euler'

        Nabijene_cestice.Runge_Kutta(self)
        color_rk = 'red'
        label_rk = 'Runge-Kutta'

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x_euler = []
        y_euler = []
        z_euler = []
        for pos in self.x_euler:
            x_euler.append(pos[0])
            y_euler.append(-pos[1])
            z_euler.append(pos[2])

        x_rk = []
        y_rk = []
        z_rk = []
        for pos in self.x_rk:
            x_rk.append(pos[0])
            y_rk.append(-pos[1])
            z_rk.append(pos[2])

        ax.plot(x_euler, y_euler, z_euler, color=color_euler, label=label_euler)
        ax.plot(x_rk, y_rk, z_rk, color=color_rk, label=label_rk)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()
        plt.title('Usporedba Eulerove i Runge-Kutta metode')
        plt.show()





p = Nabijene_cestice(E=np.array((0, 0, 0)), B=np.array((0, 0, 1)), v=np.array((0.1, 0.1, 0.1)), m=1, q=1, x=np.array((0, 0, 0)), dt=0.01, t_kr=20)
e = Nabijene_cestice(E=np.array((0, 0, 0)), B=np.array((0, 0, 1)), v=np.array((0.1, 0.1, 0.1)), m=1, q=-1, x=np.array((0, 0, 0)), dt=0.01, t_kr=20)
e1 = Nabijene_cestice(E=np.array((0, 0, 0)), B=np.array((0, 0, 1)), v=np.array((0.1, 0.1, 0.1)), m=1, q=-1, x=np.array((0, 0, 0)), dt=0.2, t_kr=20)
p.Simulacija(e)
plt.title('Usporedba gibanja elektrona i pozitrona')
plt.show()
e1.Usporedba()