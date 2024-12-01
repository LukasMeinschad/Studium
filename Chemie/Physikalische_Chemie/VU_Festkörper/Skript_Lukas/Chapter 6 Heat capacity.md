[[Chapter 5 Phonons]]
[[Chapter 4 Crystal Binding]]


> Law of Dulong-Petit $C = 3k_b$ per atom

This law holds well at room temperature with deviations at lower temperatues

### Einstein's model

> Equipartition theorem states that each atom can be modeled as a classical harmonic oscillator

Starting Point

+ Each atom is modeled as independent quantum harmonic oscillators
+ Each atom has the same frequency $\omega_0$ 

![[Pasted image 20241128211946.png]]

With eigenenergies $E_n = (n + 1/2)\hbar \omega_0$ 

The occupation number is given by the Bose-Einstein distribution:

$\langle n \rangle = n_B(\omega,T) = \frac{1}{e^{\hbar \omega / k_b T}-1}$ 

Resubstitution of this gives

$E(T) = \frac{\hbar \omega_0}{e^{\hbar \omega_0 / k_bT}-1} + 0.5 \hbar \omega_0$ 

![[Pasted image 20241128212229.png]]

Now one can simply derive the heat capacity per harmonic oscillator by the definition

$C(T) = \frac{dE(T)}{dT}$

![[Pasted image 20241128212350.png]]

> The Einstein Temperature is the temperature below which the thermal excitations of the quantum harmonic oscillator start to freeze out. i.e there is not enough thermal energy to excite the harmonic oscillator above the ground state

![[Pasted image 20241128212715.png]]

### Debye Model

![[Pasted image 20241128212907.png]]

> The low-temperature heat capacity of silver is underestimated by the Einstein model.

Debye considered the sound waves in a material as independent harmonic oscillators

#### Recap Sound wave

The displacement of an atom at position r and time t is described by

$\delta r = \delta r_0 e^{i(kr - \omega t)}$

Where $k= (k_x,k_y,k_z)$ is the wave vector the wavelength is related to the wavevector $k$ through $\lambda = 2\pi / |k|$ 

Thus the wave depends on tim only through the factor $e^{-i\omega t}$ and they are normal modes

A wave has three normal modes

+ Two transverse (perpendicular to $k$) and two longitudinal (parallel to $k$)

Waves are characterized by their frequency, wavevector and polarization. The frequency is related to the wavevector with the dispersion relation 

$\omega = v_s |k|$ 

The quantum excitations of harmonic osscilators are called phonons, the expected number of phonons in the oscillator at temperatur $T$ is given by the Bose-Einstein distribution. We now have $3N$ osciallators with frequencies depending on k through the dispersion relation

$\omega(k) = v_s |k|$ 

![[Pasted image 20241130085349.png]]

### Periodic Boundary Conditions

The heat capacity is a macroscopic property: it doesnt depend on the materials shape just on the volume

Let $V = L^3$ be a box with periodic boundary conditions

$\delta r(r + Lx) = \delta r(r)$

Substituting in the plane wave one gets

$\delta r_0 e^{i(k\cdot r + k_xL -\omega t)} = \delta r_0 e^{i(kr - \omega t)}$ 

In order to satisfy periodic boundary conditions $k_x = n_x \frac{2\pi}{L}$ damit ergeben sich die erlaubten werte für k als

$k = \frac{2\pi}{L}(n_x,n_y,n_z)$

![[Pasted image 20241130085652.png]]

> There is exactly one allowed $k$ value per $(\frac{2\pi}{L})^3$ consider with large box sizes $L \to \infty$ that the volume per allowed mode becomes smaller and smaller
> $\sum_k \approx \frac{L^3}{(2\pi)^3} \int dk$ 

With this approximation the total energy can be rewritten

![[Pasted image 20241130085910.png]]

Because through the dispersion relation we now that $\omega(k) = v_s |k|$ thus this is only dependent on the magnitude, we can rewrite the integral in spherical coordinates

![[Pasted image 20241130090016.png]]

![[Pasted image 20241130090025.png]]

This integral can be split into two parts, the factor in the brackets describes the average energy of a phonon mode with frequency $\omega$. The other factor is the density of states $g(\omega)$ 

> The density of states $g(\omega)$ counts the total number of available normal modes inside a frequency interval $\omega + d\omega$ 

![[Pasted image 20241130090333.png]]

The density of states thus is not dependend of the temperature, one can split the integral now into temperature dependent and independent parts

![[Pasted image 20241130090451.png]]

We can now see by calculating the derivative that 

$C = \frac{dE}{dT} \approx T^3$ 

+ At temperature T, only phonon modes with an energy below the thermal energy $E_T = k_bT$ become thermally excited. These modes have $\hbar \omega(k) \leq k_b T$ 

### Conclusions

+ The Debye model assumes atoms in a material move in a collective fashion, described by quantized normal modes with the dispersion relation $\omega = v_s |k$
+ The phonon modes have a constant density of $(L/2\pi)^3$ in the reciprocal k-space
+ The total energy and heat capactity are obtained via the integration
+ The density of states $g(\omega)$ is the number of states per frequency
+ At low temperature the phonon heat capacity is proportional to $T^3$ 

