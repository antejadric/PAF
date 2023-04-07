#Zadataka 2, Vjezba 4
import Particle as P
import numpy as np
import matplotlib.pyplot as plt
vri=np.linspace(0.01, 0.2, 999)
ad=[]
k = np.radians(60)
for t in vri:
    d = 10*np.cos(k)*t
    ad.append(d)
    f=sum(ad)
#print(f)

num = []
for dt in vri:
    p = P.Particle(10, 60, 0, 0)
    a = p.range(dt)
    num.append(a)
    p.reset()
#print(num)

er=[]
for i in range(len(ad)):
    gr=abs(f-num[i])/f*100
    er.append(gr)
#print(f)

plt.plot(vri, er)
plt.title('Ovisnost odstupanja o koraku dt')
plt.xlabel('dt [s]')
plt.ylabel('Odstupanje [%]')
plt.show()