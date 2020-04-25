# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:16:36 2020

@author: kpurc
"""

import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.integrate import odeint


### Plotting the census from the website
pop = open("pop.txt", 'r+')

n=0
#pop_line=[]
column=[]
while n<42:
    pop_line = pop.readline()
    column.append(pop_line.split("\t"))
    n=n+1

year, population = [],[]
n=0
while n<42:
    year.append(column[n][0])
    n=n+1
n=0
while n<42:
    population.append(column[n][1])
    n=n+1

pop_float = list(np.float_(population))
year_float = list(np.float_(year))
    
    
#k = 0.3 #growth rate
#N = 1000 #population constraint
P=75000 #initial population

k0=0.0236 #current growth rate of US
N0=432639000 #400,000,000

while N0 < 500000000:

    def logistic(y, t0, k=k0, N=N0):
        P_dot = k*y[0]*(1-(y[0]/N))
        return P_dot
    
    t = range(1610,2100) #time range
    
    log = odeint(logistic, P, t)
    
    N_line = [N0]*490
    
    fig, ax = plt.subplots()
    ax.plot(t, log, label="Logistic Plot")
    ax.plot(t,N_line, label='Population Constraint')
    #plt.annotate('Population Constraint', xy=(0, 1001))
    plt.title("Logistic Equation v. US Census k= "+str("%.4f" % k0)+" N= "+str(N0))
    
    
    ax.plot(year_float, pop_float, label="US Census")
    ax.legend(loc="center left",fontsize=14)
    ax.set_xlabel("Time")
    ax.set_ylabel("Population")
    ax.set_ylim(0,532639000)
    #plt.show()
    plt.savefig("VerhulstN"+str("%.1f" % N0)+"k"+str("%.4f" % k0)+".png")
    
    N0=N0+10000000

