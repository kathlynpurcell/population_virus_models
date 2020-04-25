# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:48:03 2020

@author: kpurc
"""


import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.integrate import odeint

a,b,c = 0.1,1./100, 0.019
    #two hear and then tells others 
    #heal after 1 semester 
    #chance to leave is 50% per person 
H,S,I,D = .999,0.001,0,0


def Virus_find(x, t0, a=a, b=b, c=c):
    H_f = -a*x[0]*x[1] - c*x[0]*x[3]
    S_f = a*x[0]*x[1] - (b+c)*x[1] #+ c*x[1]*x[3]
    I_f = b*x[1]
    D_f = c*x[1] + c*x[0]*x[3] 
    return H_f, S_f, I_f,D_f


t = range(0,450) #time range
x = [H,S,I,D]

Virus_f = odeint(Virus_find, x, t)
#print(x)

H_p,S_p,I_p,D_p=Virus_f.T

#Dead=15-(H_p+S_p+I_p)
Pop = (abs(H_p)+abs(S_p)+abs(I_p)+abs(D_p))
#print(Pop)
#PLOTTING
fig, ax = plt.subplots()
ax.plot(t, H_p, label="Healthy", color="green")
ax.plot(t, S_p, label="Sick", color='orange')
ax.plot(t, D_p, label="Zombie", color="black")
ax.plot(t, I_p, label="Immune", color='blue')
ax.plot(t, Pop,'--', color='0.8', label="Total Pop")
plt.title("Zombie Outbreak and Immunity")
ax.legend(loc="center left",fontsize=10)
ax.set_xlabel("Time (days)")
ax.set_ylabel("People")

plt.show()
#plt.savefig("zombies_immunity.png")