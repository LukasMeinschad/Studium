import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve


def newton_explicit_derivative(f,Df,x0,epsilon,max_iter):
    """
    Explicit Implementation of the Newton method to solve f(x) = 0

    Parameters
    ----------
    f: function
        function
    x0: number
        initial guess
    epsilon: number
        tolerance 
    max_iter: integer
        maximum number of iterations of Newton's Method
    """

    xn = x0
    x_history = [xn]

    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print(f"Found solution after {n} iterations")
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print("Zero derivative. No Solution found")
            return None
        xn = xn - fxn/Dfxn
        x_history.append(xn)
    print("Exceeded maximum number of iterations. No solution found")
    return None

p = lambda x: x**3  - x**2 - 1
Dp = lambda x: 3*x**2 - 2*x
approx = newton_explicit_derivative(p,Dp,1,1e-10,20)
print(approx)


def simplified_newton(f,J,x0,tol=1e-8,max_iter=50):
    """
    Implementation of the simplified newton method with fixed jacobian matrix

    Parameters
    ---------
    f: function 
        the function we want to study
    J: function
        the jacobian matrix
    x0: array
        starting value
    tol: float
        tolerance for the iteration
    max_iter: int
        maximum number of iterations
    """
    x = x0.copy()
    J0 = J(x0) # initial jacobian
    conv_history = [x.copy()]
    error_history = [np.linalg.norm(f(x))]

    for k in range(max_iter):
        fx = f(x)
        if np.linalg.norm(fx) < tol:
            break

        # Solve the system J0 * Delta x = -f(x)
        delta_x = solve(J0,-fx)
        x += delta_x

        conv_history.append(x.copy())
        error_history.append(np.linalg.norm(f(x)))
    return x, np.array(conv_history), np.array(error_history)

# Beispiel: Nichtlineares Gleichungssystem
def f(x):
    return np.array([
        x[0]**2 + x[1]**2 - 4,
        np.exp(x[0]) + x[1] - 1
    ])

def J(x):
    return np.array([
        [2*x[0], 2*x[1]],
        [np.exp(x[0]), 1]
    ])

# Startwert
x0 = np.array([1.0, 2])

# Anwendung des vereinfachten Newton-Verfahrens
sol, conv_hist, error_hist = simplified_newton(f, J, x0)

# Plot der Konvergenz
plt.figure(figsize=(12, 5))

# Plot 1: Iterationspfad
plt.subplot(1, 2, 1)
plt.plot(conv_hist[:, 0], conv_hist[:, 1], 'o-')
plt.plot(sol[0], sol[1], 'rx', markersize=10, label='Lösung')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Iterationspfad im Zustandsraum')
plt.grid(True)
plt.legend()

# Plot 2: Fehlerkonvergenz
plt.subplot(1, 2, 2)
plt.semilogy(error_hist, 'o-')
plt.xlabel('Iteration')
plt.ylabel('||f(x)||')
plt.title('Fehlerkonvergenz (logarithmisch)')
plt.grid(True)

plt.tight_layout()
plt.show()

print(f"Gefundene Lösung: {sol}")
print(f"Funktionswert an der Lösung: {f(sol)}")
print(f"Anzahl Iterationen: {len(conv_hist)-1}")
