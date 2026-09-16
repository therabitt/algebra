# Teori: Pertidaksamaan Linear (Theory: Linear Inequalities)

## 1. Definisi Pertidaksamaan / Definition of Inequality

**Pertidaksamaan (Inequality):** Pernyataan matematika yang membandingkan dua ekspresi menggunakan tanda ketidaksamaan.

| Simbol | Dibaca (ID) | Read (EN) | Contoh |
|--------|-------------|-----------|--------|
| **<** | kurang dari | less than | x < 5 |
| **>** | lebih dari | greater than | x > -2 |
| **≤** | kurang dari atau sama dengan | less than or equal to | x ≤ 3 |
| **≥** | lebih dari atau sama dengan | greater than or equal to | x ≥ 0 |
| **≠** | tidak sama dengan | not equal to | x ≠ 4 |

**Perbedaan penting dengan persamaan:**
- Persamaan → satu (atau beberapa) nilai solusi spesifik
- Pertidaksamaan → **himpunan solusi** berupa interval atau region

---

## 2. Sifat-Sifat Pertidaksamaan / Properties of Inequalities

### A. Sifat Tambah / Addition Property
```
Jika a < b, maka a + c < b + c  (untuk semua c)
Contoh: x - 3 < 5  →  x - 3 + 3 < 5 + 3  →  x < 8
```

### B. Sifat Kurang / Subtraction Property
```
Jika a < b, maka a - c < b - c  (untuk semua c)
Contoh: x + 4 > 9  →  x + 4 - 4 > 9 - 4  →  x > 5
```

### C. Sifat Kali — Bilangan POSITIF / Multiplication by POSITIVE
```
Jika a < b dan c > 0, maka a·c < b·c
(TANDA TIDAK BERUBAH!)
Contoh: x/3 < 4  →  x < 12
```

### D. Sifat Kali — Bilangan NEGATIF ⚠️ PEMBALIKAN TANDA!
```
Jika a < b dan c < 0, maka a·c > b·c
(TANDA BERUBAH ARAH!)

Contoh: -2x < 6
  x > 6/(-2)
  x > -3   ← tanda berubah dari < menjadi >
```

**KUNCI:** Kalikan atau bagi dengan bilangan negatif → BALIK TANDA PERTIDAKSAMAAN!

### E. Sifat Transitif / Transitive Property
```
Jika a < b dan b < c, maka a < c
```

### F. Sifat Invers / Inverse Property
```
Jika a < b, maka b > a
```

### G. Sifat Perbandingan / Comparison of Reciprocals
```
Jika 0 < a < b, maka 1/b < 1/a  (urutan terbalik untuk bilangan positif)
Jika a < b < 0, maka 1/b > 1/a
```

---

## 3. Menyelesaikan Pertidaksamaan Linear Satu Variabel

### Prosedur (sama dengan persamaan, kecuali aturan pembalikan tanda):
1. Sederhanakan setiap ruas
2. Pindahkan variabel ke satu ruas
3. Pindahkan konstanta ke ruas lain
4. Bagi dengan koefisien (PERHATIKAN TANDA!)

### Contoh:
```
Selesaikan: -3x + 7 > 1

  -3x > 1 - 7
  -3x > -6
  x < -6/(-3)   ← TANDA BERUBAH karena bagi dengan -3!
  x < 2

Himpunan solusi: {x | x < 2} atau (-∞, 2)
```

---

## 4. Pertidaksamaan Majemuk / Compound Inequalities

### AND (Konjungsi / Irisan ∩):
Kedua kondisi harus terpenuhi.
```
2 < x ≤ 7   (sama dengan: x > 2 DAN x ≤ 7)
Dibaca: "x berada di antara 2 dan 7, 2 tidak termasuk, 7 termasuk"
Solusi: interval (2, 7]
```

### OR (Disjungsi / Gabungan ∪):
Setidaknya satu kondisi terpenuhi.
```
x < -1 ATAU x > 3
Solusi: (-∞, -1) ∪ (3, +∞)
```

