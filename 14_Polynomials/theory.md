# Teori Lengkap: Polinomial / Complete Theory: Polynomials

---

## 1. Definisi Polinomial / Definition of a Polynomial

**Indonesia:** Polinomial dalam variabel x adalah ekspresi berbentuk:

$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0$$

di mana:
- $a_n, a_{n-1}, \ldots, a_0 \in \mathbb{R}$ (atau $\mathbb{C}$) adalah **koefisien**
- $n$ adalah bilangan bulat non-negatif
- $a_n \neq 0$ (jika $n > 0$)

**English:** A polynomial in variable x is an expression of the form:

$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0$$

where the $a_i$ are **coefficients** (real or complex numbers), and $n$ is a non-negative integer.

**Yang BUKAN polinomial / NOT polynomials:**
- $\frac{1}{x}$ = $x^{-1}$ (eksponen negatif / negative exponent)
- $\sqrt{x}$ = $x^{1/2}$ (eksponen pecahan / fractional exponent)
- $2^x$ (variabel di eksponen / variable in exponent)
- $|x|$ (nilai mutlak / absolute value)

---

## 2. Derajat, Koefisien Utama, Suku Utama, Suku Konstan

### 2.1 Derajat (Degree)
**Derajat** suatu polinomial adalah eksponen tertinggi dari variabelnya.

| Polinomial | Derajat |
|-----------|---------|
| $P(x) = 7$ | 0 (konstanta) |
| $P(x) = 3x + 1$ | 1 (linear) |
| $P(x) = x^2 - 4$ | 2 (kuadrat) |
| $P(x) = 2x^3 - x + 5$ | 3 (kubik) |
| $P(x) = x^4 + 1$ | 4 (kuartik) |
| $P(x) = x^5$ | 5 (kuintik) |

**Polinomial nol** (semua koefisien = 0) tidak memiliki derajat yang terdefinisi.

### 2.2 Koefisien Utama (Leading Coefficient)
Koefisien dari suku berderajat tertinggi: $a_n$ dalam $P(x) = a_n x^n + \cdots$

Contoh: $P(x) = -3x^4 + 2x^2 - 1$ → koefisien utama = $-3$

### 2.3 Suku Utama (Leading Term)
Suku berderajat tertinggi: $a_n x^n$

Contoh: $P(x) = -3x^4 + 2x^2 - 1$ → suku utama = $-3x^4$

### 2.4 Suku Konstan (Constant Term)
Suku dengan eksponen 0: $a_0 = P(0)$

Contoh: $P(x) = -3x^4 + 2x^2 - 1$ → suku konstan = $-1$

---

## 3. Bentuk Standar (Standard Form)

Bentuk standar polinomial ditulis dengan menurunkan derajat dari kiri ke kanan:
$$P(x) = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0$$

Contoh (bukan standar): $3 - 2x^2 + x^4$
Bentuk standar: $x^4 - 2x^2 + 3$

---

## 4. Jenis-Jenis Polinomial Berdasarkan Jumlah Suku

| Nama | Jumlah Suku | Contoh |
|------|-------------|--------|
| **Monomial** | 1 | $5x^3$ |
| **Binomial** | 2 | $x^2 - 4$ |
| **Trinomial** | 3 | $x^2 + 3x - 10$ |
| **Polinomial** | 4+ | $x^4 - 2x^3 + x - 7$ |

---

## 5. Penjumlahan dan Pengurangan Polinomial

**Aturan:** Gabungkan suku-suku sejenis (sama derajat).

**Example:**
$$P(x) = 3x^3 - 2x^2 + x - 5$$
$$Q(x) = x^3 + 4x^2 - 3x + 2$$

$$P(x) + Q(x) = (3+1)x^3 + (-2+4)x^2 + (1-3)x + (-5+2)$$
$$= 4x^3 + 2x^2 - 2x - 3$$

$$P(x) - Q(x) = (3-1)x^3 + (-2-4)x^2 + (1+3)x + (-5-2)$$
$$= 2x^3 - 6x^2 + 4x - 7$$

**Properti / Properties:**
- Himpunan polinomial tertutup terhadap penjumlahan dan pengurangan
- Derajat dari $P \pm Q \leq \max(\deg P, \deg Q)$

