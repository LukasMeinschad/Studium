
> According to the free electron model the valence electrons of atoms become conduction electrons and move freely through the volume of the metal

Simple metals are the alkali metals, lithium, sodium postassium. Consider for example sodium the valence electron is a 3s state, thus we have a 3s conduction band

![[Pasted image 20241130095150.png]]

Why is condensed matter so transparent to conduction electrons:

+ The conduction electron is not deflected by ion cores arranged on a periodic lattice, because matter waves can propagate freely in a periodic structure
+ The conduction electron is only scattered infrequently by other electrons due to the Pauli exclusion principle

### Energy Levels in One Dimension

The electron of mass $m$ is confined to a lenght $L$ by infinite barriers. The wavefunction $\psi_n(x)$ is a solution of the Schrödinger equation $H \psi = E \psi$ 

So we have $H \psi_n = -\frac{\hbar^2}{2m} \frac{d^2\psi_n}{dx^2} = E_n \psi_n$

An orbital is denoted as a solution of this equation, we can assign N electrons to N different orbitals, this model is only exact if there is no interaction between electrons

![[Pasted image 20241130095712.png]]

> According to the Pauli exclusion principle, no two electrons can have all their quantum number identical

In a linear solid we have $n$ Hauptquantenzahl and $m_s$ as the magnetic quantum number; the number of orbitals with the same energy is called degeneracy

![[Pasted image 20241130095845.png]]

> The Fermi energy $E_F$ is defined as the energy of the topmost filled level in the ground state of a N electron system

![[Pasted image 20241130100013.png]]

### Effect of Temperature on the Fermi-Dirac Distribution 

> The Fermi-Dirac distribution gives the probability that an orbital at energy $E$ will be occupied in an ideal electron gas in thermal equilibrium

$f(E) = \frac{1}{\exp[(E- \mu)/(k_BT)+1]}$ 

![[Pasted image 20241130100218.png]]

### Free Electron Gas in Three Dimensions

![[Pasted image 20241130100535.png]]

If we next require the wavefunctions to be periodic in $x,y,z$ with period $L$ thus,

$\psi(x + L, y,z) = \psi(x,y,z)$ we can describe our solution as a traveling plane wave

$\psi_k = \exp(ikr)$, with the wavevector satisfying the periodic boundary conditions $k_x = 0; ±\frac{2\pi}{L} ...$ 

For the energy we get

$E_K = \frac{\hbar^2}{2m}(k_x^2 + k_y^2 +k_z^2)$ 

The magnitude of the wavevector being $|k| = \frac{2\pi}{\lambda}$ 

The ground state of $N$ free electrons, the occupied orbitals may be represented as points in a sphere in $k$ space. The energy surface of the sphere is the Fermi energy, (highest occupied energy)

![[Pasted image 20241130101056.png]]

With the surface $E_F = \frac{\hbar^2}{2m}k_F^2$ 


![[Pasted image 20241130101145.png]]


Now we find an expression for the number of orbitals per unit energy range $D(E)$ called the density of states

We now the number of orbitals of energy $\leq E$:

$N.= \frac{V}{3\pi^2}(\frac{2mE}{\hbar^2})^{3/2}$ 

thus the density of states

![[Pasted image 20241130101346.png]]

So we can calculate how many electron levels there are at a given energy.

### Heat Capacity of the electron gas

> A question that proposed difficulties in the development of this theory is the heat capacity of the conduction electrons.

+ Classical statistical mechanics predics a free particle has heat capacity of $\frac{3}{2}k_b$ where $k_b$ is the Boltzmann constant. Then we should in total get $3/2 Nk_b$ which is just not the case

> When one heats the specimen from absolute zero not every electron gains $k_BT$ as expected, the electrons in orbitals within an energy range of $k_BT$ to the Fermi level are excited therminaly. Thus only a fractuin $T/T_F$ can be excited

![[Pasted image 20241130101858.png]]

The total electronic thermal energy $U_{el} \approx (NT/T_F)k_bT$ 

thus $C_el \approx \delta U / \delta T \approx  N k_b (T/T_F)$ 

#### Derivation of a quantiative epxression of electronic heat capacities at low volume

![[Pasted image 20241130102237.png]]

![[Pasted image 20241130102327.png]]

![[Pasted image 20241130102354.png]]


> Conclusion: The actual heat capacities are much smaller than the classical ones, this is dou to the Fermi statistics, only the particles near $E_F$ are excited in this model.

### Experimental Heat Capacity of Metals

At low temperatures below the Debye Temperature $\theta$ the Fermi temperature $T_F$ may be written as a sum of electron and phonon contributions $C = \gamma T + AT^3$ with $\gamma$ and $A$ constants of the material. The electronic term is linear and dominant at low temperatures.

The $AT^3$ comes from the Debye model.

### Electrical Conductivity and Ohms law

The momentum of a free electron is related to the wavevector by $mv = \hbar k$ Newtons second law of motion gives us the force

![[Pasted image 20241130102831.png]]

In absence of collisions the Fermi sphere moves in k space at uniform rate by a constant when an electric field is applied

The electrical conductivity is defined by $j = \sigma E$ so by 

$\sigma = \frac{ne^2 \tau}{m}$ 

The electrical resitivity is defined as the reciprocal of the conductivity so

$\rho = m/ne^2 \tau$


![[Pasted image 20241130103211.png]]

+ The Fermi sphere does not accelarate indefinitely, because electrons do scatter with lattice imperfections, impurities or phonons.

### Summary of the Free Electron Fermi Gas

+ Assumption: The conduction electrons feel no potential differences in the metal, uncorrelated motion of electrons
+ The infrequent scattering of a electron with other conduction electrons is due to the Pauli exclusion principle
+ The Densitiy of sates is the number of states with energy $dE$ per Volume and energy interval $dE$
+ The total heat capacity of a solid is $c_V = \gamma T + \beta T^3$ 
+ The electronic head capacity dominates at $T \to 0$
+ Due to collisions of the electron with impurities, latice defects and phonons, the electrons are maintained in a steady state upon application of an electric field

$j = n_e \delta v_{drift}(-e) = \sigma E$ (Ohms law)