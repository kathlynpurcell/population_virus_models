# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:55:31 2020

@author: kpurc
"""

import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.integrate import odeint

a,b,c = 0.14,1./100, 0.0035 
    #two hear and then tells others 
    #heal after 1 semester 
    #chance to leave is 50% per person 
H,S,I = .999,0.001,0


def death(x, t0, a0=a, b0=b):
    H_f = -a*x[0]*x[1]
    S_f = a*x[0]*x[1] - (b+c)*x[1]
    I_f = b*x[1]
    return H_f, S_f, I_f


t = range(0,200) #time range
x = [H,S,I]

Virus_f = odeint(death, x, t)
#print(x)

H_p,S_p,I_p=Virus_f.T*15

Dead=15-(H_p+S_p+I_p)
Pop = (H_p+S_p+I_p)

#PLOTTING
fig, ax = plt.subplots()
ax.plot(t, H_p, label="What's Modeling?", color="green")
ax.plot(t, S_p, label="Scared", color='orange')
ax.plot(t, Dead, label="Droped Out", color="black")
ax.plot(t, I_p, label="Confident", color='blue')
ax.plot(t, Pop,'--', color='0.8', label="Total Inrolled")
plt.title("Status of Astro Freshman in their 1st Year")
ax.legend(loc="center left",fontsize=10)
ax.set_xlabel("Time (days)")
ax.set_ylabel("People")

plt.show()
plt.savefig("fresh_death.png")