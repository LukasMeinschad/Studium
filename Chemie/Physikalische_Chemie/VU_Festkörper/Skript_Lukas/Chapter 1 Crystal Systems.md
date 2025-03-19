
> An ideal crystal is constructed by infinite repetition of identical groups of atoms.

+ A group is called the basis
+ The set of mathematical points to which the basis is attached is called the lattice. 

Representation in 3D is through three dimensional translation vectors $a_1,a_2,a_3$ 

$R = n_1a_1 + n_2a_2 + n_3a_3$ 

![[Pasted image 20241128141603.png]]

+ A lattice is called primitive if it only contains one single lattice point

### Basis of a Crystal structure

> The basis of the crystal structure can be identified once the crystal axes have been chosen

![[Pasted image 20241128141928.png]]

to every point of the space lattice the basis then gets added this is our crystal structure


### Differences between unit cells

+ Unit cell: a repeating unit in a crystal
	+ Primitive unit cell: a unit cell containing only a single lattice point
	+ Conventional unit cell: A unit cell with more than one lattice point often used for more easier calculations
	+ Wigner-Seitz Cell: A construction to yield a primitive unit cell
### Wigner-Seitz cell

>A Wigner–Seitz cell is an example of a [primitive cell](https://en.wikipedia.org/wiki/Primitive_cell "Primitive cell"), which is a [unit cell](https://en.wikipedia.org/wiki/Unit_cell "Unit cell") containing exactly one lattice point. For any given lattice, there are an infinite number of possible primitive cells. However there is only one Wigner–Seitz cell for any given lattice. It is the [locus](https://en.wikipedia.org/wiki/Locus_(mathematics) "Locus (mathematics)") of points in space that are closer to that lattice point than to any of the other lattice points.

![[Pasted image 20241128142102.png]]

The algorithm for constructing a Wigner Seitz Cell

![[Pasted image 20241128142227.png]]

### Fundamental Types of Lattices

> Crystal lattices can be carried or mapped into themselves by the lattice translations T and by various symmetry operations.

Lattices can be found such that one, two, three, four and sixfold rotations carry the lattice into itself, $2\pi, 2\pi/2 ..$ 

Answer to question why no fivefold rotation exists

![[Pasted image 20241128142751.png]]

because we cannot fill the whole space with pentagons!

### Two dimensional lattice types

In order to make 2D lattices invariant unter symmetry operations $2\pi/3,2\pi/4,2\pi/6$ we have to apply restrictions, this lead to special lattice types.

![[Pasted image 20241128143738.png]]

### Three dimensional lattice types

> The ppint symmetry groups in three dimension require the 14 different lattice types listed in the following table

![[Pasted image 20241128143822.png]]

The cubic cell has three lattices:
+ Simple cubic (sc)
+ Body centered cubic (bcc)
+ face centered cubic (fcc)

#### Simple cubic

The simple cubic system is rare because it is an inefficient way to pack the spheres together

+ 1 lattice point per unit cell and a area of $a^3$ 
+ The number of nearest neighbors: 6
+ Packing fraction = $\pi /6 = 0.52$

![[Pasted image 20241128144130.png]]

#### Body centered cubic

The body centered cubic is a simple cubic with an additional cell in the center of the cube

+ 2 lattice point per unit cell with volume $a^3/2$ 
+ Number of nearest neighbours: 8
+ Nearest neighbour distance = 0.866a
+ Packing fraction = $\sqrt{3} \pi / 8 = 0.68

Primitive lattice is defined by the three translation vectors

+ $a_1 = 0.5 * (x+y-z)$ 
+ $a_2 = 0.5 * (-x+y+z)$
+ $a_3 = 0.5 *(x - y + z)$ 

![[Pasted image 20241128144459.png]]

### Face centered cubic

Simple cubic lattice with an additional point on the center of each plane

+ fcc has 4 lattice points per unit cell with a volume of $a^3/4$
+ Number of nearest neighbours = 12
+ Nearest neighbour distance = 0.707a
+ Packing fraction = $\sqrt{2} \pi / 6 \approx 0.74$ 

![[Pasted image 20241128144810.png]]

Thus we can define the translation vectors:

+ $a_1 = 0.5 * (x+ y)$
+ $a_2 = 0.5*(y+ z)$
+ $a_3 = 0.5*(x+z)$ 

### Sphere packing

> In euclidean space, the densest packing of equal spheres is achieved by a family of structures called close packed structures.

![[Pasted image 20241128145138.png]]

Thus the face centered cubic is build up by the ABCABC sequence and the ABAB structure gives the HCP

The packing fraction in this case is 0.74




