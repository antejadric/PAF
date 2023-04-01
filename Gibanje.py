#Gibanje
import Particle as P
p=P.Particle(10, 45, 0, 0)
p.range(0.01) # rezultat dometa je 10.18233764908627 m. 
p.plot_trajectory()
p.reset()

#Analitcko rjesavanje zadatka
#Analiticka formula d=(v0**2 sin(theta))/g
import numpy as np
g=9.81
v0=float(input('Pocetna brzina: '))
theta=float(input('kut u stupnjevima'))
k=np.radians(theta)
d=(v0**2*np.sin(2*k))/g
print('Domet kod analitickog rjesenja iznosi {}.'.format(d))#rezultat dometa je 10.19367991845056 m.
a=10.18233764908627  #iznod dometa za dt=0.01
b=9.899494936611669  #iznos dometa za dt=0.1
Err=abs(a-d)/d
Err1=abs(b-d)/d
po=float(Err)*100
po1=float(Err1)*100
print('odstupanje za dt=0.01 je {} %'.format(po))
print('odstupanje za dt=0.1 je {} %'.format(po1))
#Numericko rijesenje je drukcije od analitickog, odstupanje se smanjuje samnjivanjem promjene vredmenskog intervala dt.