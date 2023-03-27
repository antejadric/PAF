class Particle:
    def __init__(self,mass,x_0,v_0):
        self.mass=mass
        self.x_0=x_0
        self.v_0=v_0

    def printInfo(self):
        print('Masa cestice=',self.mass)
        print('Polozaj cestice=',self.x_0)
        print('Pocetna brzina=',self.v_0)
    def moveToOrigin(self):
        self.x_0=0
    def prombrzine(self,a):
        self.v_0+=a


