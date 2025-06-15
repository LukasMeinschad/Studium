import numpy as np
import matplotlib.pyplot as plt

"""
1 Dimensional Case 

Remember the update step in gauß newton method is given by

x_(k+1) = x_k + alpha_k(J(x_k)^T J(x_k))^-1 * (J(x_k))^T f(x^k)
"""

def function1(a,b,x):
    return a*x/(b+x)

f1 = function1

x = np.linspace(0,5,50)
y = f1(2,3,x) + np.random.normal(0,0.1,size=50)

plt.scatter(x,y)
plt.show()

def Jacobian(f,a,b,x):
    eps = 1e-6
    # Central Differences for Jacobian Matrix
    grad_a = (f(a+eps,b,x) - f(a-eps,b,x))/(2*eps)
    grad_b = (f(a,b+eps,x) - f(a,b-eps,x))/(2*eps)
    return np.column_stack([grad_a, grad_b])

def Gauss_Newton(f,x,y,a0,b0,tol,max_iter):
    old = new = np.array([a0,b0])
    for itr in range(max_iter):
        old = new
        J = Jacobian(f, old[0],old[1],x) # Calculate Jacobian at current point
        dy = y - f(old[0],old[1],x) # Calculate function value
        new = old + np.linalg.inv(J.T @ J)@J.T@dy
        if np.linalg.norm(old -new) < tol:
            break
    return new

a,b = Gauss_Newton(f1,x,y,5,1,1e-5,10)

y_hat = f1(a,b,x)

plt.scatter(x,y)
plt.plot(x,y_hat)
plt.show()

"""
2 Dimensional Case
"""

def function3(a,b,x):
    return a-(1/b)*x[:,0]**2 - x[:,1]**2

f3 = function3

# Generate data rows from real model

x1 = np.linspace(-5,5,50)
x2 = np.linspace(-5,5,50)
X1,X2 = np.meshgrid(x1,x2)
X = np.column_stack([X1.ravel(), X2.ravel()])
y = f3(5,4,X) + np.random.normal(0,1,size=len(X))

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")
ax.scatter(X[:,0],X[:,1],y, c=y, marker="o")
plt.show()

a,b = Gauss_Newton(f3,X,y,3,1,1e-5,50)
y_hat = f3(a,b,X)

from matplotlib import cm

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X[:,0].reshape(50,50), X[:,1].reshape(50,50),y_hat.reshape(50,50),cmap=cm.coolwarm)
ax.scatter(X[:,0],X[:,1],y,c=y, marker="o")
plt.show()
