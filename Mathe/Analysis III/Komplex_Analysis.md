# Kapitel 1 Komplexe Zahlen und Funktionen

## 1.4 $\exp,\cos,\sin,\log$ auf $\mathbb{C}$

### Definition komplexe Exponentialfunktion

Wir definieren die Exponentialfunktion auf ganz $\mathbb{C}$ durch

> $\exp(z):= e^z := \sum_{n=0}^\infty \frac{z^n}{n!}$

### Definition komplexer Cosinus und Sinus

WIr definieren die Funktionen $\cos,\sin: \mathbb{C} \to \mathbb{C}$ durch

+ $\cos(z) = \frac{e^{iz}+ e^{-iz}}{2}$
+ $sin(z) = \frac{e^{iz}-e^{-iz}}{2i}$

### Satz 1.21 Eindeutigkeit und Definition von $\pi$

Es gibt genau eine reelle Zahl $r \in [0,2]$ mit $cos(r)=0$. Wir definieren diese einzige Zahl in $[0,4]$ mit $cos(\pi/2) = 0$ 

### Satz 1.22 Eindeutigkeit von Polarkoordinaten

Wir bezeichnen den Einheitskreis mit $\mathbb{T}= \{z \in \mathbb{C}<: |z| = 1\}$

1. Die stetige Abbildung $\gamma: [0, 2\pi) \to \mathbb{T}$ mit $\gamma(t)=e^{it}$ ist bijektiv und durchläuft $\mathbb{T}$ im mathematisch positiven Sinn
2. Es gilt $e^z = 1$ genau dann, wenn $z = 2ki\pi$ für $k \in \mathbb{Z}$
3. Jede komplexe Zahl $z \neq 0$ kann eindeutig in der Form

$z = re^{i \phi}$ mit $r = |z| >0$ und $\phi \in [0, 2\pi)$ geschrieben werden mit $\phi$ dem Argument und $e^{i\phi}$ der Phase.

# Kapitel 2 Komplexe Differenzierbarkeit und der Cauchy'sche Integralsatz

In diesem Kapitel ist $U$ stets eine nichtleere, offene Teilmenge von $\mathbb{C}$

## 2.1 Komplex Differenzieren

### Definition komplex differenzierbar, holomorph, ganz

Sei $U \neq \empty$ offen. $f: U \to \mathbb{C}$ heißt in $z_0 \in U$ komplex differenzierbar falls ein $f'(z_0):=c \in \mathbb{C}$ exestiert,

$\forall \epsilon >0, \exists \delta > 0: |\frac{f(z_0)-f(z)}{z_0-z}-c| \leq \epsilon ~\forall z \in B_\delta(z_0), z\neq z_0$ 

Alternativ schreiben wir $lim_{z\to z_0}\frac{f(z_0)-f(z)}{z_0-z} = c$

Ist die dadurch definierte Ableitungsfunktion $f'$ stetig dann heißt $f$ holomorph auf U. Eine auf ganz $\mathbb{C}$ definierte und dort holomorphe Funktion heißt ganz.

### Definition 2.2 (Stammfunktion)

Sei $U \neq \empty$ offen und $f: U \to \mathbb{C}$ . Eine differenzierbare Funktion $F: U \to \mathbb{C}$ mit $F'= f$ heißt Stammfunktion von $f$

### Lemma 2.3 differenzierbar $\Rightarrow$ stetig

Sei $U \neq \empty$ offen. Falls die FUnktion $f: U \to \mathbb{C}$ in $z_0$ differenzierbar ist so ist sie in $z_0$ stetig


