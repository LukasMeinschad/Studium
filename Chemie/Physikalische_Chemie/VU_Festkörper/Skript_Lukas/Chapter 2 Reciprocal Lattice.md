[[Chapter 1 Crystal Systems]]

### Index System for Crystal Planes

The orientation of a crystal plane is determined by three points in the plane. In order to specify these planes we can use the **Miller Indices**

1. Find the intercepts on the axes in terms of the lattice constants $a_1,a_2,a_3$
2. Take this intercepts into fractional co-oordinates, divide through the lattice parameters
3. Finally take the reciprocal and then specify the numbers

![[Pasted image 20241128150011.png]]

### The Bragg Law

> The crystal structure is studied through the diffraction of photons, neutrons and electrons. The diffraction depends on the crystal structure and on the wavelength.

Consider Braggs Law, that each incident wave is reflected specularly from parallel planes of atoms in the crystal

$2d \sin \theta = n \lambda$ 

![[Pasted image 20241128151239.png]]

### Fourier Analysis

A crystal in general is invariant under translation

$T = u_1a_1 + u_2a_2 + u_3a_3$

The electron density $n(r)$ is a periodic function thus

$n(r + T) = n(r)$

Because of the periodicity we can use Fourier analysis. Consider a function $n(x)$ in one dimension this can be described as a fourier series

![[Pasted image 20241128152046.png]]

Ist in general convenient to rewrite this Fourier series in the compact form

>$n(x) = \sum_p n_p \exp(i2\pi px / a)$ 

To extend this Fourier analysis to periodic functions $n(r)$ in three dimension we find vectors

$n(r) = \sum_G n_G \exp(iG \cdot r)$

In general one can describe the Fourier transformation as

$𝑓(𝑥) = \int_{-\infty}^{\infty}f(x)e^{2\pi ikx}dk$ 

![[Pasted image 20241128152448.png]]


### Reciprocal lattice vectors

In general one can construct the reciprocal lattice with the following formula

![[Pasted image 20241128152656.png]]

Here $b_1,b_2,b_3$ are the primitive vectors of the reciprocal lattice

We have a orthogonality property $b_i \cdot a_j = 2 \pi \delta_{ij}$ 

Points in the reciprocal lattice are a set of vectors with

$G = v_1 b_1 + v_2 b_2 + v_3 b_3$

The vectors in the Fourier series then are just reciprocal lattice vectors

> Each an every crystal structure has two lattices associated with it, the crystal lattice and the reciprocal lattice

Vectors in the direct lattice have the dimensions of (length); vectors in the reciprocal lattice have the dimension of (1/length). The reciprocal lattice is a lattice in the Fourier space associated with the crystal.

### Diffraction Condition

![[Pasted image 20241128153225.png]]

We see the difference in phase vectors is

$\exp[i(k-k')*r]$ between the beams scattered from the volume elements r apart.

The total scattering amplitude can be evaluated with the integral over the crystal of $dV$ 

Thus $F =  \int dV n(r) \exp(-i \Delta k \cdot r)$ 

with $k + \Delta k = k'$ this is the scattering vector $\Delta k'$ 

By introducing the Fourier series into the integral

$F = \sum_G \int dV n_G \exp[i(G - \Delta k)\cdot r]$ 

When the scattering vector $\Delta k$ is equal to a reciprocal lattice vector the $\Delta k = G$ this exponential vanishes.

It is then very simple to show that F is very small when $\Delta k$ differs from the reciprocal lattice vector

> Laue condition for diffraction $k - k' = G$ 


![[Pasted image 20241128154713.png]]


### Laue Condition 

> $k - k' = G$ is the conservation of crystal momentum 


Crystal momentum can be described as the combined momentum of crystal and electron. For elastic scattering, when the particle leaves the sample: $|k| = |k'|$ due to conservation of energy.

![[Pasted image 20241128193236.png]]


### X-Ray and Neutron Diffraction

Since neutrons are uncharged, they scatter almost exclusively from nuclei via the nuclear forces. As a result the scattering potential is extremely short ranged, and can be well approximated as a delta function

$V(x) = \sum_{j} f_j \delta(x-x_j)$ 

Where $f_i$ is the form factor and represents the strenght of scatterng from that particular nucleus. For neutrons it is proportional to the "nuclear scattering length" $b_i$ 

![[Pasted image 20241128193557.png]]

X-Rays scatter from the electrons in the material here $V(x) is proportional to the electron density

$V(x) = \sum_j Z_j g_j(x-x_j)$ 

![[Pasted image 20241128193704.png]]

+ X-Rays scatter from heavy atoms and hardly from light atoms, difficult to distinguish atoms that are very close to each other in their atomic number
+ The nuclear scattering length varies erratically with atomic number, hydrogen scatters well so it is easy to detect.

### Ewald Sphere


Now we now the Laue condition $k_{in} - k_{out} = G$ and the elastic scattering $|k_{in}| = |k_{out}|$, the Ewald sphere is the graphical translation of the Laue condition: wave vector difference = reciprocal lattice vector.

In general the Laue condition here is satisfied if a point lies on the Ewald Sphere

![[Pasted image 20241128194247.png]]

### The Laue Method

> Incident X-Ray beam is non monochromatic and contains all the wavelength that potentially satisfiy construtive interference

$k_{min} < k_{in} < k_{max}$ 

Since there are different k vectors, there are many Ewald spheres

![[Pasted image 20241128194604.png]]

+ Main application is the detection of high symmetry directions, the diffraction pattern then gets symmetric with an exact orientation of the single crystal

### Debye Scherrer Method

> This is generally known as powder diffraction, is the use of wave scattering on a sample which is not single crystalline but is powdered

The reciprocal lattice points lie with equal probability on a sphere around the origin. The intensities come only from the small fraction of crystallites which happen to be "right for this diffraction reflex"

![[Pasted image 20241128195232.png]]
