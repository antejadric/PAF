#Zdk1.
import matplotlib.pyplot as plt
import numpy as np

F = float(input('Iznos sile u N: '))
m = float(input('Iznos mase u kg: ')) 
a = F/m #izračun konstantne akceleracije
v0 = 0
x0 = 0
dt = 0.2

t = np.arange(0, 10, dt) #utimanje t točnije uzimanje "koraka" za funkciju
v = [v0]
x = [x0]
akc = [a]
b=len(t)-1 #koristi se da bi program isključio posljednju brojku tako da se ista ne bi oduzimala od ničeg
for i in range(b):
    dv = akc[-1] * dt
    v_i = v[-1] + dv
    v.append(v_i)

    dx = v[-1] * dt
    x_i = x[-1] + dx
    x.append(x_i)

    akc.append(a)
#plotiranje v-t grafa
plt.plot(t, v)
plt.title('v-t graf')
plt.xlabel('t [s]')
plt.ylabel('v [m/s]')
plt.show()

#plotiranje x-t grafa
plt.plot(t, x)
plt.title('x-t graf')
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.show()

#plotiranje a-t grafa
plt.plot(t, akc)
plt.title('a-t graf')
plt.xlabel('t [s]')
plt.ylabel('a [m/s^2]')
plt.show()
#####################################################################################################################################
#Zdk2.
import matplotlib.pyplot as plt
import numpy as np
v0=float(input('Unesi početnu brzinu u m/s: '))
k=float(input('Unesi kut u stupnjevima:'))
pi=np.pi
rad = k*(pi/180)
g=9.81

#za crtanje x-y grafa
t = np.arange(0, 10, 0.2)
x = v0 * np.cos(rad) * t
y = v0 * np.sin(rad) * t - 0.5 * g * t**2

plt.plot(x, y)
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title('x-y graf')
plt.show()

#za crtanje x-t grafa
t = np.arange(0, 10, 0.2)
x = v0 * np.cos(rad) * t

plt.plot(t, x)
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.title('x-t graf')
plt.show()

#za crtanje y-t grafa
t = np.arange(0, 10, 0.2)
y = v0 * np.sin(rad) * t - 0.5 * g * t**2

plt.plot(t, y)
plt.xlabel('t [s]')
plt.ylabel('y [m]')
plt.title('y-t graf')
plt.show()