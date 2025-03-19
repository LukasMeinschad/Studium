[[Chapter 4 Crystal Binding]]
[[Chapter 2 Reciprocal Lattice]]
[[Chapter 1 Crystal Systems]]


> A phonon is the elementary excitation of vibrations in a crystal lattice, or the quantum unit of a crystal lattice vibration.

For these phonons we have energy $\hbar \omega$ as a excitation quantum of the lattice vibrational mode with frequency $\omega$

Phonons are not localized quasiparticles, but wavepackages can be fairly localized by combining modes of slightly different frequency

Like photons, phonons are bosons and not conserved thus can be created or destroyed

![[Pasted image 20241128203608.png]]


+ Taking three phonon modes: one longitudinal and two transversal

We assume the response of the crystal to be a linear function of the forces (Hooke's Law:)

$F_s = C(u_{s+1}-u_s) + C(u_{s-1}-u_s)$ where $C$ is the force constant between the nearest-neighbors.

Equation of motion:

$M\frac{d^2 u_s}{dt^2} = C(u_{s+1}-u_{s-1}-2u_s)$ 

Then we look for a time oscillatory solution

$-M\omega^2 u_s = C(u_{s+1}+u_{s-1}-2u_s)$ 

> A normal mode is defined as a collective oscillation where all particles move at the same frequency

![[Pasted image 20241128203921.png]]

> Central here is the dispersion relation

+ One can see that the slope of $\omega(K)$ is zero at the BZ boundaries: $\sin(\pi /2)$ 

![[Pasted image 20241128204021.png]]

#### The First Brillouin Zone

What range of K is physically significant for elastic waves? Only those in the first Brillouin zone.

 The ratio of displacements of two successive planes is given by:

$\frac{u_{s+1}}{u_s} = \exp(iKa)$ 

The range of independent values of K is specified by

$-\frac{\pi}{a} < K \leq \frac{\pi}{a}$ 

At the boundaries of the first Brillouin zone the solution represents a standing wave

![[Pasted image 20241128205011.png]]

#### Group Velocity:

The transmission velocity of a wave packet is the group velocity given as

$v_g = d\omega / dK$ 

which is $v_g = (Ca^2 / M)^{1/2}\cos(1/2 Ka)$ 

this is zero at the boundary zone

![[Pasted image 20241128205137.png]]

### Two Atoms per Basis

In crystals with more atoms per primitive cell, additional phonon modes are presents:

+ acoustical (A): the atoms move toghether
+ optical (O): the adjacent atoms move against each other

![[Pasted image 20241128205634.png]]

If there are $p$ atoms then there are $3p$ branches, 3 acoustical branches and (3p-3) optical branches.

![[Pasted image 20241128205803.png]]

Consider waves propagating in a symmetry direction of the crystal and only nearest-neighbor interactions

Then one equation of motions for the two type of ions:

![[Pasted image 20241128205848.png]]

Through some matrix shit one can then find the phonon dispersion relation for this quadratic equation

![[Pasted image 20241128205932.png]]

![[Pasted image 20241128205949.png]]

Just as a general outline of this topic it is somewhat complicated:

> Acoustic phonons are coherent movements of atoms of the lattice out of their equilibirium positions. Displacment perpendicular to the propagation direction is comparable to waves on a string. If the wavelength of acoustic phonons goes to infinity, this corresponds to the simple displacement of the whole crystal

> Optical phonons are out-of-phase movements of the atoms in the lattice, this occurs it if the lattice basis consists of two or more atoms, it is called optical because it can create a  electrical polarization.