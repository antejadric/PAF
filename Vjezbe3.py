#Vjezbe3.
#Zadatak 1.
#a)
a=5.0-4.935 #očekivani rezlutat 0.065
print(a)#rezlutat je 0,06500000000000039
#Razlog zašto rezlutat nije 0.065 već 0,06500000000000039 je 
# pogreška u zaokruživanju. Broj kao što je 4.935 se u 
# pythonu ne gleda kao decimalni već kao binarni broj
#. Samo s brojevima oblika 1/2^{n} može idealno računati sve ostalo je aproksimacija, aproksimacija kojom se približava toj vrijednosti što je više moguće.

#b)
b=0.1+0.2+0.3
print(b)
print('ovdje staje 1.zdk')
#rezultat je 0.6000000000000001
#Razlog rezultat jest taj što, baš kao i u prvom slučaju, Python ne vidi naše desimalne brojeve kao takve već kao njihovu binarnu
#reprezentaciju koja nije točno jednaka dotičnimk brojevima pa samim tim ni njihov zbroj neće biti.

#Zadatak 2.
br=0
N1=200
N2=2000
N3=20000

while br==0:
    for ele in range(N1):
        ele=1/3
        br=br+ele
    print('Rezlutat zbrajanja 200 iteracija je {}.'.format(br))

    br=0

    for le in range(N2):
        le=1/3
        br=br+le
    print('Rezlutat zbrajanja 2000 iteracija je {}.'.format(br))

    br=0

    for l in range(N3):
        l=1/3
        br=br+le
    print('Rezlutat zbrajanja 20000 iteracija je {}.'.format(br))

    br=5

    for i in range(N1):
        i=1/3
        br=br-i
    print('Rezultat od 200 oduzetih iteracija broju 5 je {}.'.format(br))
   
    br=5

    for j in range(N2):
        j=1/3
        br=br-j
    print('Rezultat od 200 oduzetih iteracija broju 5 je {}.'.format(br))

    br=5

    for k in range(N3):
        k=1/3
        br=br-k
    print('Rezultat od 200 oduzetih iteracija broju 5 je {}.'.format(br))