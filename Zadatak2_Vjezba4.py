#Zadataka 2, Vjezba 4
import Particle as P
import numpy as np
import matplotlib.pyplot as plt
#x(t)=x_0+vx*t
er=[]
ad=[]
k = np.radians(60)
for t in np.arange(0.01, 0.2, 0.001):
    d = 10*np.cos(k)*t
    ad.append(d)

num = []
for dt in np.arange(0.01, 0.2, 0.001):
    p = Particle(10, 60, 0, 0)
    a = p.range(dt)
    num.append(a)

plt.plot(vri, er)
plt.title('Ovisnost odstupanja o koraku dt')
plt.xlabel('dt [s]')
plt.ylabel('Odstupanje [%]')
plt.show()