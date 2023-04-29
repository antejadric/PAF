#Vjezba_6
#provjera preciznosti(1.Zdk)
import Harmonic_oscillator as ho 
import numpy as np 
import matplotlip.pyplot as plt 

hosn=ho.HarmonicOscillator(x=3,v=2,k=1,dt=200,m=3)
ha = ho.HarmonicOscillator(x=3, v=2, k=1, dt=0.01, m=3)
hb = ho.HarmonicOscillator(x=3, v=2, k=1, dt=0.001, m=3)
hc = ho.HarmonicOscillator(x=2, v=2, k=1, dt=0.16, m=3)

def Analiticko_rj(t_kr):
    A = np.sqrt((hosn.x[0])**2+((hosn.m/hosn.k)*(hosn.v[0])**2))
    fi = np.arcsin(hosn.x[0]/A)
    omega=np.sqrt(hosn.k/hosn.m)
    arj=[]
    vrijeme=[]
    for t in np.linspace(0,t_kr,hosn.dt):
        vrijeme.append(t)
        x=A*np.sin(omega*t+fi)
        arj.append(x)
    return vrijeme, arj

def Preciznost(t_kr):
    arj, vrijeme = Analiticko_rj(t_kr=t_kr)
    plt.plot(arj, vrijeme, label='analiticko rjesenje')
    plt.title('Preciznost')
    plt.plot(ha.Izracun(t=20)[0], ha.Izracun(t=20)[1], 'o', color='red',markersize='1')
    plt.plot(hb.Izracun(t=20)[0], hb.Izracun(t=20)[1], 'o', color='blue',markersize='0.1')
    plt.plot(hc.Izracun(t=20)[0], hc.Izracun(t=20)[1], 'o', color='green',markersize='0.5')
    plt.xlabel('t [s]')
    plt.ylabel('x [m]')
    plt.legend(['Analiticko', 'dt = 0.01', 'dt = 0.001', 'dt = 0.16'])
    plt.show()

Preciznost(t_kr=20)
########################################################################################################
#Analiticki i numericki period(2.Zdk)