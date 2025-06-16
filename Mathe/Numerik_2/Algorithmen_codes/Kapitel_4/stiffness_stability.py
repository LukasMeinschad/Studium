"""
This python script explores the stability of Runge-Kutta Methods

In this first part we consider the explicit Euler Method here the stability function is given by R(lamda h) = 1+lambda h
"""
import numpy as np
import matplotlib.pyplot as plt

def stiff_ode(t,y):
    return -10*y

def exact_solution(t):
    return np.exp(-10*t)

def explicit_euler(f,t0,y0,t_end,h):
    t = np.arange(t0, t_end + h , h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(1,len(t)):
        y[i] = y[i-1] + h*f(t[i-1],y[i-1])
    return t,y

# Time Parameters
t0 = 0
t_end = 1
y0 = 1

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))



## Top plot: Unstable (h > 2/|λ| = 0.2)
h = 0.21  # > 2/10
t, y = explicit_euler(stiff_ode, t0, y0, t_end, h)
ax1.plot(t, y, 'o-', label=f'Explicit Euler (h={h})')
ax1.plot(t, exact_solution(t), 'k-', label='Exact solution')
ax1.set_title('Unstable: h > 2/|λ| (h=0.21 > 0.2)')
ax1.legend()
ax1.grid(True)

## Middle plot: Stable but oscillatory (1/|λ| < h < 2/|λ|)
h = 0.15  # between 0.1 and 0.2
t, y = explicit_euler(stiff_ode, t0, y0, t_end, h)
ax2.plot(t, y, 'o-', label=f'Explicit Euler (h={h})')
ax2.plot(t, exact_solution(t), 'k-', label='Exact solution')
ax2.set_title('Stable but oscillatory: 1/|λ| < h < 2/|λ| (0.1 < h=0.15 < 0.2)')
ax2.legend()
ax2.grid(True)

## Bottom plot: Reasonable solution (h < 1/|λ|)
h = 0.05  # < 0.1
t, y = explicit_euler(stiff_ode, t0, y0, t_end, h)
ax3.plot(t, y, 'o-', label=f'Explicit Euler (h={h})')
ax3.plot(t, exact_solution(t), 'k-', label='Exact solution')
ax3.set_title('Reasonable solution: h < 1/|λ| (h=0.05 < 0.1)')
ax3.legend()
ax3.grid(True)

plt.title("Stability Testing of Explicit Euler Method")
plt.tight_layout()
plt.show()


def implicit_euler(f,t0,y0,t_end,h):
    t = np.arange(t0,t_end + h, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(1,len(t)):
        # For y' = lambda y we can solve this exactly
        # y_{n+1} = y_n + h*lambda*y_{n+1} --> y_{n+1} = y_n / (1-h*lambda)
        y[i] = y[i-1]/(1-h*(-10))
    return t,y


# Time parameters
t0 = 0
t_end = 1
y0 = 1

# Create figure with subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

## Top plot: Large step size (h = 0.5)
h = 0.5
t, y = implicit_euler(stiff_ode, t0, y0, t_end, h)
ax1.plot(t, y, 'o-', label=f'Implicit Euler (h={h})')
ax1.plot(t, exact_solution(t), 'k-', label='Exact solution')
ax1.set_title(f'Large step size (h={h})')
ax1.legend()
ax1.grid(True)

## Middle plot: Medium step size (h = 0.1)
h = 0.1
t, y = implicit_euler(stiff_ode, t0, y0, t_end, h)
ax2.plot(t, y, 'o-', label=f'Implicit Euler (h={h})')
ax2.plot(t, exact_solution(t), 'k-', label='Exact solution')
ax2.set_title(f'Medium step size (h={h})')
ax2.legend()
ax2.grid(True)

## Bottom plot: Small step size (h = 0.02)
h = 0.02
t, y = implicit_euler(stiff_ode, t0, y0, t_end, h)
ax3.plot(t, y, 'o-', label=f'Implicit Euler (h={h})')
ax3.plot(t, exact_solution(t), 'k-', label='Exact solution')
ax3.set_title(f'Small step size (h={h})')
ax3.legend()
ax3.grid(True)

plt.tight_layout()
plt.show()
