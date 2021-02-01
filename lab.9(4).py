import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.linspace(0,1000,100)
def radio_function(v,t):
    dmdt=(b-k*v)/m
    return dmdt
m=1000
k=10
v_0=100
b=100

solve_Bi=odeint(radio_function,v_0,t)
plt.plot(t,solve_Bi[:,0],label='график')
plt.legend()
plt.show