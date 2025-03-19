[[Chapter 2 Reciprocal Lattice]]
[[Chapter 1 Crystal Systems]]

> The attractive electrostatic interaction between the negative charges of the electrons and the positive charges of the nuclei is responsible for the cohesion of solids

Determining why atoms stick together to form solids is finding the solution to a many particle Schrödinger equation

$H \psi = E \psi$ 

![[Pasted image 20241128195624.png]]

### Ionic Crystals

Ionic crystals are made up of positive and negative ions, this bond results from the electrostatic interaction of oppositely charges ions. 

+ Ionization Energy (IE) = Energy required to remove one electron from a neutral atom to create a positive ion
+ Electron affinity (EA) = Energy gain for creating a negative Ion

![[Pasted image 20241128195910.png]]

The long range interaction between ions with charge $q$ is the electrostatic interaction

$± q / 4 \pi \epsilon_0 r$ 

Ions arrange themselves in whatever crystal structure gives the strongest attractive interaction compatible with the repulsive interaction at short distances between ion cores.

> The main contribution to the binding energy of ionic crystals is electrostatic and called Madelung energy

If $U_{ij}$ is interaction between i and j the sum $U_i$ of all interactions

$U_I = \sum_j U_{ij}$ 

This can be written as coloumb potential

$U_{ij} = \lambda \exp(-r_{ij}/\rho) ± \frac{q^2}{4\pi \epsilon_0 r_{ij}}$ 


![[Pasted image 20241128200527.png]]

The total lattice energy $U_{tot} = N U_i$ describes the energy needed to seperate a crystal into individual ions.

Include the repulsive interaction only agains nearest neighbors:

![[Pasted image 20241128200702.png]]

For stable crystal this Madelung constant needs to be positive.

![[Pasted image 20241128200811.png]]

#### Further descriptions

![[Pasted image 20241201102658.png]]

This figure shows the Coloumbic Madelung energy and the repulsive interactions. One can see the total energy as a sum of both the interactions.


So what does the Madelung constant tell us

$\lambda = \sum_{j \neq i } \frac{±}{p_{ij}}$ 

This is used to determine the electrostatic potential of a single ion in a crystal by approximating the ions by point charges
### Covalent Crystals

> The covalent bond is a strong bond, usually formed from two electrons, these tend to be partially localized in the region between the two atoms, the spin is antiparallel.


#### Particle in a box picture

Modeling a hydrogen atom as a box of size L the energy is

$E = \frac{\hbar^2 \pi^2 }{2 m L^2}$ 

When the electron is shared it is delocalized over two position, thus in a box size of $2L$

$E_{bonding} = \frac{\hbar^2 \pi^2}{2m(2L)^2}$ 

The new ground state orbital is known as the bonding orbital.

![[Pasted image 20241201103017.png]]

> It is important by the Pauli-Principle that the electrons in the bonding orbital differ in spin

#### Why does no covalent $He_2$ exist?

In a $He$ each atom has two electrons, thus two of the four electrons must occupy a excited anti-bonding orbital having the same energy as the original ground state of the atoms. So there is no net energy gain

![[Pasted image 20241201103215.png]]



#### Molecular Orbital or Tight binding theory

For this we fix the nuclear positions with the Born-Oppenheimer approximation and consider the Hamiltonian for two H atoms or $H_2^+$ for a single electron

$H = K + V_1 + V_2$ with $K = \frac{p^2}{2m}$ and $V_i = \frac{e^2}{4\pi \epsilon_0 R |r-R_i|}$ 

![[Pasted image 20241128201709.png]]

Next let $|1 \rangle$ and $|2 \rangle$ be orthonormal $\langle i | j \rangle = \delta_{ij}$ 

![[Pasted image 20241128201836.png]]

Important is that you have $V_cross$ as a coloumb integral, this is the potential orbital $|1\rangle$ or $|2\rangle$ felt by the other nucles

And the $t$ is the Hopping term, exchange integral.

![[Pasted image 20241128201945.png]]

> Through this Exchange term $t$ the electron is able to hop between orbitals

One then gets two eigenstates for this wave function

![[Pasted image 20241128202236.png]]

### Van der Waals Forces

> Also for example noble gases can interact with each other, both atoms have a dipole moment, which may be zero but can fluctuate momentarily due to quantum mechanics

The first the induces a dipole to the second one.

![[Pasted image 20241128202414.png]]

If there is a electric field applied to an atom it will develop a polarization, the electron will be more likely located on one side of the nucleus

$p = \chi E$ 

Suppose now one electron has a momentarily induced dipole momentum $p_1$ then the second atom will experience an electric field:

$E = \frac{p_1}{4\pi \epsilon_0 r^3}$ 