# Teori: Ekspresi Aljabar (Theory: Algebraic Expressions)

## 1. Definisi: Ekspresi vs Persamaan / Definition: Expression vs Equation

**Ekspresi Aljabar (Algebraic Expression):**
Kombinasi variabel, konstanta, dan operasi matematika yang **tidak** mengandung tanda sama dengan.

```
Contoh ekspresi: 3x² + 2x - 5,   4ab - 7,   (x+1)/(x-2)
```

**Persamaan (Equation):**
Pernyataan bahwa dua ekspresi **bernilai sama**, ditandai dengan tanda `=`.

```
Contoh persamaan: 3x² + 2x - 5 = 0,   2x + 3 = 11
```

**Perbedaan Kunci:**
- Ekspresi: dapat disederhanakan atau dievaluasi
- Persamaan: dapat diselesaikan (dicari nilai variabelnya)

---

## 2. Variabel / Variables

**Definisi:** Simbol (biasanya huruf) yang mewakili nilai yang tidak diketahui atau nilai yang dapat berubah.

**Konvensi umum:**
- `x, y, z` — variabel umum
- `a, b, c` — konstanta atau koefisien dalam konteks tertentu
- `n, m, k` — bilangan bulat / indeks
- `t` — waktu (time)
- `r` — jari-jari (radius)

**Contoh:**
```
Dalam 5x² + 3y - 7:
- x dan y adalah variabel
```

---

## 3. Konstanta / Constants

**Definisi:** Nilai tetap yang tidak berubah dalam suatu ekspresi.

**Jenis:**
- **Bilangan bulat:** -5, 0, 3, 100
- **Desimal:** 3.14
- **Konstanta matematika:** π ≈ 3.14159..., e ≈ 2.71828..., √2 ≈ 1.41421...

---

## 4. Koefisien / Coefficients

**Definisi:** Faktor numerik yang mengalikan bagian variabel dari sebuah suku.

```
Suku      | Koefisien | Bagian Variabel
----------|-----------|----------------
7x²       |    7      |     x²
-3xy      |   -3      |     xy
x         |    1      |     x   (koefisien implisit = 1)
-y        |   -1      |     y   (koefisien implisit = -1)
5         |    5      |     (konstanta, tidak ada variabel)
```

**Catatan penting:** Koefisien bisa berupa bilangan apa pun termasuk pecahan: (1/2)x, πr²

---

## 5. Suku (Terms) — Monomial, Binomial, Trinomial, Polinomial

**Suku (Term):** Bagian dari ekspresi yang dipisahkan oleh tanda + atau -.

### Klasifikasi berdasarkan jumlah suku:

| Nama | Jumlah Suku | Contoh |
|------|-------------|--------|
| Monomial | 1 | 4x³, -7, 2xy |
| Binomial | 2 | x + 3, 2a - 5b |
| Trinomial | 3 | x² - 3x + 2 |
| Polinomial | ≥ 1 | a⁴ - 2a³ + a - 9 |

### Definisi Formal Polinomial:
Ekspresi berbentuk:
```
P(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₁x + a₀
```
di mana:
- `aₙ, aₙ₋₁, ..., a₀` adalah koefisien (bilangan real)
- `n` adalah bilangan bulat non-negatif (derajat)
- `aₙ ≠ 0` (koefisien utama/leading coefficient tidak nol)

### Non-Polinomial:
Ekspresi BUKAN polinomial jika mengandung:
- Pangkat pecahan: x^(1/2) = √x
- Pangkat negatif: x⁻¹ = 1/x
- Variabel dalam penyebut: 1/(x+1)
- Variabel dalam akar: √x

---

## 6. Suku Sejenis vs Tidak Sejenis / Like Terms vs Unlike Terms

**Suku Sejenis (Like Terms):** Suku yang memiliki **bagian variabel yang identik** (variabel yang sama dengan pangkat yang sama).

```
Suku Sejenis:
- 3x² dan -7x²    (sama: x²)
- 5ab dan -2ab    (sama: ab)
- 4 dan -9        (sama: konstanta)

Suku Tidak Sejenis (Unlike Terms):
- 3x² dan 3x     (pangkat berbeda)
- 2xy dan 2x²y   (pangkat berbeda)
- 5x dan 5y      (variabel berbeda)
```

