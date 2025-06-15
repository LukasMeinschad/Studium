import numpy as np

def householder_qr(A):
    """
    Performs QR Decomposition using Householder Reflections in Python


    Parameters:
    ---------
    A: Input matrix

    Returns:
    --------
    Q: Orthogonal Matrix
    R: Upper Triangular Matrix
    """

    m,n = A.shape # Get the matrix dimensions
    Q = np.eye(m) # Initialize Q matrix
    R = A.copy() # Initialize R as Copy of r

    for k in range(min(m,n)):
        # Extract the k-th column vector
        x = R[k:,k]


        # Compute the Householder Vector
        e1 = np.zeros_like(x)
        e1[0] = 1
        v =  np.sign(x[0])*np.linalg.norm(x) * e1 + x  # Initialize v
        v = v / np.linalg.norm(v)

        # Compute the householder reflection matrix
        H = np.eye(m)

        H[k:,k:] -= 2 * np.outer(v,v)

        # Update both R and Q
        R = H@R
        Q = Q@H.T

    return Q,R

# Example usage
A = np.array([[12, -51, 4],
              [6, 167, -68],
              [-4, 24, -41]], dtype=float)

Q, R = householder_qr(A)


print("------------------QR Decomposiiton using Householder Reflections----------------------------")
print("Matrix A:")
print(A)
print("\nOrthogonal matrix Q:")
print(np.round(Q, 4))
print("\nUpper triangular matrix R:")
print(np.round(R, 4))
print("\nVerification (Q @ R):")
print(np.round(Q @ R, 4))

def QR_decomposition_gram_schmidt(A):
      """
      Implementation of the QR-Decomposition Using Gram-Schmidt Process
      """
      n,m = A.shape

      Q = np.empty((n,n)) # Initialize Q
      u = np.empty((n,n)) # Initialize U matrix

      u[:, 0] = A[:, 0] # Extract first column
      Q[:,0] = u[:,0] / np.linalg.norm(u[:,0])  # Normalize

      for i in range(1,n):
          u[:,i] = A[:,i] # Extract the vector
          for j in range(i):
              u[:,i] -= (A[:,i] @ Q[:,j]) * Q[:,j] # Substract projection
          Q[:,i] = u[:,i]/ np.linalg.norm(u[:,i]) # Compute the new e vector

      R = np.zeros((n,m))
      for i in range(n):
          for j in range(i,m):
              R[i,j] = A[:,j] @ Q[:,i]
      return Q,R

Q, R = QR_decomposition_gram_schmidt(A)

print("------------------------QR Decomposition using Gram-Schmidt Process-------------------------")
print("Matrix A:")
print(A)
print("\nOrthogonal matrix Q:")
print(np.round(Q, 4))
print("\nUpper triangular matrix R:")
print(np.round(R, 4))
print("\nVerification (Q @ R):")
print(np.round(Q @ R, 4))
