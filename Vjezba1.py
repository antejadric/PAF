#Vježba1
#3. zadatak
xk=[]

while True:
    t1=input('unesi x1 koordinatu: ')
    t2=input('unesi x2 koordinatu: ')
    xk.append(t1)
    xk.append(t2)
        
    while not(xk[0].replace('.', '').replace('-', '').isnumeric() and xk[1].replace('.', '').replace('-', '').isnumeric()):
        print('ponovno unesite koordinate')
        xk=[]
        t1=input('unesi x1 koordinatu: ')
        t2=input('unesi x2 koordinatu: ')
        xk.append(t1)
        xk.append(t2)
        
    x1=float(xk[0])
    x2=float(xk[1])
    break

yk=[]

while True:
    T1=input('unesi y1 koordinatu: ')
    T2=input('unesi y2 koordinatu: ')
    yk.append(T1)
    yk.append(T2)
        
    while not(yk[0].replace('.', '').replace('-', '').isnumeric() and yk[1].replace('.', '').replace('-', '').isnumeric()):
        print('ponovno unesite koordinate')
        yk=[]
        t1=input('unesi y1 koordinatu: ')
        t2=input('unesi y2 koordinatu: ')
        yk.append(T1)
        yk.append(T2)
        
    y1=float(yk[0])
    y2=float(yk[1])
    break
try:
    k=(y2-y1)/(x2-x1)
except ZeroDivisionError:
    print('Dijeljenje s nulom')
    exit()

l=k*x1+y1
if l>0:
    print('jednadžba pravca je: {}x+{}.'.format(round(k,2),round(l,2)))
else:
    print('jednadžba pravca je: {}x{}.'.format(round(k,2),round(l,2)))



#4. zadatak
def jednadzba_pravca():
    xk=[]
    while True:
        t1=input('unesi x1 koordinatu: ')
        t2=input('unesi x2 koordinatu: ')
        xk.append(t1)
        xk.append(t2)

        while not(xk[0].replace('.', '').replace('-', '').isnumeric() and xk[1].replace('.', '').replace('-', '').isnumeric()):
            print('ponovno unesite koordinate')
            xk=[]
            t1=input('unesi x1 koordinatu: ')
            t2=input('unesi x2 koordinatu: ')
            xk.append(t1)
            xk.append(t2)

        x1=float(xk[0])
        x2=float(xk[1])
        if x1 == x2:
            continue
        break
    yk=[]
    while True:
        T1=input('unesi y1 koordinatu: ')
        T2=input('unesi y2 koordinatu: ')
        yk.append(T1)
        yk.append(T2)

        while not(yk[0].replace('.', '').replace('-', '').isnumeric() and yk[1].replace('.', '').replace('-', '').isnumeric()):
            print('ponovno unesite koordinate')
            yk=[]
            t1=input('unesi y1 koordinatu: ')
            t2=input('unesi y2 koordinatu: ')
            yk.append(T1)
            yk.append(T2)

        y1=float(yk[0])
        y2=float(yk[1])
        break
    try:
        k=(y2-y1)/(x2-x1)
    except ZeroDivisionError:
        print('Dijeljenje s nulom')

    l=k*x1+y1
    if l>0:
        return 'jednadžba pravca je: {}x+{}.'.format(round(k,2),round(l,2))
    else:
        return 'jednadžba pravca je: {}x{}.'.format(round(k,2),round(l,2))
    
print(jednadzba_pravca())

#5. zadatak

import matplotlib
import matplotlib.pyplot as plt
xk=[]

while True:
    t1=input('unesi x1 koordinatu: ')
    t2=input('unesi x2 koordinatu: ')
    xk.append(t1)
    xk.append(t2)
        
    while not(xk[0].replace('.', '').replace('-', '').isnumeric() and xk[1].replace('.', '').replace('-', '').isnumeric()):
        print('ponovno unesite koordinate')
        xk=[]
        t1=input('unesi x1 koordinatu: ')
        t2=input('unesi x2 koordinatu: ')
        xk.append(t1)
        xk.append(t2)
        
    x1=float(xk[0])
    x2=float(xk[1])
    break

yk=[]

while True:
    T1=input('unesi y1 koordinatu: ')
    T2=input('unesi y2 koordinatu: ')
    yk.append(T1)
    yk.append(T2)
        
    while not(yk[0].replace('.', '').replace('-', '').isnumeric() and yk[1].replace('.', '').replace('-', '').isnumeric()):
        print('ponovno unesite koordinate')
        yk=[]
        t1=input('unesi y1 koordinatu: ')
        t2=input('unesi y2 koordinatu: ')
        yk.append(T1)
        yk.append(T2)
        
    y1=float(yk[0])
    y2=float(yk[1])
    break

x=[x1,x2]
y=[y1,y2]

plt.plot(x, y, marker="o", markersize=13, markeredgecolor="red")
plt.show()
plt.annotate('1', xy=(x1, y1), xytext=(x1+0.1, y1+0.1))
plt.annotate('2', xy=(x2, y2), xytext=(x2+0.1, y2+0.1))
    
