Device based semiconductors include transistors, switches, diodes, photovoltaic cells, detectors and thermistors

In general one can classify them by their electrical resistivity at room temperature $10^{-2}$ to $10^9$ ohm-cm

+ AB with A trivalent, B pentavalent are III-V for example Ga As
+ AB with A divalent, B hexavalent II-VI zb Zn S, Cd S

> A highly purified semiconductor exhibits intrinsic conductivity as distinguished from the impurity conductivity of less pure speciman

In the intrinsic temperature range the electrical properties of a semiconductor are not modified by impurities in the crystal

![[Pasted image 20241130143812.png]]

+ Band gab is the difference in energy between the valance band and the conduction band
+ The highest point in the valance band is called valance band edge
.
### Band Gap

The conductivity and intrinsic carrier concentrations are controlled by $E_g/k_BT$ the ratio of the band gap to the temperature. If the ratio is large, then the carriers are low and vice versa

![[Pasted image 20241130144014.png]]

### Holes

The properties of vacant orbitals in an otherwise filled band are important in semiconductor physics and in solit state electronics. A hole acts in applied electric and magnetic fields as if it has a positive charge +e


![[Pasted image 20241130144427.png]]

![[Pasted image 20241130144625.png]]



1.  $k_h = -k_e$ 

The wavevector of the electrons in the filled band is zero $\sum k = 0$ this sums over all states in the Brillouin zone. This has inversion symmetry, if the band is filled by all pairs of orbitals $k$, also $-k$ is filled then the total wavevector is zero. When one electron is now missing $k_e$ the total wavevector of the system is $-k_e$ attributed from the whole

2. $e_h(k_h) = -e_e (k_e)$ 

The lower in the band the missing electron lies, the higher the energy of the system. The energy of the hole is the opposite sign of the energy of the missing electron, because it takes work to remove an electron from a low orbital

3. $v_h = v_e$

The velocity of the whole is equal to the velocity of the missing electron

4. $m_h = - m_e$ 
The effective mass is inversely proportional to the curvature $d^2 \epsilon /dk^2$ the whole has the oposite sign of the electron

### Effective mass

When one looks at the energy-wavevector relation

$\epsilon = (\hbar^2 / 2m)k^2 for free electrons, we see that $k^2$ determines the curvature of $\epsilon - k$. 

> For electrons in the band there are regions of unusually high curvature near the band gap at the zone boundary

One can define the effective mass $m^*$ with

$\frac{1}{m^*} = \frac{1}{\hbar^2}\frac{d^2 \epsilon}{dk^2}$ 

![[Pasted image 20241130145309.png]]

### Spin orbit coupling

![[Pasted image 20241130145430.png]]

### Silicon and Germanium

![[Pasted image 20241130145502.png]]

This figure shows the band structure of germanium:

+ The valence band edge is derived from $p_{3/2}$ and $p_{1/2}$ states of the three atoms, which comes essentiallyfrom the tight binding approximation
+ The $p_{3/2}$ is fourfold degerate and $p_{1/2}$ is double degenerate

![[Pasted image 20241130145717.png]]

### Intrinsic carrier concentration

> We want the concentration of intrinsic carriers as a function of temperature in terms of the band gap. This will be treated for simple parabolic band edges.

+ In terms of the chemical potential $\mu$ one can calculate the number of electrons excited to the conduction band at temperature $T$ 

Let $\epsilon - \mu >> k_bT$ thus the Fermi Dirac Distribution is

$f_e \approx \exp[(\mu - \epsilon)/k_bT]$ 

Then the probability that the conduction electron orbital is occupied is valid when $f_e <<1$ 

The energy of an electron in the conduction band is

$\epsilon_k = E_c + \hbar^2 k^2 / 2m_e$ where $E_c$ is the energy at the conduction band edge

With the density of states

![[Pasted image 20241130150256.png]]

One can now calculate the concentration of electrons in the conduction band 

![[Pasted image 20241130150314.png]]

This integrates and gives

![[Pasted image 20241130150350.png]]


The distribution function for holes is related to the distribution function for electrons with $f_h = 1-f_e$ 

![[Pasted image 20241130150443.png]]

#### Multipliying together the results

![[Pasted image 20241130150519.png]]

We now have a formula that doesn't involve the Fermi-Level and describes the conversion rate between electrons and hole


> In an intrinsic semiconductor the number of electronsi s equal to the number of wholes thus with $E_g = E_c - E_v$

![[Pasted image 20241130150713.png]]

Thus the intrinsic carrier concentration depends exponentially on $E_g / 2k_BT$ where $E_g$ is the energy gap.

### Intrinsic Mobility


> The mobility is the magnitude of the drift velocity of a charge carrier per unit electric field

$\mu = |v|/E$ 

The mobility is positive for both electrons and holes, although their drift velocities are opposite in an electric field

![[Pasted image 20241130151032.png]]

> As a rule of thumb the hole mobilities are typiclly smaller than the electron mobilities

### Impurity Conductivity 

> Certain impurities and imperfections drastically affect the electrical properties of a semiconductor

+ For example addition of boron to silcon increaxes the conductivity of the silicon with $10^3$ 
+ 
![[Pasted image 20241130151407.png]]

#### Donor States

> If an impurity atom of valence 5, such as P,As,Sb is substituted into the lattice there will be one additional valence electron from the impurity thus we have electron donors.

![[Pasted image 20241130151520.png]]

> Pentavalent impurities enter the lattice by substitution for normal atoms, the crystal as a whole remains neutral

![[Pasted image 20241130151631.png]]

![[Pasted image 20241130151708.png]]

#### Acceptor States

>A hole may be bound to a trivalent impuritiy in germanium or silicon, these are elements such as B, Al, Ga. This elements are called acceptor because they accept electrons form the valence band in order to complete the covalent bonds with their neigbor atoms, leaving holes in the band

![[Pasted image 20241130151924.png]]


If acceptors are dominant, holes will be released into the valence band and the conductivity will be controlled by holes, the material type is p-type

#### Summary Impurity states

+ If donor atoms are present in considerably greater numbers than acceptors, the thermal ionization of donors will release electrons into the conduction band. The conductivity of the specimen then will be controlled by electrons (negative charges), and the material is said to be n type.
+ If acceptors are dominant, holes will be released into the valence band and the conductivity will be controlled by holes (positive charges): the material is p type



![[Pasted image 20241130152056.png]]

### p-n Junction

> The p-n junction is made form a single crystal modified in two seperate p and n regions

+ Acceptor impurities make a p reagion where the majority carries are holes.
+ Donor impurities make the other part produce a n region with electrons
+ Holes concentrated on the p side tend to diffuse to fill the crystal uniformly
+ Electrons would diffuse from the n side but diffusion will upset the local electrical neutrality of the system.
+ The charge double layer creates an electric field directed from n to p that inhibits diffusion and maintains the seperation of the carrier types
![[Pasted image 20241130152607.png]]

> For the p-n junction the Fermi levels on both sides of the junction are the same

![[Pasted image 20241130152702.png]]


To reverse the p-n junction one can make then the p side more negative, making it "uphill" for the electrons to move across the junction

![[Pasted image 20241130152750.png]]

### Photovoltaic effect

> When light shines on a p_n junction without an external bias voltage, each absorbed photon creates an electron and a hole. When dese carries diffuse into the junction, the electric field of the carrier seperates them at the energy barrier producing a voltage

![[Pasted image 20241130152942.png]]

The appearence of a forward voltage across an illuminated junction is called photovoltaic effect. This junction can provide power to an external circuit.