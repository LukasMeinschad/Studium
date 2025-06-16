"""
Algorithm for a given matrix A

(i) Search k \in {2,...,n} with |a_{k1}| = max_{2 \leq j \leq n} |a_{j1}| If a_k1=0 the first column of A is of the form [*,0...0]^T and we are done

    Otherwise we swap second row with k-th row and second column with k-th column (to leave the spectrum the same) A' = P_2 A P_2^{-1}

(ii) Next we perform Gaussian Elemenination step such that L_2 A = [ a_11'   ...   a_1n' 
                                                                    a_21'    ...   a_2n'
                                                                    0       ....    * 
                                                                    0    *          * ]

    for this we determine l_{i2} = -a_{i1}'/a_{21}' and then multiply  L2A'L_2^-1 and iterate to get the Hessenberg form
"""
import numpy as np

A = np.array([[3,2,1],
     [2,1,3],
     [1,3,1]])

def hessenberg_reduction(A):
    """
    Reduce a square matrix A to upper Hessenberg form.
    Returns (H, P) where H is the Hessenberg form and P is the transformation matrix.
    """
    A = np.array(A, dtype=float)
    n = A.shape[0]
    P = np.eye(n)  # Accumulates similarity transformations

    for k in range(n-2):
        # Step (i): Find the index of maximum element in column k below diagonal
        max_idx = k+1 + np.argmax(np.abs(A[k+1:, k]))

        # If maximum element is not zero and not already in desired position
        if A[max_idx, k] != 0 and max_idx != k+1:
            # Swap rows
            A[[k+1, max_idx], :] = A[[max_idx, k+1], :]
            # Swap columns
            A[:, [k+1, max_idx]] = A[:, [max_idx, k+1]]
            # Update transformation matrix
            P[:, [k+1, max_idx]] = P[:, [max_idx, k+1]]

        # Step (ii): Gaussian elimination to create zeros below subdiagonal
        if A[k+1, k] != 0:
            # Compute multipliers for elimination
            tau = A[k+2:, k] / A[k+1, k]
            # Create elimination matrix L
            L = np.eye(n)
            L[k+2:, k+1] = -tau
            # Apply similarity transformation
            A = L @ A @ np.linalg.inv(L)
            # Update transformation matrix
            P = P @ np.linalg.inv(L)

    return A, P

H, P = hessenberg_reduction(A)

print("Original matrix A:")
print(A)
print("\nHessenberg form H:")
print(H)

