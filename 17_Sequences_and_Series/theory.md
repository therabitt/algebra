# Theory: Sequences and Series / Teori: Barisan dan Deret

---

## 1. Definition of a Sequence / Definisi Barisan

A **sequence** (barisan) is an **ordered list of numbers** where each number
occupies a specific position.

```
Formal Definition:
A sequence is a function f: ℕ → ℝ (or ℂ), where the natural numbers index
each term. We write a_n = f(n).
```

**Examples:**
- (2, 4, 6, 8, ...) — even numbers
- (1, 1/2, 1/4, 1/8, ...) — powers of 1/2
- (1, 1, 2, 3, 5, 8, ...) — Fibonacci

---

## 2. Notation / Notasi

- **a_n** — the nth term (suku ke-n)
- **{a_n}** or **(a_n)** — the whole sequence
- **a_1** — first term (suku pertama)
- **a_n = f(n)** — general term / explicit formula
- **n ∈ ℕ** — index n is a natural number

**Examples of general terms:**
- a_n = 2n → (2, 4, 6, 8, ...)
- a_n = 1/n → (1, 1/2, 1/3, 1/4, ...)
- a_n = (-1)^n → (-1, 1, -1, 1, ...)

---

## 3. Finite vs Infinite Sequences / Barisan Hingga vs Tak Hingga

| Type | Description | Example |
|------|-------------|---------|
| **Finite** | Has a last term (suku terakhir ada) | (1, 2, 3, ..., 100) |
| **Infinite** | Continues without end (tak ada akhir) | (1, 2, 3, 4, ...) |

---

## 4. Arithmetic Sequences / Barisan Aritmetika

An **arithmetic sequence** has a **constant difference** between consecutive terms.

```
Definition:
A sequence {a_n} is arithmetic if a_{n+1} - a_n = d (constant) for all n.
d is called the common difference (beda).
```

### General Term Formula
```
a_n = a_1 + (n - 1)d
```
where:
- a_1 = first term
- d = common difference
- n = term number

### Properties:
- If d > 0: sequence is increasing (naik)
- If d < 0: sequence is decreasing (turun)
- If d = 0: constant sequence (konstan)
- The terms form a linear function of n: a_n = dn + (a_1 - d)

**Example:** 3, 7, 11, 15, ...
- d = 4, a_1 = 3
- a_n = 3 + (n-1)·4 = 4n - 1
- a_10 = 4(10) - 1 = 39

---

## 5. Geometric Sequences / Barisan Geometri

A **geometric sequence** has a **constant ratio** between consecutive terms.

```
Definition:
A sequence {a_n} is geometric if a_{n+1}/a_n = r (constant) for all n.
r is called the common ratio (rasio).
```

### General Term Formula
```
a_n = a_1 · r^(n-1)
```

### Properties:
- If |r| > 1: sequence grows without bound (diverges)
- If |r| = 1: constant sequence (if r=1) or alternating (if r=-1)
- If |r| < 1: terms approach 0 (converges to 0)
- If r < 0: terms alternate in sign

**Example:** 2, 6, 18, 54, ...
- r = 3, a_1 = 2
- a_n = 2 · 3^(n-1)
- a_5 = 2 · 3^4 = 162

### Geometric Mean:
If a, G, b are in geometric sequence: G² = ab → G = √(ab)

---

## 6. Other Special Sequences / Barisan Khusus Lainnya

### Fibonacci Sequence
- **Definition:** F_1 = 1, F_2 = 1, F_n = F_{n-1} + F_{n-2}
- Sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
- **Binet's Formula:** F_n = (φ^n - ψ^n)/√5
  where φ = (1+√5)/2 ≈ 1.618 (golden ratio), ψ = (1-√5)/2

### Triangular Numbers
- T_n = n(n+1)/2
- Sequence: 1, 3, 6, 10, 15, 21, ...
- Represents dots forming equilateral triangles

