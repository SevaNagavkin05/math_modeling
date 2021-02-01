import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.linspace(0,25,100)
def radio_function(v,t):
    dmdt=-k*v**2/m+a_0
    return dmdt
m=10
a_0=2
k=0.05
v_0=0
solve_Bi=odeint(radio_function,v_0,t)
plt.plot(t,solve_Bi[:,0],label='график')
plt.legend()
plt.show