
> The theory of lattice vibrations discussed thus far has been limited in the potential energy to terms quadratic in the interatomic displacements. This is the harmonic theory; the consequences are:

+ Two lattice waves do not interact; a single wave does not decay or change form with its time
+ There is no thermal expansion
+ Adiabatic and isothermal elastic constants are equal
+ The heat capacity becomes constant at high temperature

A nice demonstration of anharmonic effects are that the interaction of two phonons can produce a third phonon with frequency $\omega_3 = \omega_1 + \omega_2$ 

![[Pasted image 20241130091456.png]]

We develop the potential as a power series around the equilibrium position

$U(x) = V_0 + c\cdot x^2 - g \cdot x^3 - f\cdot x^4$ 

The term $x^3$ represents the Asymmetrie of the mutual repulsion of atoms. The term $x^4$ represents the softening of the vibration at large amplitudes.

The average displacement is calculated using the Boltzmann distribution function

![[Pasted image 20241130091804.png]]

Because the energy of the anharmonic terms is small in comparison of $k_BT$ we can expand this integral and calculate our thermal expansion

Consider for example the lattice constant of solid argon shown in this figure. The slope is proportional to the thermal expansion coefficient

![[Pasted image 20241130092004.png]]

### Thermal conductivity

> The thermal conductivity is defined with respect to the steady-state flow of head down a long rod with temperature gradient $dT/dx$
> $j_U = -K \frac{dT}{dx}$ 

with $j_U$ being the flux of the thermal energy, transmitted across a unit area per unit time

![[Pasted image 20241130092253.png]]

The thermal energy transfer is a random process. The energy does not simply enter one end of the specimen and proceed directly in a straight path to the other end, we have a random propagation

We now from the kinetic theory of gases

$K = 1/3 C v l$

+ C is the heat capacity per unit volume
+ $v$ is the average particle velocity
+ $l$ is the mean free path of a particle between collisions

Derivation

1. The flux of a particle in x direction $0.5 n \langle |v_x| \rangle$ where n is the concentration of molecules (brackets are average value)
2. If $c$ is the heat capacity if we move from $T + \Delta T$ the particle will take up energy $c \Delta T$
3. Now $\Delta T$ is with the free path $\Delta T = \frac{dT}{dx}v_x \tau$ with $\tau$ the average time between collisions

The net flux is $j_U = - n \langle v_x^2 \rangle c\tau \frac{dT}{dx}$ 

As for phonos $v$ is constant thus

$j_U = -\frac{1}{3}Cvl \frac{dT}{dx}$

### Thermal Resitivity of the Phonon Gas

> The phonon mean free path $l$ is determined by geometrical scattering and scattering by other phonons. If the forces were harmonic, there would be no mechanims for collisions between different phonons, the mean free path would be limited solely by the collisions of a phonon wit the crystal boundary

The theory of the anharmonic coupling predicts that $l$ is proportional to 1/T at high temperatures.

> In order to define a thermal conductivity there must exist mechanisms in the crystal whereby the distribution of phonons may be brought locally into thermal equilibrium.

+ Phonon collisions only with static imperfection or a crystal boundary will not establish thermal equilibrium

consider for example a three phonon collision process $K_1 + K_2 = K_3$ 

![[Pasted image 20241130093453.png]]

### Umklapp Processes

> The important three-phonon processes that cause thermal resisivity are not of the form $K_1+K_2 = K_3$ in which $K$ is conserved but $K_1 +. K_2 = K_3 +G$ where G is a reciprocal lattice vector

By now we have seen examples of wave interactions where the total wavevector change is equal to a reciprocal lattice vector, these are always possible in reciprocal lattices.

![[Pasted image 20241130094748.png]]