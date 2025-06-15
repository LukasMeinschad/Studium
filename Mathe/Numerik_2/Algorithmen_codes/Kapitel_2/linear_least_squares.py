# We now consider artificial data x = np.linspace(0,1,101)
# and y = 1+x+x*np.random.random(len(x))
# we do least squares regression with y_hat = alpha_1 x + alpha_2 
# Again we have to compute the normal equations beta(A^T A)^-1 A^T Y

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt



# generate x and y

x = np.linspace(0,1,101)
y = 1+x+x*np.random.random(len(x))

# Assemble the matrix a whcih containes the model at our datapoints


A = np.vstack([x, np.ones(len(x))]).T

y = y[:, np.newaxis] # Turns y into a column vector

# Determines alpha from the normal equations
alpha = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),y)
print(alpha)

# plot the results
plt.figure(figsize = (10,8))
plt.plot(x, y, 'b.')
plt.plot(x, alpha[0]*x + alpha[1], 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
