#Seminar
#Tema 4
# Tekst zadataka: Razvijte vlastiti modul koji ce korisniku omoguciti numericko racunanje polozaja, brzine i akceleracije za
#jednodimenzionalno gibanje. Neka modul radi za bilo koju silu koju korisnik moze definirati kao proizvoljnu
#funkciju brzine, polozaja i vremena (F = f(v, x, t)). Testirajte modul u slucajevima konstante sile (F =
#const) i harmonickog oscilatora (F = −kx).
import numrac_vxt as N

def f1(v, x, t):#za konstantnu silu
    return 5

u = N.Num_racunanje(x=3, v=2, m=3, dt=0.01, t=20, f=f1)
u.Graf(f1)



def f2(v, x, t):#za harmonijski oscilator.
    return -2 * x

h = N.Num_racunanje(x=3, v=2, m=3, dt=0.01, t=20, f=f2)
h.Graf(f2)
