#calculus
#1.Zadatak##################################################
import numpy as np
class calculus:
    def __init__(self, a, b, x, dx, n):
        self.a = a
        self.b = b
        self.x = x
        self.dx = dx
        self.n=n

    def derivacijaI(self, f, x, dx, IIPmeth=True):
        if IIPmeth:
            der = (f(x)-f(x-dx))/dx
        else:
            der = (f(x+dx)-f(x-dx))/(2*dx)
        return der
    
    def derivacijaII(self, f, a, b, dx, IIPmeth=True):
        tocke_derivacije=[]
        N=np.linspace(a,b,100)
        for ele in N:
            if IIPmeth:
                der=(f(ele)-f(ele-dx))/dx
                tocke_derivacije.append(der)
            else:
                der=(f(ele+dx)-f(ele-dx))/(2*dx)
                tocke_derivacije.append(der)
        return N,tocke_derivacije
#2.Zadatak################################################
    def integracijaI(self, f, x, a, b, dx, n):
        gornja_gran=[]
        donja_gran=[]
        N=np.linspace(a,b,n)
        for i in range(1,n):
            F_U=f(N[i])*dx
            gornja_gran.append(F_U)
            F_L=f(N[i-1])*dx
            donja_gran.append(F_L)
        return gornja_gran,donja_gran 
    
    def integracijaII(self, f, a, b, dx, n):
        numericka_vrijednost=[]
        suma=[]
        N=np.linspace(a,b,n)
        for j in range(1,n):
            sc=f(N[j]+(f(N[j])+f(N[0]))/2)
            suma.append(sc)
            h=sum(suma)
            trap=dx*h
            numericka_vrijednost.append(trap)
        return numericka_vrijednost