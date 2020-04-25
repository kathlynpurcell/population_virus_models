# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:43:34 2020

@author: kpurc
"""

import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.integrate import odeint

a,b,c,d,e,f,g = 1,0.1,1.5,0.2,0.5,2,0.2
P = 100
D = 30
B = 5
x = [P,D,B]

def PDB_find(x, t0, a0=a, b0=b, c0=c, d0=d,e0=e,f0=f,g0=g):
    p_dot = a0*x[0] - b0*x[0]*x[1]
    d_dot = -c0*x[1] + d0*x[0]*x[1] - e0*x[1]*x[2]
    b_dot = -f0*x[2] + g0*x[1]*x[2]
    return np.array([p_dot, d_dot, b_dot])


t = range(0,100) #time range

PDB_found = odeint(PDB_find, x, t)




fig, ax = plt.subplots()
#ax.scatter(RF_found[:,0], RF_found[:,1], label="Rabits v. Foxes")
plt.plot(t, PDB_found[:,0], label="Peas")
plt.plot(t, PDB_found[:,1], label="Deer")
plt.plot(t, PDB_found[:,2], label="Bears")
plt.title("Lotka-Voltera Peas, Deer, Bears P= "+str(P)+" D= "+str(D)+" B= "+str(B))

ax.legend(loc="upper center",fontsize=12)
ax.set_xlabel("Time")
ax.set_ylabel("Animals")

plt.show()
plt.savefig("LV_PDB_long_P="+str(P)+"D="+str(D)+"B="+str(B)+".png")