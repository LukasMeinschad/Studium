"""
Goal of this exercise is to implement the Embedded Runge Kutta (3)(2) Method

This is given by the following butcherau tableau

    0 |
  1/3 | 1/3 
  2/3 | 0     2/3
  -----------------------------
      | 1/4    0     3/4    b_i 
      | 0      1/2   1/2    b_i_hat 
      | -1/4  1/2    -1/4   d_i

Calculation of the optimal Step size given a tolerance tol we can calculate h_opt

||y_1 - y(x_0 + h_opt) || =! tol

so tol = Ch_opt^t and est = || y_1_hat - y_1|| = Ch^p

We use in the simplest case the equation 


h_opt = 0.9 h * sqrt[p](tol / est)

***Algorithm***

For a given diffferential equation y'=f(x,y), starting point (x_0, y_0) and starting step size h \leq x_bar - x_0

We calculate the numerical solution y_1 and y_1 hat and est || h * sum_{i=1}^s d_i Y_i' || = || y_1_hat - y_1||

if est<= tol then
    x_0 := x_0 + h
    y_0 := y_1 
    h := min(h_opt, x_bar - x_0)
else
    remove step and do again with h=h_opt

if x_0 = x_bar then stop
"""

import numpy as np

def embedded_rk32(f, x0, y0, x_bar, h_init, tol):
    """
    Implementation of the Embedded Runge-Kutta (3)(2) method with adaptive step size control

    Parameters:
        f: function
        x0: initial x value
        y0: initial y value
        x_bar: final x value to integrate to
        h_init: initial step size
        tol: tolerance for error control
    
    Returns:
        xs: list of x values
        ys : list of corresponding y values
        hs: list of used step sizes
    """
    y0 = np.asarray(y0)

    # Initialize Solution arrays
    xs = [x0]
    ys = [y0.copy()]
    hs = []

    x = x0
    y = y0.copy()
    h = min(h_init, x_bar - x0)

    while x < x_bar:
        # Stop if we integrated to endpoint
        if abs(x-x_bar) < 1e-14:
            break

        # Calculate the stages
        k1 = f(x,y)
        k2 = f(x + h/3, y + h*(1/3)* k1)
        k3 = f(x + 2*h/3, y + h*(2/3)*k2)

        # Calculate the two solutions
        y1 = y + h*( 1/4*k1 + 3/4 * k3)
        y1_hat = y + h*(1/2* k2 + 1/2*k3)

        # Calculate the error estimate
        est = np.linalg.norm(y1_hat - y1)

        if est <= tol or abs(h) < 1e-14:
            # Step accepted
            x = x+ h
            y = y1.copy()

            xs.append(x)
            ys.append(y.copy())
            hs.append(h)

            if est > 0:
                h_opt = 0.9 * h * (tol / est)**(1/3) # p=3
            else:
                h_opt = 2* h # if error is zero double the step size

            h = min(h_opt, x_bar-x)

        else:
            # Step rejected try again with h_opt
            h_opt = 0.9 * h * (tol / est)**(1/3)
            h = h_opt

            # Runtime error if h is to small
            if abs(h) < 1e-14:
                raise RuntimeError("Step size became to small!")
    return np.array(xs), np.array(ys), np.array(hs)



# Example: Solve y' = -2x*y, y(0) = 1 (solution: y = exp(-x^2))
def f(x, y):
    return -2 * x * y

# Initial conditions
x0 = 0
y0 = np.array([1.0])
x_bar = 2.0
h_init = 0.1
tol = 1e-6

# Solve using embedded RK32
xs, ys, hs = embedded_rk32(f, x0, y0, x_bar, h_init, tol)

# Print some information
print(f"Solution reached x = {xs[-1]} with {len(xs)} steps")
print(f"Final y value: {ys[-1]}")
print(f"Exact solution: {np.exp(-xs[-1]**2)}")

# Plot the solution
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(xs, ys, 'o-', label='Numerical solution')
plt.plot(xs, np.exp(-xs**2), '--', label='Exact solution')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(xs[:-1], hs, 'o-')
plt.xlabel('x')
plt.ylabel('Step size h')
plt.tight_layout()
plt.show()
