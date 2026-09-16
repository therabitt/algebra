# 📖 Teori Sistem Persamaan (Systems of Equations Theory)

## 1. Definisi Sistem Persamaan / Definition

**Sistem persamaan** adalah sekumpulan dua atau lebih persamaan yang harus dipenuhi secara bersamaan.

Notasi umum:
$$\begin{cases} f_1(x_1, x_2, \ldots, x_n) = 0 \\ f_2(x_1, x_2, \ldots, x_n) = 0 \\ \vdots \\ f_m(x_1, x_2, \ldots, x_n) = 0 \end{cases}$$

Untuk sistem **linear** 2 variabel:
$$\begin{cases} a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2 \end{cases}$$

---

## 2. Solusi Sistem / Solution of a System

**Solusi** adalah pasangan terurut (x, y) yang memenuhi **semua** persamaan dalam sistem.

Untuk sistem 2×2 linear, solusi adalah **titik potong** dua garis pada bidang koordinat.

**Pengecekan solusi:** Substitusikan nilai (x₀, y₀) ke setiap persamaan dan verifikasi kesetaraan.

---

## 3. Klasifikasi Sistem Linear 2 Variabel / Classification

### 3a. Konsisten (Satu Solusi) / Consistent – Unique Solution

Dua garis berpotongan di tepat satu titik.

**Kondisi:** $\frac{a_1}{a_2} \neq \frac{b_1}{b_2}$

Gradien (slope) berbeda: $m_1 \neq m_2$

```
y
|  /  garis 2
| /
|/ ← titik potong (x₀, y₀)
/
\   garis 1
 \
```

### 3b. Inkonsisten (Tidak Ada Solusi) / Inconsistent – No Solution

Dua garis sejajar (tidak pernah berpotongan).

**Kondisi:** $\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}$

Gradien sama, intercept berbeda: m₁ = m₂, namun garis berbeda.

```
y
|  garis 1  garis 2
|  /         /
| /         /
|/         /
```

### 3c. Dependen (Tak Hingga Solusi) / Dependent – Infinitely Many Solutions

Dua persamaan merepresentasikan garis yang sama (berimpit).

**Kondisi:** $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$

Salah satu persamaan adalah kelipatan persamaan lainnya.

---

## 4. Metode Penyelesaian 2×2 / Methods for 2×2 Systems

### 4a. Metode Substitusi / Substitution Method

**Langkah:**
1. Isolasi satu variabel dari salah satu persamaan
2. Substitusikan ke persamaan lain
3. Selesaikan persamaan satu variabel
4. Back-substitute untuk mendapatkan variabel lainnya

**Contoh:**
$$\begin{cases} x + y = 5 \\ 2x - y = 1 \end{cases}$$

Dari persamaan 1: y = 5 - x
Substitusi: 2x - (5 - x) = 1 → 3x = 6 → x = 2
Back-substitute: y = 5 - 2 = 3
**Solusi: (2, 3)**

---

### 4b. Metode Eliminasi / Elimination Method

**Langkah:**
1. Kalikan persamaan agar koefisien salah satu variabel sama (atau berlawanan)
2. Tambahkan/kurangkan persamaan untuk eliminasi satu variabel
3. Selesaikan variabel yang tersisa
4. Back-substitute

**Contoh:**
$$\begin{cases} 3x + 2y = 12 \\ x - y = 1 \end{cases}$$

Kalikan persamaan 2 dengan 2: 2x - 2y = 2
Tambah persamaan 1: 3x + 2y + 2x - 2y = 12 + 2 → 5x = 14 → x = 14/5
Back-sub: y = x - 1 = 14/5 - 5/5 = 9/5
**Solusi: (14/5, 9/5)**

---

### 4c. Metode Grafik / Graphical Method

1. Tulis setiap persamaan dalam bentuk y = mx + b
2. Plot kedua garis
3. Titik potong adalah solusi

Metode ini akurat untuk nilai integer/simple fractions, namun kurang presisi untuk nilai desimal.

---

### 4d. Aturan Cramer / Cramer's Rule

Untuk sistem:
$$\begin{cases} a_1 x + b_1 y = c_1 \\ a_2 x + b_2 y = c_2 \end{cases}$$

**Determinan utama:**
$$D = \begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix} = a_1 b_2 - a_2 b_1$$

**Determinan x (ganti kolom x dengan kolom konstanta):**
$$D_x = \begin{vmatrix} c_1 & b_1 \\ c_2 & b_2 \end{vmatrix} = c_1 b_2 - c_2 b_1$$

**Determinan y (ganti kolom y dengan kolom konstanta):**
$$D_y = \begin{vmatrix} a_1 & c_1 \\ a_2 & c_2 \end{vmatrix} = a_1 c_2 - a_2 c_1$$