---

## 6. Perkalian Polinomial (Polynomial Multiplication)

### 6.1 Aturan Umum (General Rule)
Gunakan hukum distributif: setiap suku dari P dikalikan dengan setiap suku dari Q.

Jika $P$ memiliki $m+1$ suku dan $Q$ memiliki $n+1$ suku, maka hasil kali memiliki derajat $m + n$.

### 6.2 Kasus Khusus

**Monomial × Polynomial:**
$$3x^2 \cdot (2x^3 - x + 4) = 6x^5 - 3x^3 + 12x^2$$

**FOIL (untuk dua binomial):**
$$(a+b)(c+d) = ac + ad + bc + bd$$
$$(x+3)(x-5) = x^2 - 5x + 3x - 15 = x^2 - 2x - 15$$

**Kuadrat binomial:**
$$(a+b)^2 = a^2 + 2ab + b^2$$
$$(a-b)^2 = a^2 - 2ab + b^2$$

**Konjugat / Selisih kuadrat:**
$$(a+b)(a-b) = a^2 - b^2$$

**Kubik:**
$$(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$$
$$(a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$$

### 6.3 Teorema Binomial (Binomial Theorem)
$$(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$$

di mana $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ adalah koefisien binomial.

---

## 7. Algoritma Pembagian Panjang Polinomial (Polynomial Long Division)

**Teorema Pembagian:** Untuk semua polinomial $P(x)$ dan $D(x) \neq 0$, terdapat unik $Q(x)$ (hasil bagi) dan $R(x)$ (sisa) sehingga:

$$P(x) = D(x) \cdot Q(x) + R(x), \quad \deg(R) < \deg(D)$$

### Algoritma:
1. Urutkan $P(x)$ dan $D(x)$ dalam bentuk standar (derajat menurun)
2. Bagi suku utama $P$ dengan suku utama $D$ → suku pertama $Q$
3. Kalikan hasil tersebut dengan $D(x)$, kurangi dari $P(x)$
4. Ulangi sampai derajat sisa < derajat $D$

**Contoh:** $(2x^3 - 3x^2 + x - 5) \div (x - 2)$

```
        2x^2 + x + 3
       ─────────────────
x - 2 │ 2x^3 - 3x^2 + x - 5
        2x^3 - 4x^2
        ───────────
              x^2 + x
              x^2 - 2x
              ─────────
                   3x - 5
                   3x - 6
                   ───────
                       1
```

Jadi: $2x^3 - 3x^2 + x - 5 = (x-2)(2x^2 + x + 3) + 1$

---

## 8. Pembagian Sintetik (Synthetic Division)

Pembagian sintetik adalah cara ringkas membagi $P(x)$ oleh $(x - a)$.

**Algoritma Horner untuk pembagian sintetik:**
Untuk $P(x) = a_n x^n + \cdots + a_0$ dibagi $(x - c)$:

```
c | a_n  a_{n-1}  ...  a_1  a_0
  |       c·b_n   ...
  ─────────────────────────────
    b_n   b_{n-1} ...  b_0  | R
```

di mana $b_n = a_n$ dan $b_k = a_k + c \cdot b_{k+1}$, dan $R = P(c)$.

**Contoh:** $(3x^3 - 4x^2 + 2x - 1) \div (x - 2)$

```
2 | 3  -4   2  -1
  |     6   4  12
  ─────────────────
    3   2   6  11
```

Hasil: $Q(x) = 3x^2 + 2x + 6$, sisa $R = 11$

**Verifikasi:** $3(2)^3 - 4(2)^2 + 2(2) - 1 = 24 - 16 + 4 - 1 = 11$ ✓

---

## 9. Teorema Sisa (Remainder Theorem)

**Teorema:** Jika polinomial $P(x)$ dibagi oleh $(x - a)$, maka sisanya adalah $P(a)$.

$$P(x) = (x-a) \cdot Q(x) + P(a)$$

**Bukti:** Dari teorema pembagian: $P(x) = (x-a) \cdot Q(x) + R$
Substitusikan $x = a$: $P(a) = (a-a) \cdot Q(a) + R = 0 + R = R$ ∎

**Contoh:** Temukan sisa dari $(x^3 - 2x^2 + 3x - 4) \div (x - 1)$

$P(1) = 1 - 2 + 3 - 4 = -2$ → sisa = $-2$

---

## 10. Teorema Faktor (Factor Theorem)

**Teorema:** $(x - a)$ adalah faktor dari $P(x)$ jika dan hanya jika $P(a) = 0$.

**Artinya:** $a$ adalah akar dari $P(x) \iff (x - a)$ membagi $P(x)$ habis.

**Bukti:**
- (⇒) Jika $(x-a)$ adalah faktor, maka $P(x) = (x-a) Q(x)$, sehingga $P(a) = 0$.
- (⇐) Jika $P(a) = 0$, dari teorema sisa: sisa = $P(a) = 0$, jadi $(x-a)$ membagi habis. ∎

**Contoh:** Apakah $(x - 3)$ faktor dari $P(x) = x^3 - 6x^2 + 11x - 6$?

$P(3) = 27 - 54 + 33 - 6 = 0$ ✓ → Ya, $(x-3)$ adalah faktor.

---

## 11. Teorema Akar Rasional (Rational Root Theorem)

**Teorema:** Jika $P(x) = a_n x^n + \cdots + a_0$ memiliki koefisien bilangan bulat,
maka setiap akar rasional $\frac{p}{q}$ (dalam bentuk paling sederhana) memenuhi:
- $p$ adalah faktor dari konstanta $a_0$
- $q$ adalah faktor dari koefisien utama $a_n$

**Contoh:** $P(x) = 2x^3 - 3x^2 - 11x + 6$

Faktor $a_0 = 6$: $\pm 1, \pm 2, \pm 3, \pm 6$
Faktor $a_n = 2$: $\pm 1, \pm 2$

Kandidat akar rasional: $\pm 1, \pm 2, \pm 3, \pm 6, \pm \frac{1}{2}, \pm \frac{3}{2}$

Uji: $P(3) = 54 - 27 - 33 + 6 = 0$ → $x = 3$ adalah akar.

---

## 12. Teorema Fundamental Aljabar (Fundamental Theorem of Algebra)

**Teorema (Gauss, 1799):** Setiap polinomial derajat $n \geq 1$ dengan koefisien kompleks
memiliki tepat $n$ akar kompleks (dihitung dengan multiplisitas).

**Akibat:**
- Setiap polinomial derajat $n$ dapat difaktorkan sepenuhnya atas $\mathbb{C}$:
$$P(x) = a_n (x - r_1)(x - r_2) \cdots (x - r_n)$$
- Polinomial dengan koefisien real: akar kompleks muncul berpasangan konjugat.

---

## 13. Multiplisitas Akar (Multiplicity of Roots)

Jika $(x - a)^k$ membagi $P(x)$ tetapi $(x - a)^{k+1}$ tidak, maka $a$ adalah akar dengan **multiplisitas** $k$.

| Multiplisitas | Perilaku grafik di $x = a$ |
|---------------|---------------------------|
| Ganjil (1, 3, 5...) | Grafik memotong sumbu-x |
| Genap (2, 4, 6...) | Grafik menyentuh sumbu-x (titik balik) |

**Contoh:** $P(x) = (x-1)^2 (x+3)^3$
- $x = 1$ adalah akar dengan multiplisitas 2 (grafik menyentuh sumbu-x)
- $x = -3$ adalah akar dengan multiplisitas 3 (grafik memotong sumbu-x)

---

## 14. Perilaku Ujung Polinomial (End Behavior)

Perilaku ujung ditentukan oleh **suku utama** $a_n x^n$:

| $a_n$ | $n$ | $x \to -\infty$ | $x \to +\infty$ |
|-------|-----|-----------------|-----------------|
| $+$ | genap | $+\infty$ | $+\infty$ |
| $-$ | genap | $-\infty$ | $-\infty$ |
| $+$ | ganjil | $-\infty$ | $+\infty$ |
| $-$ | ganjil | $+\infty$ | $-\infty$ |

Mnemonik: "even = same, odd = opposite" (untuk $a_n > 0$)

---

## 15. Teorema Nilai Antara untuk Polinomial (Intermediate Value Theorem)

**Teorema:** Jika $P(x)$ kontinu (semua polinomial kontinu) dan $P(a) < 0 < P(b)$
(atau $P(a) > 0 > P(b)$), maka terdapat $c \in (a, b)$ sehingga $P(c) = 0$.

**Akibat praktis:** Jika $P(a)$ dan $P(b)$ berbeda tanda, ada akar real di antara $a$ dan $b$.

Ini menjadi dasar dari **metode bagi-dua (bisection method)** untuk mencari akar secara numerik.

---

## 16. Interpolasi Polinomial — Pengenalan Lagrange

**Masalah:** Diberikan $n+1$ titik $(x_0, y_0), (x_1, y_1), \ldots, (x_n, y_n)$
dengan $x_i$ berbeda, temukan polinomial berderajat $\leq n$ yang melalui semua titik.

**Formula Interpolasi Lagrange:**
$$P(x) = \sum_{i=0}^{n} y_i \cdot L_i(x)$$

di mana **basis Lagrange**:
$$L_i(x) = \prod_{j=0, j \neq i}^{n} \frac{x - x_j}{x_i - x_j}$$

**Properti:** $L_i(x_j) = \delta_{ij}$ (delta Kronecker: 1 jika $i=j$, 0 jika tidak)

---

## 17. Polinomial Khusus (Special Polynomials)

### 17.1 Polinomial Chebyshev
$$T_n(\cos\theta) = \cos(n\theta)$$

Digunakan dalam aproksimasi numerik karena meminimalkan error maksimum.
Jenis pertama: $T_0 = 1, T_1 = x, T_{n+1} = 2xT_n - T_{n-1}$

### 17.2 Polinomial Legendre
$$P_n(x) = \frac{1}{2^n n!} \frac{d^n}{dx^n}[(x^2-1)^n]$$

Ortogonal pada $[-1, 1]$. Digunakan dalam fisika (persamaan Laplace) dan kuadratur Gauss.

### 17.3 Polinomial Hermite, Laguerre
Digunakan dalam mekanika kuantum dan probabilitas.

---

## 18. Ketidaksamaan Polinomial (Polynomial Inequalities)

Untuk menyelesaikan $P(x) > 0$ (atau $< 0$):

1. Temukan semua akar real dari $P(x) = 0$
2. Tandai akar-akar pada garis bilangan — bagi garis menjadi interval
3. Uji tanda $P(x)$ di setiap interval (pilih titik uji)
4. Gunakan multiplisitas untuk menentukan apakah tanda berubah di setiap akar

**Contoh:** $(x - 1)(x + 2)(x - 3) > 0$

Akar: $x = -2, 1, 3$. Interval: $(-\infty, -2), (-2, 1), (1, 3), (3, +\infty)$

| Interval | Uji $x$ | Tanda |
|----------|---------|-------|
| $(-\infty, -2)$ | $x = -3$ | $(−)(−)(−) = −$ |
| $(-2, 1)$ | $x = 0$ | $(−)(+)(−) = +$ |
| $(1, 3)$ | $x = 2$ | $(+)(+)(−) = −$ |
| $(3, +\infty)$ | $x = 4$ | $(+)(+)(+) = +$ |

Solusi: $x \in (-2, 1) \cup (3, +\infty)$

---

## 19. Metode Horner untuk Evaluasi Efisien

Mengevaluasi $P(x) = a_n x^n + \cdots + a_0$ secara langsung memerlukan $O(n^2)$ operasi.

**Metode Horner** menulis ulang:
$$P(x) = (\cdots((a_n x + a_{n-1})x + a_{n-2})x + \cdots + a_1)x + a_0$$

Hanya memerlukan $n$ perkalian dan $n$ penjumlahan → $O(n)$ operasi!

---

## Referensi / References

- Stewart, J. (2016). *Calculus: Early Transcendentals*. Cengage.
- Axler, S. (2015). *Linear Algebra Done Right*. Springer.
- Lang, S. (2005). *Undergraduate Algebra*. Springer.
- Knuth, D.E. (1997). *The Art of Computer Programming, Vol. 2*. Addison-Wesley.
