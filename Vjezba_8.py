import numpy as np
import matplotlib.pyplot as plt
class Nabijene_cestice:
    def __init__ (self, E, B, v, m, q, dt, t_kr):
        self.E=np.array((self.Ex,self.Ey,self.Ez))
        self.B=np.array((self.Bx,self.By,self.Bz))
        self.v=np.array((self.vx,self.vy,self.vz))
        self.m=m
        self.q=q
        self.dt=dt
        self.t_kr=t_kr
        self.ax=self.q/self.m*(self.E[0]+np.cross(v,B))
        self.ay=self.q/self.m*(self.E[1]+np.cross(v,B))
        self.az=self.q/self.m*(self.E[2]+np.cross(v,B))