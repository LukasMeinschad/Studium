"""
Gershgorin's Theorem gives us bounds of the locations of eigenvlues of an arbitrary square complex matrix

These eigenvalues are contained in Disks, known as Gershgorin Disks centered on the diagonal elements of the matrix

The radius of the disks is the sum of the absolute values of the elements of the k-th row
"""

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(202103014)

N = 5 # dimension of the matrix

D= np.diag([0,3+ 1j, 4+ 1j, 1+5j, 9+2j])
M = np.random.rand(N,N) + D # Add Random Noise to the Diagonal Matrix

R = np.zeros(N) # initialise disk-radii

for i in range(N):
    R[i] = sum(abs(M[i,:]) - abs(M[i,i]))

eigenvalues = np.linalg.eigvals(M)

fig,ax = plt.subplots()
for k in range(N):
    x,y = M[k,k].real, M[k,k].imag
    ax.add_artist(plt.Circle((x,y), R[k],alpha=0.5))
    plt.plot(eigenvalues[k].real,eigenvalues[k].imag,"k+")

ax.axis([-4,12.5,-4,9])
ax.set_aspect(1)

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.title("Gershgorin disks and eigenvalues $x + iy$")
plt.show()
