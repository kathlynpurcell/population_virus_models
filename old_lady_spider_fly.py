# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 23:48:00 2020

@author: kpurc
"""


import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.integrate import odeint

a,b,c,d,e,f,g,h,i = 1,0.1,0.1,1.5,0.5,0.2,1.5,0.2,0.2
F = 3
S = 2
L = 1
x = [F,S,L]

def FSL_find(x, t0, a0=a, b0=b, c0=c, d0=d,e0=e,f0=f,g0=g,h0=h,i0=i):
    f_dot =  a0*x[0] - b0*x[0]*x[1] - c0*x[0]*x[2]
    s_dot = -d0*x[1] + e0*x[0]*x[1] - f0*x[1]*x[2]
    l_dot = -g0*x[2] + h0*x[0]*x[2] + i0*x[2]*x[1]
    return np.array([f_dot, s_dot, l_dot])


t = range(0,50) #time range

FSL_found = odeint(FSL_find, x, t)




fig, ax = plt.subplots()
#ax.scatter(RF_found[:,0], RF_found[:,1], label="Rabits v. Foxes")
plt.plot(t, FSL_found[:,0], label="Flies")
plt.plot(t, FSL_found[:,1], label="Spiders")
plt.plot(t, FSL_found[:,2], label="Lady")
plt.title("LV Old Lady Who Swalloed the Fly F= "+str(F)+" S= "+str(S)+" L= "+str(L))

ax.legend(loc="upper left",fontsize=12)
ax.set_xlabel("Time")
ax.set_ylabel("Happiness/Spiders/Flies")

plt.show()
plt.savefig("LV_FSL_long_F="+str(F)+"S="+str(S)+"L="+str(L)+".png")