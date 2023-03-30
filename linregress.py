#linregress
#import matplotlib.pyplot as plt
#import numpy as np
import math as m
M=[0.052, 0.124, 0.168, 0.236, 0.284, 0.336] #mjerna jedinica za moment sile Nm
φ=[0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] # mjern jedinica za kut zakretanja rad
φM=0
x_naz=0
y_bro=0
#y=a*x
#a=avrage(x*y)/avrage(x**2)
#stda=np.sqrt(1/n*(avrage(y**2)/avrage(x**2)-a**2))
#modul torzije Dt
#generalne formule
#M=Dt*φ
#Dt=pros_xy/pros_^2

#if len(M)==len(φ):
#    print('true, len je {}'.format(len(M)))
#else:
#    print('false')

φM=sum(M)*sum(φ)
avr_φM=φM/6
print(avr_φM)
avr_M=y_bro/6
avr_φ=x_naz/6
Dt=avr_φM/avr_φ
std=m.sqrt(1/6*((avr_M)/(avr_φ))-Dt**2)

