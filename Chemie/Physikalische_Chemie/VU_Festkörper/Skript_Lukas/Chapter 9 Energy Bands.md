
![[Pasted image 20241130110719.png]]

Free electron model gives insight into heat capacity, thermal conductivity, electrical conductivity and electrodynamics of metals but fails to draw distinction between metals, semimetals, semiconductors and insulators

+ Electrons in crystals are arranges in energy bands, seperated regions are called band gap
+ Insulator: Energy bands are either filled or empty
+ Metal: one or more bands are partially filled
+ Semiconductor: one or two bands filled slightly

### Nearly Free electron model

![[Pasted image 20241130111040.png]]

+ In the nearly free electron model the band electrons are only perturbed weakly by the periodic potential of the ion cores

We now that $E_k = \frac{\hbar^2}{2m}(k_x^2 + k_y^2 + k_z^2)$ 

with periodic boundary conditions $k_x,k_y,k_z = 0; \frac{2\pi}{L}...$ 

and free electron wave functions of the form $\psi_k(r) = \exp(ikr)$ 

> Bragg reflection is a characteristic feature of wave propagation in crystals. Bragg reflection of electron waves in crystals is the cause of band gaps as the solutions of the SG dont exist

![[Pasted image 20241130111318.png]]

The Bragg conditon $(k + G)^2 = k^2$ for a diffraction in one dimension is

> $k = ± 0.5 G = \frac{n\pi}{a}$ 

Here G is a reciprocal latticed vector, the first gap occurs at $k= ± \pi/a$ which is the first Brillouin zone of the lattice

The wavefunctions at this special k values are made up of equal parts of traveling plane waves to the left and right. Thus we can represent this as standing waves

one can form two standing waves from the two traveling waves

![[Pasted image 20241130111733.png]]

### Origin of the Energy Gap

> The two standing waves $\psi_+$ and $\psi_-$ pile up electrons at different regions, therefore have different values of the potential energy in the field of the ions of the lattice. This is the origin of the band gap. The probability density $\rho = \psi^* \psi = |\psi|^2$ 

For a traveling wave this is one and the charge density is constant (as is also clear in this free electron picture). For a standing wave one gets

![[Pasted image 20241130111929.png]]

![[Pasted image 20241130111939.png]]

so $\psi_+$ puts electron density to the cores, $\psi_-$ away from the cores.

Thus we have an energy gap of $E_g$ if the energies of $\rho_-$ and $\rho_+$ differ by $E_g$

![[Pasted image 20241130112120.png]]

### Bloch Functions

The solutions of the Schrödinger equation for a periodic potential must be of special form:

$\psi_k(r) = u_k(r)\exp(ikr)$ 

Where $u_k(r)$ has the period of the crystal lattice with $u_k(r) = u_k(r+T)$ with $T$ a translation vector of the lattice

> Eigenfunctions of the wave equation for a periodic potential are the product of a plane wave $\exp(ikr)$ times a function $u_k(r)$ with the periodicity of the lattice


#### Small and not concise proof of Blochs Theorem

Let $\psi_k$ be nondegenerate, we consider $N$ identical lattice points on a ring of length $Na$ the potential energy is thus periodic

$U(x) = U(x + sa)$ we look for solutions $\psi(x + a) = C \psi(x)$ 

When going around the ring we now $\psi(x+Na) = \psi(x) = C^n\psi(x)$ 

thus $\psi(x)$ is single valued and $C$ are the N roots of unity

$C = \exp(i2\pi s/N)$  

### Kronig-Penney Model

> A periodic potential for which the SG can be solved is a array of square wells

![[Pasted image 20241130112726.png]]


![[Pasted image 20241130112750.png]]

![[Pasted image 20241130112855.png]]

+ So we now inside the square well we have a solution which is a linear combination of eigenfunctions
+ Outside the well the solution is still nonzero this is because of the quantum tunneling effect
+ The solutions should all satisfy Blochs Theorem because the potential is periodic
+ Because we have continuity of our function at boundaries we can set them equal and derive the lowest formula

By some further simplification we can see

$(\frac{P}{ka})sin(Ka) + cos(Ka) = cos(ka)$

where the right side is bounded by the values of the cosine

> What is to note here is that the values of Ka where the solution doesn't exist are the band gap

![[Pasted image 20241130113543.png]]

### Empty lattice approximation

> The empty lattice model elucidates various aspects of energy dispersion relations in solids, pertaining a non-interacing free electron in the crystal

When the wave vectors are outside the first Brillouin zone they are carried back into the first zone via the substraction of a appropiate reciprocal lattice vector

$k' + G = k$

![[Pasted image 20241130113807.png]]

### Number of Orbitals in a Band

Consider first a linear crystal constructed of an even number of $N$ with primitive cells of lattice constant $a$ the allowed values of the electron wavevector in the first Brillouin zone are given by

$k = 0; \frac{2\pi}{L} ...$

we cut the series ar $N\pi/l = \pi/a$ which is the zone boundary

> Each primitive cell contributes exactly one independent value of k to each energy band. This result also carries over to 3 Dimensions

> There are 2N independent orbitals in each energy band.

+ If there is a single atom of valance then the band is half filled with electrons
+ If the atom contributes two valence electrons to the band, the band can be exactly filled.

![[Pasted image 20241130114153.png]]

![[Pasted image 20241130114220.png]]

> If the valence electrons fill one or more bands, leaving others empty the crystal will be an insulator

A crystal can be an insulator only if the number of valence electrons in a primitive cell of the crystal is a even integer

+ Alkali metals and noble metals have one valence electron per primitivwe cell so they have to be metals
+ Alkaline earth metals have two valance electrons per primitive cell, they could be insulators, but the band overlaps in energy to give metals
+ Diamond Silicon and germanium have two atoms of valence four, thus eight valence electrons per primitive cell, the bands do not overlap giving a pure crystal

![[Pasted image 20241130114532.png]]


### Tight Binding Model

![[Pasted image 20241130120758.png]]

+ The electronic structure of a crystalline solid may be considfered in terms of linear combinatons of atomic orbitals (LCAO) centered on the constitutend atoms
+ The energy band structure of this system is derived from the atomic orbital levels of seperated atoms

Consider first two neutral seperated atoms, the charge distributions then overlap if the atoms are brought together. For example two electrons in the 1s ground state

![[Pasted image 20241130121011.png]]

![[Pasted image 20241130121025.png]]

