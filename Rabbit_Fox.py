# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:32:26 2020

@author: kpurc
"""

import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.integrate import odeint

a,b,c,d = 1,0.1,0.25,1.5
F = 15
R = 15

x = [R,F]

def RF_find(x, t0, a0=a, b0=b, c0=c, d0=d):
    r_dot = a0*x[0] - b0*x[0]*x[1]
    f_dot = c0*x[0]*x[1] - d0*x[1]
    return np.array([r_dot, f_dot])


t = range(0,100) #time range

RF_found = odeint(RF_find, x, t)
#print(RF_found)

#fig, ax = plt.subplots()
#plt.scatter(RF_found[:,0], RF_found[:,1], label="Rabits v. Foxes")
plt.plot(t, RF_found[:,0], label="Rabbits")
plt.plot(t, RF_found[:,1], label="Foxes")
    

plt.title("Lotka-Voltera for Rabbits and Foxes R= "+str("%.4f" % R)+" F= "+str("%.4f" % F))

plt.legend(loc="lower center",fontsize=14)
plt.xlabel("Time")
plt.ylabel("Foxes and Rabbits")
plt.show()
plt.savefig("Lotka-Voltera_Phase_int_R="+str(R)+"F="+str(F)+".png")