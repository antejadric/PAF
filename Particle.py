#Vjezba 4
#1. Zadatak
import numpy as np
import matplotlib.pyplot as plt
class Particle:
    def __init__(self,v_0,Θ,x,y):
        self.v_0=v_0
        self.Θ=Θ
        self.x=x
        self.y=y
        self.vy=[]
        self.vx=[]
        y=[]
        x=[]
    def reset(self):
        self.v_0=[]
        self.Θ=[]
        self.x=[]
        self.y=[]

    def __move(self, dt):
        g=9.81
        self.vy=self.v_0[-1]-g*dt
        self.vy.append(self.vy)
        self.vx=self.v_0[-1]
        self.vx.append(self.vx)
        self.x=self.x[-1]+g*dt
        self.x.append(self.x)
        self.y=self.y[-1]+self.vy[-1]*dt
        self.y.append(self.y)


