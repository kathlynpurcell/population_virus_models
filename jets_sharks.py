# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:32:26 2020

@author: kpurc
"""

import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.integrate import odeint

a,b = 1,0.6
kj,ks= 1, 0.6
Nj,Ns = 100,100
J = 50
S = 6
#F = 10
x = [J,S]

def JS(x, t0, a0=a, b0=b, kj=kj, ks=ks, Nj=Nj, Ns=Ns):
    j_dot = kj*x[0]*(1-((x[0]+a*x[1])/Nj))
    s_dot = ks*x[1]*(1-((x[1]+b*x[0])/Ns))
    return np.array([j_dot, s_dot])


t = range(0,100) #time range

JS_found = odeint(JS, x, t)


plt.scatter(JS_found[:,0], JS_found[:,1], label="Sharks v. Jets")
#plt.plot(t, JS_found[:,0], label="Jets")
#plt.plot(t, JS_found[:,1], label="Sharks")
    

plt.title("LV for Jets and Sharks J= "+str(J)+" S= "+str(S))

plt.legend(loc="middle left",fontsize=14)
plt.xlabel("Jets")
plt.ylabel("Sharks")
plt.show()
plt.savefig("LVc.png")