# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:37:43 2020

@author: kpurc
"""
import matplotlib.pyplot as plt
import math
import numpy as np
import scipy as sci

def body(t,y):
    #ydot=np.empty(2,)
    alpha = 1
    beta = 0.1
    gamma = 0.25
    delta = 1.5
    rabbit = alpha*y[0] - beta*y[0]*y[1]
    fox = -delta*y[1] +gamma*y[0]*y[1]

    return rabbit, fox

y0 = np.array([10, 5])

sol = sci.integrate.solve_ivp(fun=body, y0=y0, t_span=(0,10000),method='LSODA')
#sol = integrate.odeint(func=body,  y0=y0, t=(0,100))

data=np.transpose(sol.y)
xsol2=data[:,0]
ysol2=data[:,1]

plt.figure()
plt.plot(xsol2, ysol2, color='k')
plt.show()