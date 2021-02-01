import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t=np.linspace(0,10,100)
def radio_function(m,t):
    dmdt=-k*m*t
    return dmdt
m_0=1000
k=0.08

solve_Bi=odeint(radio_function,m_0,t)
plt.plot(t,solve_Bi[:,0],label='график')
plt.legend()
plt.show