### Harmonic Sequence
- a_n = 1/n
- Sequence: 1, 1/2, 1/3, 1/4, ...
- Terms → 0 but series DIVERGES

### Prime Sequence
- 2, 3, 5, 7, 11, 13, 17, ...
- No closed-form general formula

### Square Numbers
- a_n = n²
- Sequence: 1, 4, 9, 16, 25, ...

---

## 7. Recursive vs Explicit Formulas / Rumus Rekursif vs Eksplisit

| Type | Description | Example |
|------|-------------|---------|
| **Explicit** | a_n directly in terms of n | a_n = 3n + 1 |
| **Recursive** | a_n in terms of previous terms | a_n = a_{n-1} + 3, a_1 = 4 |

**Converting recursive to explicit:**
For arithmetic: a_n = a_1 + (n-1)d (if a_{n+1} = a_n + d)
For Fibonacci: Use Binet's formula

---

## 8. Definition of a Series / Definisi Deret

A **series** (deret) is the **sum of terms** of a sequence.

```
Finite Series:  S_n = a_1 + a_2 + ... + a_n = Σ_{k=1}^{n} a_k

Infinite Series: S = Σ_{k=1}^{∞} a_k = lim_{n→∞} S_n
```

The **partial sum** S_n = a_1 + a_2 + ... + a_n is itself a sequence.

---

## 9. Sigma Notation / Notasi Sigma (Σ)

```
Σ_{k=m}^{n} a_k = a_m + a_{m+1} + ... + a_n
```

**Components:**
- Σ (capital sigma) = summation
- k = index variable (indeks)
- m = lower limit (batas bawah)
- n = upper limit (batas atas)
- a_k = summand (suku yang dijumlahkan)

**Key Formulas:**
- Σ_{k=1}^{n} 1 = n
- Σ_{k=1}^{n} k = n(n+1)/2
- Σ_{k=1}^{n} k² = n(n+1)(2n+1)/6
- Σ_{k=1}^{n} k³ = [n(n+1)/2]²

**Properties of Sigma:**
- Σ c·a_k = c · Σ a_k  (constant factor)
- Σ (a_k + b_k) = Σ a_k + Σ b_k  (linearity)

---

## 10. Arithmetic Series / Deret Aritmetika

The sum of the first n terms of an arithmetic sequence:

### Sum Formula
```
S_n = n(a_1 + a_n)/2 = n[2a_1 + (n-1)d]/2
```

### Derivation / Penurunan Rumus:
```
S_n = a_1 + (a_1+d) + (a_1+2d) + ... + a_n       ...(1)
S_n = a_n + (a_n-d) + (a_n-2d) + ... + a_1       ...(2) [reversed]

Add (1) + (2):
2S_n = n(a_1 + a_n)
S_n = n(a_1 + a_n)/2  ■
```

