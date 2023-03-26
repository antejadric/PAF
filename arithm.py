#arithm
#Zadatak3.Vjezbe3
#a)
import math as m
n=10
l=[]
d=[]
for ele in range(n):
    x=float(input('Unesi točku: '))
    l.append(x)
    s=sum(l)
    pros=s/n

for ele in range(n):
    a=(ele-pros)**2
    d.append(a)
e=sum(d)
naz=n*(n-1)
dev=m.sqrt(e/naz)
print('Aritmetička sredina točaka {} iznosi {}. Standardna devijacija iznosi {}.'.format(l,pros,dev))
#############################################################################################################
#b)
#Zad 2.
import numpy as np
li=[]
for i in range(n):
    t=float(input('Unesi točke: '))
    li.append(i)
b=np.average(li)
c=np.std(li)/np.sqrt(n-1)
print('Standardna devijacija je {}, a aritmetička sredina iznosi {}.'.format(li,c,b))

