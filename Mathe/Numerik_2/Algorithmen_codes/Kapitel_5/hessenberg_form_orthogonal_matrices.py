import numpy as np

def householder_hessenberg(A):
    """
    Transforms matrix A into upper Hessenberg form using Householder Reflections
    """
    n = A.shape[0]
    H = A.copy().astype(float)
    Q = np.eye(n) # Orthogonal Matrix for Transformation

    for k in range(n-2):
        # Extract the column below the diagonal
        x = H[k+1:, k]

        # Compute the Householder vector
        e1 = np.zeros_like(x)
        e1[0] = 1.0
        vk = np.sign(x[0])*np.linalg.norm(x)*e1 + x
        vk = vk / np.linalg.norm(vk)

        # Apply the Householder Reflection
        H[k+1:,k:] = H[k+1:, k:]  - 2* np.outer(vk,vk@H[k+1:,k:])
        H[:,k+1:] = H[:,k+1:] - 2*np.outer(H[:,k+1:]@vk,vk)

        Q[k+1:,:] = Q[k+1:,:] - 2*np.outer(vk,vk@Q[k+1:,:])
    return H, Q.T


A = np.array([[4, 3, 2, 1],
              [3, 4, 3, 2],
              [2, 3, 4, 3],
              [1, 2, 3, 4]])

H, Q = householder_hessenberg(A)

print(H)