**Solusi (jika D ≠ 0):**
$$x = \frac{D_x}{D}, \quad y = \frac{D_y}{D}$$

**Catatan:**
- Jika D = 0 dan Dₓ = Dᵧ = 0: sistem dependen
- Jika D = 0 dan (Dₓ ≠ 0 atau Dᵧ ≠ 0): sistem inkonsisten

---

### 4e. Metode Matriks (Preview Eliminasi Gauss) / Matrix Method

Tulis sistem dalam bentuk matriks: **Ax = b**

$$\begin{pmatrix} a_1 & b_1 \\ a_2 & b_2 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} c_1 \\ c_2 \end{pmatrix}$$

**Augmented matrix:**
$$\left[\begin{array}{cc|c} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \end{array}\right]$$

Lakukan operasi baris dasar (ERO) untuk mencapai bentuk row echelon:
$$\left[\begin{array}{cc|c} 1 & 0 & x_0 \\ 0 & 1 & y_0 \end{array}\right]$$

---

## 5. Sistem 3 Variabel / Three-Variable Systems

$$\begin{cases} a_1 x + b_1 y + c_1 z = d_1 \\ a_2 x + b_2 y + c_2 z = d_2 \\ a_3 x + b_3 y + c_3 z = d_3 \end{cases}$$

**Interpretasi geometris:** Setiap persamaan adalah sebuah bidang (plane) dalam ruang 3D.

| Konfigurasi | Solusi |
|-------------|--------|
| Tiga bidang berpotongan di satu titik | Solusi unik (x, y, z) |
| Tiga bidang berpotongan di satu garis | Tak hingga solusi |
| Tiga bidang tidak punya titik persekutuan | Tidak ada solusi |

**Metode eliminasi bertahap:**
1. Eliminasi z dari persamaan 1 & 2 → persamaan baru (I)
2. Eliminasi z dari persamaan 1 & 3 → persamaan baru (II)
3. Selesaikan sistem 2×2 dari (I) dan (II)
4. Back-substitute untuk mendapatkan z

---

## 6. Soal Cerita / Word Problems

### Pola Umum:
1. **Identifikasi variabel** — apa yang tidak diketahui?
2. **Tulis persamaan** — terjemahkan kondisi ke persamaan
3. **Selesaikan sistem**
4. **Interpretasi** — pastikan jawaban masuk akal dalam konteks

### Jenis Masalah Umum:

**Masalah Campuran (Mixture):**
- "Berapa liter larutan 20% dan 50% harus dicampur untuk mendapat 30 liter larutan 30%?"
- x + y = 30  (total volume)
- 0.20x + 0.50y = 0.30(30)  (total solute)

**Masalah Kecepatan (Rate/Distance):**
- "Perahu menempuh 40 km searah arus dalam 2 jam, dan 20 km melawan arus dalam 2 jam"
- Searah: (v_perahu + v_arus) × 2 = 40
- Melawan: (v_perahu - v_arus) × 2 = 20

**Masalah Ekonomi (Supply/Demand):**
- Supply: P = 2Q + 5
- Demand: P = -Q + 20
- Equilibrium: 2Q + 5 = -Q + 20 → Q = 5, P = 15

---

## 7. Sistem Non-Linear / Non-Linear Systems

Sistem yang mengandung setidaknya satu persamaan non-linear.

**Contoh 1: Lingkaran dan Garis**
$$\begin{cases} x^2 + y^2 = 25 \\ y = x + 1 \end{cases}$$
Substitusikan y ke persamaan lingkaran → persamaan kuadrat dalam x.

**Contoh 2: Parabola dan Garis**
$$\begin{cases} y = x^2 - 3 \\ y = 2x \end{cases}$$
Set sama: x² - 3 = 2x → x² - 2x - 3 = 0 → (x-3)(x+1) = 0

**Kemungkinan Jumlah Solusi:**
- Lingkaran + garis: 0, 1, atau 2 solusi
- Parabola + garis: 0, 1, atau 2 solusi
- Dua parabola: 0, 1, 2, 3, atau 4 solusi

---

## 8. Aplikasi / Applications

### Ekonomi — Keseimbangan Pasar (Market Equilibrium):
- **Supply curve:** harga naik → produsen mau jual lebih banyak
- **Demand curve:** harga naik → konsumen mau beli lebih sedikit
- **Equilibrium:** titik potong supply dan demand

### Teknik Sipil — Analisis Rangka (Truss Analysis):
Setiap simpul memberikan 2 persamaan (keseimbangan gaya x dan y) → sistem besar.

### Kimia — Kesetimbangan Campuran:
Berapa gram setiap zat diperlukan untuk membuat campuran dengan komposisi tertentu.

### Fisika — Sirkuit Listrik (Kirchhoff's Laws):
Setiap loop memberikan satu persamaan → sistem persamaan linear.
