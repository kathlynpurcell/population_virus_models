# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:35:54 2020

@author: kpurc
"""
import numpy as np
import matplotlib.pyplot as plt
time, pop1 = np.loadtxt ("pop.txt", unpack=True)
inds_sorted = time.argsort()
time = time[inds_sorted]
#time=time-1220
#1600-2100
pop1 = pop1[inds_sorted]
p=75000
k=0.02
#k=0.0414
nmax=410 #460 mil
pop=[p]
x=np.arange(0,410,1)

pop2=np.zeros(len(x))
pop2[0]=p

#print(p,r,nmax)

for n in range(1,nmax):
   p=p+(k*p*(1-p/460000000))
   pop=np.append(pop,p)


plt.figure()
plt.legend()


for n in range(len(x)-1):
    p=pop2[n]*np.exp(k*1)
    pop2[n+1]=p

x= x+1610
plt.plot(x,pop,'ro',markersize=2,label='Logistic Model')
#plt.plot(x,pop2,'green',label='Exponential Model')    
plt.plot(time,pop1,'blue',markersize=5,label='Census Data')
plt.xlabel('Time Step')
plt.ylabel('Population')
plt.title('Logistic Model')
plt.legend()
plt.show()