### Contoh AND:
```
Selesaikan: -4 < 2x + 2 ≤ 10

Bagi menjadi dua:
  -4 < 2x + 2   DAN   2x + 2 ≤ 10
  -6 < 2x             2x ≤ 8
  -3 < x              x ≤ 4

Solusi: -3 < x ≤ 4  atau  (-3, 4]
```

### Contoh OR:
```
Selesaikan: 3x - 1 < 5 ATAU 2x + 3 > 11

  3x < 6        2x > 8
  x < 2   ATAU  x > 4

Solusi: (-∞, 2) ∪ (4, +∞)
```

---

## 5. Pertidaksamaan Nilai Mutlak / Absolute Value Inequalities

**Definisi nilai mutlak:**
```
|x| = x   jika x ≥ 0
|x| = -x  jika x < 0
```

### Tipe 1: |x| < a  (a > 0) → "Lebih Dekat"
```
|x| < a  ↔  -a < x < a

Contoh: |2x - 3| < 7
  -7 < 2x - 3 < 7
  -7 + 3 < 2x < 7 + 3
  -4 < 2x < 10
  -2 < x < 5
  Solusi: (-2, 5)
```

### Tipe 2: |x| > a  (a > 0) → "Lebih Jauh"
```
|x| > a  ↔  x < -a  ATAU  x > a

Contoh: |3x + 1| > 5
  3x + 1 < -5   ATAU   3x + 1 > 5
  3x < -6       ATAU   3x > 4
  x < -2        ATAU   x > 4/3
  Solusi: (-∞, -2) ∪ (4/3, +∞)
```

### Tipe 3: |x| = a  → Dua kasus
```
|x| = a  ↔  x = a  ATAU  x = -a
```

### Kasus khusus:
```
|x| < 0  → Tidak ada solusi (nilai mutlak selalu ≥ 0)
|x| ≥ 0  → Semua bilangan real (selalu benar)
|x| ≤ 0  → Hanya x = 0
```

---

## 6. Representasi pada Garis Bilangan / Number Line Representation

```
Simbol  | Titik pada garis bilangan
--------|---------------------------
x < a   | Tanda panah ke kiri dari a (lingkaran kosong ○ di a)
x > a   | Tanda panah ke kanan dari a (lingkaran kosong ○ di a)
x ≤ a   | Tanda panah ke kiri dari a (lingkaran penuh ● di a)
x ≥ a   | Tanda panah ke kanan dari a (lingkaran penuh ● di a)

Contoh: x ≤ 3
  ←—————●
       3

Contoh: -2 < x ≤ 5
     ○——————————●
    -2          5
```

---

## 7. Notasi Interval / Interval Notation

| Pertidaksamaan | Notasi Interval | Grafik Garis Bilangan |
|----------------|-----------------|----------------------|
| a < x < b | (a, b) | ○——○ |
| a ≤ x ≤ b | [a, b] | ●——● |
| a ≤ x < b | [a, b) | ●——○ |
| a < x ≤ b | (a, b] | ○——● |
| x > a | (a, +∞) | ○→ |
| x ≥ a | [a, +∞) | ●→ |
| x < a | (-∞, a) | ←○ |
| x ≤ a | (-∞, a] | ←● |
| Semua real | (-∞, +∞) | ←→ |

**Catatan:** Tanda kurung `( )` = terbuka (tidak termasuk), `[ ]` = tertutup (termasuk)

---

## 8. Pertidaksamaan Linear Dua Variabel / Linear Inequalities in Two Variables

**Bentuk:** `ax + by < c`  (atau ≤, >, ≥)

**Solusi:** Himpunan semua pasangan (x, y) yang memenuhi pertidaksamaan.

### Langkah menyelesaikan:
1. Gambar garis batas: `ax + by = c`
   - Jika < atau >: garis putus-putus (titik tidak termasuk)
   - Jika ≤ atau ≥: garis penuh (titik termasuk)
2. Pilih titik uji (biasanya (0,0) jika tidak pada garis)
3. Substitusikan ke pertidaksamaan
   - Benar → arsir daerah yang mengandung titik uji
   - Salah → arsir daerah lainnya

