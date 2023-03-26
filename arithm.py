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




