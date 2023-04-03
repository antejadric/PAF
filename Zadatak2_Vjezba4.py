#Zadataka 2, Vjezba 4
import Particle as P
import numpy as np
import matplotlib.pyplot as plt
#x(t)=x_0+vx*t

ad=[]
k=np.radians(60)
for t in np.arange(0.01,0.2,0.001):
    d=10*np.cos(k)*t
    ad.append(d)
print(ad)

er=[]
p=P.Particle(10, 60, 0, 0)

for dt in np.arange(0.01,0.2,0.001):
    n=p.range(dt)
    gr=abs(n-d)/d
    a=gr*100
    er.append(a)
print(er)