**Aturan:** Hanya suku sejenis yang dapat dijumlahkan atau dikurangkan!

---

## 7. Derajat / Degree

### Derajat Suku (Degree of a Term):
Jumlah semua pangkat variabel dalam suku tersebut.

```
Suku     | Derajat
---------|--------
5x²      |   2
-3xy     |   1+1 = 2
4x²y³   |   2+3 = 5
7        |   0  (konstanta)
```

### Derajat Polinomial (Degree of a Polynomial):
Derajat tertinggi di antara semua suku-sukunya.

```
3x⁴ - 2x² + x - 7  →  derajat 4
5x²y³ + 2xy - 3    →  derajat 5
```

### Klasifikasi berdasarkan derajat:
| Derajat | Nama | Contoh |
|---------|------|--------|
| 0 | Konstan | 5 |
| 1 | Linear | 3x + 2 |
| 2 | Kuadrat (Quadratic) | x² - 4x + 3 |
| 3 | Kubik (Cubic) | 2x³ + x |
| 4 | Kuartik (Quartic) | x⁴ - 1 |
| n | Berderajat-n | aₙxⁿ + ... |

---

## 8. Evaluasi Ekspresi / Evaluation of Expressions

**Definisi:** Menghitung nilai numerik ekspresi dengan mensubstitusikan nilai tertentu ke variabel.

**Langkah-langkah:**
1. Tulis ekspresi
2. Ganti setiap variabel dengan nilai yang diberikan (gunakan tanda kurung)
3. Hitung menggunakan urutan operasi (PEMDAS/BODMAS)

**Contoh:**
```
Evaluasi P(x) = 2x² - 3x + 1 untuk x = -2:

P(-2) = 2(-2)² - 3(-2) + 1
      = 2(4) + 6 + 1
      = 8 + 6 + 1
      = 15
```

---

## 9. Penyederhanaan / Simplification — Menggabungkan Suku Sejenis

**Prosedur:**
1. Identifikasi suku sejenis
2. Jumlahkan/kurangkan koefisiennya
3. Pertahankan bagian variabelnya

**Contoh:**
```
5x² + 3x - 2x² + 7x - 4
= (5x² - 2x²) + (3x + 7x) - 4
= 3x² + 10x - 4
```

---

## 10. Penjumlahan dan Pengurangan Ekspresi Aljabar

**Penjumlahan:**
```
(3x² + 2x - 1) + (x² - 5x + 4)
= 3x² + x² + 2x - 5x - 1 + 4
= 4x² - 3x + 3
```

**Pengurangan (distribusikan tanda minus ke setiap suku):**
```
(3x² + 2x - 1) - (x² - 5x + 4)
= 3x² + 2x - 1 - x² + 5x - 4
= (3x² - x²) + (2x + 5x) + (-1 - 4)
= 2x² + 7x - 5
```

---

## 11. Perkalian Ekspresi Aljabar / Multiplication

### A. Monomial × Monomial
```
(3x²)(4x³) = 12x⁵
(-2ab)(5a²b) = -10a³b²
```

### B. Monomial × Polinomial (Hukum Distributif)
```
3x(x² - 2x + 4) = 3x³ - 6x² + 12x
```

### C. Binomial × Binomial — Metode FOIL
**FOIL** = First, Outer, Inner, Last
```
(a + b)(c + d) = ac + ad + bc + bd
                  F    O    I    L

(2x + 3)(x - 5) = 2x·x + 2x·(-5) + 3·x + 3·(-5)
                 = 2x² - 10x + 3x - 15
                 = 2x² - 7x - 15
```

### D. Polinomial × Polinomial (Perkalian Kolom)
```
(x² + 2x + 1)(x + 3):
= x²(x+3) + 2x(x+3) + 1(x+3)
= x³ + 3x² + 2x² + 6x + x + 3
= x³ + 5x² + 7x + 3
```

---

## 12. Pembagian Polinomial / Polynomial Long Division

