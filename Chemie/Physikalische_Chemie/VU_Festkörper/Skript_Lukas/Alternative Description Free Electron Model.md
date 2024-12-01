
## Drude Model

### Starting Point Ohms law

> Ohms law is a empirical observation of conductors, which states that voltage is proportional to the current $V=IR$ 


Consider a wire with cross-section $A$ length $l$ we have resistance $R = \rho l/A$ where $\rho$ is a material dependent resistivity.

A applied voltage $V$ creates an electric field $E$

thus $V = I \rho \frac{l}{A} \Rightarrow E = \rho j$ 

### Drude Model assumptions

+ Electrons scatter randomly at uncorrelated times, average time between scattering is $\tau$
+ After each scattering event the momentum randomized with a zero average $\langle r \rangle = 0$
+ Electrons are charged particle with $-e$ thus the Lorenz Force applies $F_L = -e(E + v \times B)$ 

### Goal is now to find electric current density $j$ 

A electron with charge $-e$ and velocity $v$ carries current $-ev$ when the electron density is $n$ the average current they carry is $-ne \langle v \rangle$ 

For convenience now v is the average.

In a fraction $dt$ when the electrons scatter there average velocity is zero

$mv(t + dt) = 0$ then the rest is accelerated by a Lorenz force

$mv(t +dt) = mv(t) + Fdt$ 

![[Pasted image 20241201112310.png]]

### Sommerfeld model

The Debye model studied the physical behavior of phonons. Sommerfeld considered the electrons as free particles not interacting with atomic nuclei

We have a cubic box $L \times L \times L$ with periodic boundaries. the solution to Schördingers equation for free particles are

$\psi \propto \exp(ikr)$ where $k$ is the electrons wave vector with values

$(k_x,k_y,k_z)= \frac{2\pi}{L}(n_x,n_y,n_u)$ because of periodic boundary conditions

The eigenenergies are given by the dispersion relation

$\epsilon(k) = \frac{\hbar^2 k^2}{2m}$ 

![[Pasted image 20241201113603.png]]

each dot represents the electron state

### Comparison of electrons and phonons

What we can see because electrons are fermions the occupation of states is described by the fermi dirac equation

$n_F (\beta (\epsilon - \mu)) = \frac{1}{e^{\beta (\epsilon-\mu)}+1}$ 

The chemical potential $\mu$ is the characteristic energy above which $n_F$ goes to zero

![[Pasted image 20241201113811.png]]

We can get the states when integrating over the occupied states

![[Pasted image 20241201113836.png]]


### Fermi Sea, Energy Surface, wavevector and wavelength

At $T=0$ the Fermi-Dirac distribution is a step function

$n_F(\beta(\epsilon - \mu)) = \Theta ( - (\epsilon - \epsilon_f))$ 

All energy states lower than the fermi energy are occupied this can be visualized with the k states inside a sphere

![[Pasted image 20241201114207.png]]

> This can be described as a see: Electron occupy a finite are in reciprocal space, starting from deepest lowest energy points all the way up to the Fermi-level. The border of this Fermi sea is the Fermi Surface

![[Pasted image 20241201114317.png]]

We now

$v_F = \frac{\hbar k_F}{m}$ 

![[Pasted image 20241201114411.png]]

### Electron heat capacity


Compare the ocupied states at $T =0$ in blue and the occupied states at $T>0$ orange shade

![[Pasted image 20241201114521.png]]

At a finite Temperature only the electrons occupying the top triangle blue become thermally excited thus the number of excited electrons is

$N_{exc} \approx g(\epsilon_F)k_B T$ 

and $C_e  \propto T$ 

> Only particles withing a range $k_B$ T to the Fermi energy become thermally excited each carries then a extra energy $k_BT$ 




