import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint  # for comparison


"""
Implementation of different Runge-Kutta Methods
-----------------------------------------------

Using a Pendulum equation: y''(t) + by'(t) +csin(y(t))= 0

we will explore different numerical methods to solve this equations

First we transform into a first order equation

set w(t) = y'(t) 

y'(t) = w(t) 
w'(t) = -bw(t) - csin(y(t))
"""

def pend(y,t,b,c):
    return np.array([y[1], -b*y[1] - c*np.sin(y[0])])

b = 0.25
c = 5.0
y0 = np.array([np.pi-0.1,0.0])

t = np.linspace(0,10,101)
# Use Odeint function to approximate solution
sol = odeint(pend,y0, t, args=(b,c))

plt.plot(t, sol[:, 0], 'b', label=r'$\theta(t)$')
plt.plot(t, sol[:, 1], 'g', label=r'$\omega(t)$')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()


"""
Runge Kutta-Method of Order 1 --> Euler Method

y_{n+1} = y_n + (t_{n+1}- t_n)f(y_n,t)

Here H = t_{n+1} - t-n is the step size
"""

def rungekutta1(f,y0,t,args=()):
    n = len(t)
    y = np.zeros((n,len(y0)))
    y[0] = y0
    for i in range(n-1):
        y[i+1] = y[i] + (t[i+1]-t[i])*f(y[i],t[i],*args)
    return y

sol = rungekutta1(pend,y0,t,args=(b,c))

plt.plot(t, sol[:, 0], 'b', label=r'$\theta(t)$')
plt.plot(t, sol[:, 1], 'g', label=r'$\omega(t)$')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

"""
Runge Kutta Method 2 (Mid-Point-Rule)
-------------------------------------

Given by the butcherau tableu 

0 | 
1/2 | 1/2
--------
     0  1 

y_{n+1)} = y_n  + h*f(t + h/2, y_n + h/2 f(t,y_n))
"""

def rungekutta2(f,y0,t,args=()):
    n = len(t)
    y = np.zeros((n,len(y0)))
    y[0] = y0
    for i in range(n-1):
        h = t[i+1] - t[i]
        y[i+1] = y[i] + h * f(y[i] + f(y[i], t[i], *args) * h / 2., t[i] + h / 2., *args)
    return y

t1 = np.linspace(0,10,21)
sol1 = rungekutta2(pend,y0,t1,args=(b,c))
t2 = np.linspace(0,10, 101)
sol2 = rungekutta2(pend,y0,t2,args=(b,c))
t3 = np.linspace(0,10,1001)
sol3 = rungekutta2(pend,y0,t3,args=(b,c))

plt.plot(t1,sol1[:,0], label="11 Points")
plt.plot(t2,sol2[:,0],label="101 Points")
plt.plot(t3,sol3[:,0], label="1001 Points")
plt.legend(loc="best")
plt.grid()
plt.show()


"""
Implementation fo Runge Kutta 4 Method

we have the update y{n+1} = y_n + h/g(k_1 + 2k_2 + 2k_3 + 4k_4)

with 

k_1 = f(yn, tn)
k_2 = f(y_n + 1/2k_1, t_n + h/2)
k_3 = f(y_n + h/2k_2, t_n + h/2)
k_4 = f(y_n + hk_3, t_n + h)
"""

def rungekutta4(f, y0, t, args=()):
    n = len(t)
    y = np.zeros((n, len(y0)))
    y[0] = y0
    for i in range(n - 1):
        h = t[i+1] - t[i]
        k1 = f(y[i], t[i], *args)
        k2 = f(y[i] + k1 * h / 2., t[i] + h / 2., *args)
        k3 = f(y[i] + k2 * h / 2., t[i] + h / 2., *args)
        k4 = f(y[i] + k3 * h, t[i] + h, *args)
        y[i+1] = y[i] + (h / 6.) * (k1 + 2*k2 + 2*k3 + k4)
    return y
