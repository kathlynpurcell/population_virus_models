# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:25:50 2020

@author: kpurc
"""

import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.integrate import odeint

cont,heal = 0.35,1./7 #contact rate #chance to heal in days
H,S,I = .99,0.01,0


def virus(x, t0, cont0=cont, heal0=heal):
    H_f = -cont*x[0]*x[1]
    S_f = cont*x[0]*x[1] - heal*x[1]
    I_f = heal*x[1]
    return H_f, S_f, I_f


t = range(0,200) #time range
x = [H,S,I]

Virus_f = odeint(virus, x, t)
print(x)

H_p,S_p,I_p=Virus_f.T




fig, ax = plt.subplots()
ax.plot(t, H_p, label="Healthy")
ax.plot(t, S_p, label="Sick")
ax.plot(t, I_p, label="Immune")
plt.title("Influenza Shot H: "+str("%.3f" % H)+", S: "+str("%.3f" %S)+", I: "+str("%.3f" %I))
ax.legend(loc="center",fontsize=14)
ax.set_xlabel("Time (days)")
ax.set_ylabel("People (%)")

plt.show()
#plt.savefig("FLU_shot.png")