#Zadatak1_Vjezba5
import calculus as c
import numpy as np 
import matplotlib.pyplot as plt 
def kubna_f(x):
    return 5*(x**3)-2*(x**2)+2*x-3

def trig_f(x):
    return np.sin(x)

def d1kubna_f(x):
    return 15*(x**2)-4*x+2

de=derivacije(a=-2,b=2,x=None,dx=0.1)
tr=de.derivacijaII(f=trig_f)
print(tr)

