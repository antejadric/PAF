#Seminar
#Tema 4
# Tekst zadataka: Razvijte vlastiti modul koji ce korisniku omoguciti numericko racunanje polozaja, brzine i akceleracije za
#jednodimenzionalno gibanje. Neka modul radi za bilo koju silu koju korisnik moze definirati kao proizvoljnu
#funkciju brzine, polozaja i vremena (F = f(v, x, t)). Testirajte modul u slucajevima konstante sile (F =
#const) i harmonickog oscilatora (F = −kx).
import numpy as np
import matplotlib.pyplot as plt

class Sila_kao_f:
    def __init__(self, v, x, t):
        self.x = x
        self.v = v
        self.t = t
        self.F = np.array([self.v, self.x, self.t])
        
    class Implementacija:
        def __init__(self, gk, m, k, dt):
            self.F = gk.F
            self.m = m
            self.dt = dt
            self.Sila=[]
            self.a=[]
            self.x=[gk.F[1]]
            self.v=[gk.F[0]]
            self.k=k
            self.ss=[]

        
        def VratInfo(self):
            print('F={}'.format(self.F))
            print('a={}'.format(self.a))
            print('v={}'.format(self.v))
            print('x={}'.format(self.x))
            print('Promjenjiva_sila={}'.format(self.ss))


            
        def konstF(self):
            for i in np.arange(0,self.F[2],self.dt):
                self.Sila.append(sum(self.F))
                self.a.append(self.Sila[-1]/self.m)
                self.v.append(self.x[-1]+self.a[-1]*self.dt)
                self.x.append(self.x[-1]+self.v[-1]*self.dt)

        def Euler(self):
            for i in np.arange(0,self.F[2],self.dt):
                self.a.append(-self.k / self.m * self.x[-1])
                self.v.append(self.v[-1] + self.a[-1] * self.dt)
                self.x.append(self.x[-1] + self.v[-1] * self.dt)
                self.ss.append(-self.k*self.x[-1])