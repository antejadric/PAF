#Zadataka 2, Vjezba 4
import Particle as P
import numpy as np
import matplotlib.pyplot as plt
g=9.81
v0=float(input('Pocetna brzina: '))
theta=float(input('kut u stupnjevima'))
k=np.radians(theta)
d=(v0**2*np.sin(2*k))/g
print('Domet kod analitickog rjesenja iznosi {}.'.format(d))

p=P.Particle(10, 60, 0, 0)