**Example:** Sum of 1+2+3+...+100
- a_1=1, a_n=100, n=100
- S_100 = 100(1+100)/2 = 5050 (Gauss's famous result!)

---

## 11. Geometric Series / Deret Geometri

The sum of the first n terms of a geometric sequence:

### Sum Formula
```
S_n = a_1(1 - r^n)/(1 - r)   for r ≠ 1
S_n = n·a_1                   for r = 1
```

### Derivation / Penurunan Rumus:
```
S_n = a_1 + a_1·r + a_1·r² + ... + a_1·r^(n-1)       ...(1)
r·S_n = a_1·r + a_1·r² + ... + a_1·r^n                ...(2) [multiply by r]

Subtract (1) - (2):
S_n - r·S_n = a_1 - a_1·r^n
S_n(1 - r) = a_1(1 - r^n)
S_n = a_1(1 - r^n)/(1 - r)  ■
```

**Example:** 2 + 6 + 18 + ... (n=5 terms, r=3)
- S_5 = 2(1 - 3^5)/(1 - 3) = 2(1-243)/(-2) = 242

---

## 12. Infinite Geometric Series / Deret Geometri Tak Hingga

When |r| < 1, the infinite sum converges:

```
S_∞ = a_1/(1 - r)    provided |r| < 1
```

### Proof / Bukti:
```
As n → ∞, r^n → 0 (because |r| < 1)
So: lim_{n→∞} S_n = lim_{n→∞} a_1(1-r^n)/(1-r)
                   = a_1(1-0)/(1-r)
                   = a_1/(1-r)  ■
```

**Zeno's Paradox Application:**
1/2 + 1/4 + 1/8 + ... = (1/2)/(1-1/2) = 1
(Arrow reaches target even with infinite steps!)

**Example:** 0.333... = 3/10 + 3/100 + ...
= (3/10)/(1 - 1/10) = (3/10)/(9/10) = 1/3 ✓

---

## 13. Convergence and Divergence / Konvergensi dan Divergensi

An infinite series Σa_k **converges** if the sequence of partial sums {S_n}
has a finite limit L. Otherwise it **diverges**.

### Basic Tests:

**nth Term Test (Necessary Condition for Convergence):**
If Σa_k converges, then lim_{n→∞} a_n = 0.
(Contrapositive: if lim a_n ≠ 0, series DIVERGES)

**Geometric Series Test:**
Σ a·r^k converges iff |r| < 1

**Comparison Test:**
If 0 ≤ a_k ≤ b_k and Σb_k converges, then Σa_k converges.
If a_k ≥ b_k ≥ 0 and Σb_k diverges, then Σa_k diverges.

---

## 14. Telescoping Series / Deret Teleskopik

A **telescoping series** is one where consecutive terms cancel:

```
Σ_{k=1}^{n} (a_k - a_{k+1}) = a_1 - a_{n+1}
```

**Example:**
Σ_{k=1}^{∞} 1/(k(k+1))
= Σ_{k=1}^{∞} (1/k - 1/(k+1))    [partial fractions]
= (1 - 1/2) + (1/2 - 1/3) + (1/3 - 1/4) + ...
= 1  (everything cancels except first term!)

---

## 15. Harmonic Series / Deret Harmonik

The harmonic series Σ_{n=1}^{∞} 1/n = 1 + 1/2 + 1/3 + ... **DIVERGES**.

### Proof (Oresme, ~1350 AD):
```
S = 1 + 1/2 + (1/3 + 1/4) + (1/5+1/6+1/7+1/8) + ...
     ≥ 1 + 1/2 + (1/4+1/4) + (1/8+1/8+1/8+1/8) + ...
     = 1 + 1/2 + 1/2 + 1/2 + ...  → ∞  ■
```

Despite each term approaching 0, the sum grows without bound!

---

## 16. Power Series Intro / Pengantar Deret Pangkat

A **power series** is a series of the form:
```
Σ_{n=0}^{∞} c_n · (x - a)^n = c_0 + c_1(x-a) + c_2(x-a)² + ...
```

**Geometric series as power series:**
1/(1-x) = Σ_{n=0}^{∞} x^n = 1 + x + x² + x³ + ...  (|x| < 1)

This is the foundation for Taylor series in calculus.

---

## 17. Applications / Aplikasi

### Compound Interest (Bunga Majemuk)
A = P(1 + r/n)^(nt)

If compounded continuously: A = Pe^(rt)
This uses the limit: lim_{n→∞}(1 + r/n)^n = e^r

### Zeno's Paradox
Achilles runs 1/2 + 1/4 + 1/8 + ... = 1 meter. ✓
Infinite steps, finite distance → convergent geometric series.

### Fractals
The Sierpinski triangle: at each step, area removed = (1/4)·previous area
Total area removed = (1/4)/(1 - 1/4) = 1/3 of original.

### DNA / Biology
Population growth: P_n = P_0 · r^n (geometric sequence)
Drug dosing: amount remaining after n doses (geometric series)