### Pembagian Pendek (Short Division):
```
(6x² + 3x) ÷ 3x = 2x + 1
```

### Pembagian Panjang (Long Division):
Untuk membagi P(x) dengan D(x):
```
Contoh: (2x³ - 3x² + x + 4) ÷ (x - 2)

    2x² + x + 3
   _______________
x-2 | 2x³ - 3x² + x + 4
      2x³ - 4x²
      ----------
           x² + x
           x² - 2x
           --------
               3x + 4
               3x - 6
               ------
                   10  ← sisa (remainder)

Hasil: 2x² + x + 3 + 10/(x-2)
```

**Teorema Pembagian (Division Algorithm):**
```
P(x) = D(x) · Q(x) + R(x)
```
di mana derajat R(x) < derajat D(x)

---

## 13. Perkalian Khusus / Special Products

### (a + b)² = a² + 2ab + b²
```
(x + 3)² = x² + 6x + 9
```

### (a - b)² = a² - 2ab + b²
```
(2x - 5)² = 4x² - 20x + 25
```

### (a + b)(a - b) = a² - b² (Selisih Dua Kuadrat)
```
(x + 4)(x - 4) = x² - 16
```

### (a + b)³ = a³ + 3a²b + 3ab² + b³
```
(x + 2)³ = x³ + 6x² + 12x + 8
```

### (a - b)³ = a³ - 3a²b + 3ab² - b³
```
(x - 1)³ = x³ - 3x² + 3x - 1
```

### Identitas Tambahan:
```
a³ + b³ = (a + b)(a² - ab + b²)  [Jumlah dua kubik]
a³ - b³ = (a - b)(a² + ab + b²)  [Selisih dua kubik]
```

---

## 14. Ekspresi Rasional / Rational Expressions

**Definisi:** Pecahan yang pembilang dan penyebutnya adalah polinomial.

```
Bentuk umum: P(x)/Q(x), di mana Q(x) ≠ 0

Contoh: (x² - 4)/(x + 2),   (3x + 1)/(x² - x - 6)
```

### Batasan Domain (Domain Restrictions):
Nilai variabel yang membuat **penyebut = 0** harus dikecualikan!

```
Untuk f(x) = (x+1)/(x-3):
  x - 3 = 0 → x = 3
  Domain: semua bilangan real kecuali x = 3
  Notasi: {x ∈ ℝ | x ≠ 3}
```

---

## 15. Penyederhanaan Ekspresi Rasional / Simplifying Rational Expressions

**Langkah-langkah:**
1. Faktorkan pembilang dan penyebut sepenuhnya
2. Batalkan faktor-faktor yang sama (≠ 0)
3. Nyatakan batasan domain

**Contoh:**
```
  x² - 4         (x+2)(x-2)
————————————  =  ——————————— = x - 2,   x ≠ -2
   x + 2             x+2

  x² - x - 6       (x-3)(x+2)       x+2
—————————————  =  ————————————  =  ———,   x ≠ 3, x ≠ -2
  x² - 5x + 6      (x-3)(x-2)      x-2
```

**Perkalian dan Pembagian Ekspresi Rasional:**
```
P/Q × R/S = PR/(QS)
P/Q ÷ R/S = P/Q × S/R = PS/(QR)
```

**Penjumlahan/Pengurangan (perlu KPK / LCD):**
```
P/Q + R/S = (PS + QR)/(QS)
```

---

## Ringkasan Rumus / Formula Summary

| Rumus | Nama |
|-------|------|
| (a+b)² = a² + 2ab + b² | Kuadrat jumlah |
| (a-b)² = a² - 2ab + b² | Kuadrat selisih |
| (a+b)(a-b) = a² - b² | Selisih dua kuadrat |
| (a+b)³ = a³ + 3a²b + 3ab² + b³ | Kubik jumlah |
| (a-b)³ = a³ - 3a²b + 3ab² - b³ | Kubik selisih |
| a³+b³ = (a+b)(a²-ab+b²) | Jumlah dua kubik |
| a³-b³ = (a-b)(a²+ab+b²) | Selisih dua kubik |
