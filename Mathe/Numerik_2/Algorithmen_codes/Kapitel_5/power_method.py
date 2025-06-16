"""
This notebook contains the code to applying the Power Method to compute the eigenvalues of a given Matrix


**Power Method**

Can be used to compute the eigenvalue of largest magnitude lambda_1 and the eigenvector v_1.

**Algorithm**

Choose an initial vector y_0 with an random number generator

+ normalize x_0 = y_0 // ||y_0||

for k from 0 to k_max
    y_{k+1} = A x^k
    r(k) = <y_{k+1},x^k >
    x^{k+1} = y^{k+1} / ||y^{k+1}
end

the final values of r^{k} and x^{k} approximate lambda_1 and v_1
"""
import numpy as np

A = np.array([
    [3,1,1],
    [1,8,1],
    [1,1,4]
])


def power_method(A,max_iter=10):
    n = A.shape[0]
    y_0 = np.random.rand(3)
    x = y_0 / np.linalg.norm(y_0) # Normalize
    for k in range(1,max_iter):
        y_new = A @ x
        r_k = np.dot(y_new, x)
        x = y_new / np.linalg.norm(y_new)
    return r_k, x

l_1, v_1 =power_method(A)
# compute eigenvalues using numpy
eigenvalues_np, eigenvectors_np = np.linalg.eig(A)


print("Largest Eigenvalue: ",l_1 )
print("Largest Eigenvector: ",v_1 )
print("Numpy Eigenvalues:", eigenvalues_np)
print("\n")
print("Numpy Eigenvectors: ", eigenvectors_np)