### Contoh:
```
Gambarkan: 2x + y < 4

Garis batas: 2x + y = 4
  (saat x=0: y=4) → (0,4)
  (saat y=0: 2x=4, x=2) → (2,0)

Titik uji (0,0): 2(0) + 0 < 4 → 0 < 4  ✓ BENAR

Arsir daerah yang mengandung (0,0) → di bawah garis putus-putus
```

---

## 9. Sistem Pertidaksamaan Linear / System of Linear Inequalities

**Definisi:** Kumpulan dua atau lebih pertidaksamaan linear yang harus dipenuhi secara bersamaan.

**Solusi:** Irisan (intersection) dari semua himpunan solusi individual.

```
Contoh sistem:
  x + y ≤ 6
  x - y ≥ 0
  x ≥ 0
  y ≥ 0

Setiap pertidaksamaan mendefinisikan setengah-bidang (half-plane).
Solusi sistem = irisan semua setengah-bidang = daerah poligon.
```

---

## 10. Daerah Feasible / Feasible Region

**Definisi:** Daerah pada bidang koordinat yang memenuhi semua pertidaksamaan dalam sistem (termasuk batasan non-negatif jika ada).

**Sifat-sifat:**
- Bisa berupa daerah terbatas (bounded) atau tak terbatas (unbounded)
- Titik-titik sudut (corner points / vertices) adalah titik potong garis-garis batas
- Dalam pemrograman linear, solusi optimal terjadi di titik sudut

---

## 11. Pengantar Pemrograman Linear / Introduction to Linear Programming

**Definisi:** Teknik optimasi untuk memaksimumkan atau meminimumkan fungsi tujuan linear, dengan kendala berbentuk pertidaksamaan linear.

### Komponen:
```
1. Fungsi Tujuan (Objective Function): f(x,y) = ax + by
   → Ingin dimaksimumkan (profit, produksi) atau diminimumkan (biaya)

2. Kendala (Constraints): pertidaksamaan linear
   → Misal: x + y ≤ 100, 2x + y ≤ 150, x ≥ 0, y ≥ 0

3. Daerah Feasible: semua (x,y) yang memenuhi semua kendala

4. Solusi Optimal: titik pada daerah feasible yang memaksimum/minimumkan f
```

### Teorema Dasar (Fundamental Theorem of LP):
> Jika solusi optimal ada, maka solusi tersebut terjadi di salah satu titik sudut (vertex) dari daerah feasible.

### Langkah Penyelesaian:
1. Tentukan variabel keputusan
2. Tulis fungsi tujuan
3. Tuliskan semua kendala sebagai pertidaksamaan
4. Gambar daerah feasible
5. Temukan semua titik sudut
6. Evaluasi fungsi tujuan di setiap titik sudut
7. Pilih titik yang memaksimum/minimumkan f

### Contoh Sederhana:
```
Maksimumkan: Z = 3x + 5y
Kendala:
  x + y ≤ 4
  x + 3y ≤ 6
  x ≥ 0, y ≥ 0

Titik sudut:
  A = (0, 0): Z = 0
  B = (4, 0): Z = 12
  C = (3, 1): Z = 14   ← MAKSIMUM
  D = (0, 2): Z = 10

Solusi optimal: x=3, y=1, Z_max=14
```

---

## Ringkasan Aturan Kritis / Summary of Critical Rules

| Aturan | Detail |
|--------|--------|
| Tambah/kurang kedua ruas | Tanda TIDAK berubah |
| Kali/bagi dengan positif | Tanda TIDAK berubah |
| **Kali/bagi dengan negatif** | **Tanda BERUBAH ARAH** ⚠️ |
| \|x\| < a | -a < x < a |
| \|x\| > a | x < -a ATAU x > a |
| AND | Irisan (∩) interval |
| OR | Gabungan (∪) interval |
| Kurung () | Titik tidak termasuk (open) |
| Kurung [] | Titik termasuk (closed) |
