# Teori: Persamaan Linear (Theory: Linear Equations)

## 1. Definisi: Persamaan vs Ekspresi vs Pertidaksamaan

| Jenis | Simbol | Contoh | Deskripsi |
|-------|--------|--------|-----------|
| **Ekspresi** | (tidak ada = atau ineq.) | 3x + 5 | Dapat disederhanakan/dievaluasi |
| **Persamaan** | = | 3x + 5 = 11 | Dapat diselesaikan |
| **Pertidaksamaan** | <, >, ≤, ≥ | 3x + 5 > 11 | Menghasilkan himpunan solusi |

---

## 2. Persamaan Linear: Definisi dan Bentuk Standar

**Definisi:** Persamaan yang setiap suku variabelnya berderajat tepat 1 (tidak ada x², x³, xy, dll.).

### Satu Variabel:
```
Bentuk standar: ax + b = c
di mana a ≠ 0, dan a, b, c adalah bilangan real.

Contoh:
  2x + 3 = 11         ✓ linear
  5y - 7 = 2y + 1     ✓ linear
  x² + 1 = 5          ✗ bukan linear (ada x²)
  3/x + 1 = 2         ✗ bukan linear (x di penyebut)
```

### Dua Variabel:
```
Bentuk standar: ax + by = c
di mana a, b tidak keduanya nol.

Contoh: 2x + 3y = 12, y = 4x - 1
```

---

## 3. Sifat-Sifat Kesetaraan / Properties of Equality

Sifat-sifat ini memungkinkan kita memanipulasi persamaan sambil mempertahankan kesetaraan:

### A. Sifat Tambah / Addition Property
```
Jika a = b, maka a + c = b + c
Contoh: x - 3 = 7  →  x - 3 + 3 = 7 + 3  →  x = 10
```

### B. Sifat Kurang / Subtraction Property
```
Jika a = b, maka a - c = b - c
Contoh: x + 5 = 12  →  x + 5 - 5 = 12 - 5  →  x = 7
```

### C. Sifat Kali / Multiplication Property
```
Jika a = b, maka a · c = b · c  (c ≠ 0)
Contoh: x/4 = 3  →  (x/4) · 4 = 3 · 4  →  x = 12
```

### D. Sifat Bagi / Division Property
```
Jika a = b, maka a/c = b/c  (c ≠ 0)
Contoh: 5x = 20  →  5x/5 = 20/5  →  x = 4
```

### E. Sifat Refleksif / Reflexive Property
```
a = a  (setiap bilangan sama dengan dirinya sendiri)
```

### F. Sifat Simetri / Symmetric Property
```
Jika a = b, maka b = a
```

### G. Sifat Transitif / Transitive Property
```
Jika a = b dan b = c, maka a = c
```

---

## 4. Menyelesaikan Persamaan Linear Satu Variabel / Solving Linear Equations

### Prosedur Umum:
1. **Sederhanakan** setiap ruas (hilangkan tanda kurung, gabungkan suku sejenis)
2. **Pindahkan** semua suku variabel ke satu ruas
3. **Pindahkan** semua konstanta ke ruas lain
4. **Bagi** kedua ruas dengan koefisien variabel
5. **Verifikasi** solusi dengan substitusi kembali

### Contoh Bertahap:
```
Selesaikan: 3(2x - 4) + 5 = 2x + 9

Langkah 1: Hilangkan tanda kurung
  6x - 12 + 5 = 2x + 9

Langkah 2: Sederhanakan ruas kiri
  6x - 7 = 2x + 9

Langkah 3: Pindahkan suku variabel ke kiri
  6x - 2x - 7 = 9
  4x - 7 = 9

Langkah 4: Pindahkan konstanta ke kanan
  4x = 9 + 7
  4x = 16

Langkah 5: Bagi dengan koefisien
  x = 4

Verifikasi: 3(2·4 - 4) + 5 = 3(4) + 5 = 12 + 5 = 17
            2·4 + 9 = 8 + 9 = 17 ✓
```

---

## 5. Persamaan Tanpa Solusi (Kontradiksi) / No Solution (Contradiction)

Ketika proses penyelesaian menghasilkan pernyataan yang **selalu salah**:

```
Selesaikan: 2x + 3 = 2x + 7

  2x - 2x = 7 - 3
  0 = 4   ← KONTRADIKSI! Tidak ada nilai x yang memenuhi ini.

Himpunan solusi: ∅ (himpunan kosong)
```

---

## 6. Persamaan dengan Solusi Tak Hingga (Identitas) / Infinite Solutions (Identity)

Ketika proses penyelesaian menghasilkan pernyataan yang **selalu benar**:

```
Selesaikan: 3(x + 2) = 3x + 6

  3x + 6 = 3x + 6
  0 = 0   ← SELALU BENAR! Berlaku untuk semua nilai x.

Himpunan solusi: ℝ (semua bilangan real)
```

---

## 7. Persamaan Literal / Literal Equations

**Definisi:** Persamaan yang mengandung lebih dari satu variabel (huruf). Kita menyelesaikannya dengan mengisolasi variabel tertentu.

### Contoh Fisika/Matematika:
```
Rumus luas persegi panjang: A = l × w
→ Selesaikan untuk w: w = A/l

Rumus kecepatan: v = d/t
→ Selesaikan untuk t: t = d/v

Rumus suhu: F = (9/5)C + 32
→ Selesaikan untuk C:
  F - 32 = (9/5)C
  C = (5/9)(F - 32)

Persamaan garis: y = mx + b
→ Selesaikan untuk x: x = (y - b)/m
```

---

## 8. Persamaan Linear Dua Variabel / Linear Equations in Two Variables

**Bentuk:** `ax + by = c`

**Solusi:** Pasangan terurut (x, y) yang memenuhi persamaan.

```
Untuk 2x + y = 8:
  Jika x = 0: 2(0) + y = 8 → y = 8  → titik (0, 8)
  Jika x = 1: 2(1) + y = 8 → y = 6  → titik (1, 6)
  Jika x = 4: 2(4) + y = 8 → y = 0  → titik (4, 0)
```

Semua solusi membentuk **garis lurus** pada bidang koordinat.

---

## 9. Himpunan Solusi dan Ruang Solusi / Solution Sets

**Persamaan satu variabel:** Solusi adalah satu nilai (titik pada garis bilangan)
```
2x + 3 = 11 → x = 4   →   solusi: {4}
```

**Persamaan dua variabel:** Solusi adalah tak-hingga banyak pasangan (garis pada bidang)
```
2x + y = 8 → solusi: {(x, y) | 2x + y = 8}
```

---

## 10. Proporsi dan Perkalian Silang / Proportions and Cross Multiplication

**Proporsi:** Pernyataan bahwa dua pecahan bernilai sama.
```
a/b = c/d
```

**Perkalian Silang (Cross Multiplication):**
```
a/b = c/d  →  a·d = b·c

Contoh: (x+1)/3 = (2x-1)/5
  5(x+1) = 3(2x-1)
  5x + 5 = 6x - 3
  5 + 3 = 6x - 5x
  x = 8
```

---

## 11. Translasi Soal Cerita / Word Problem Translation

| Kata Kunci (ID) | Keyword (EN) | Operasi |
|-----------------|--------------|---------|
| Jumlah dari | Sum of | + |
| Selisih dari | Difference of | - |
| Hasil kali dari | Product of | × |
| Hasil bagi dari | Quotient of | ÷ |
| Lebih dari | More than | + |
| Kurang dari | Less than / fewer | - |
| Tiga kali | Three times | 3× |
| Setengah dari | Half of | ×(1/2) |
| Sama dengan | Equals / is | = |

### Strategi:
1. Baca soal dengan teliti
2. Identifikasi apa yang tidak diketahui → buat variabel
3. Identifikasi hubungan matematis
4. Buat persamaan
5. Selesaikan
6. Verifikasi jawaban terhadap konteks soal

---

## 12. Masalah Jarak-Waktu-Kecepatan / Distance-Rate-Time Problems

**Rumus dasar:** `d = r · t`
(distance = rate × time)

**Tipe umum:**
```
Dua objek bergerak berlawanan arah:
  d₁ + d₂ = total_jarak
  r₁·t + r₂·t = D

Dua objek bergerak arah sama (kejar-kejaran):
  d₁ = d₂
  r₁·t₁ = r₂·t₂

Perjalanan pulang-pergi (rata-rata kecepatan):
  v_avg = 2v₁v₂/(v₁+v₂)
```

**Contoh:**
```
Dua kereta berangkat dari dua kota berjarak 300 km, bergerak saling mendekati.
Kereta A: 60 km/jam, Kereta B: 90 km/jam.
Kapan bertemu?

  60t + 90t = 300
  150t = 300
  t = 2 jam
```

---

## 13. Masalah Campuran / Mixture Problems

**Rumus:** `(konsentrasi₁)(volume₁) + (konsentrasi₂)(volume₂) = (konsentrasi_akhir)(volume_akhir)`

**Contoh:**
```
Berapa liter larutan 30% asam harus dicampur dengan 8 liter larutan 60% asam
untuk mendapat larutan 50%?

Misal: x liter larutan 30%

  0.30x + 0.60(8) = 0.50(x + 8)
  0.30x + 4.80 = 0.50x + 4.00
  0.80 = 0.20x
  x = 4 liter
```

---

## 14. Masalah Usia / Age Problems

**Strategi:** Definisikan usia sekarang, usia masa lalu = usia_sekarang - n, usia masa depan = usia_sekarang + n

**Contoh:**
```
Umur Andi 3 kali umur Budi. Dalam 10 tahun, umur Andi 2 kali umur Budi.
Berapa umur mereka sekarang?

Misal: umur Budi = x, umur Andi = 3x

Dalam 10 tahun: 3x + 10 = 2(x + 10)
  3x + 10 = 2x + 20
  x = 10

Budi: 10 tahun, Andi: 30 tahun
```

---

## 15. Masalah Geometri / Geometric Problems

**Rumus yang sering digunakan:**
```
Persegi panjang: P = 2(p + l),  L = p × l
Segitiga:        P = a + b + c, L = (1/2) × a × t
Lingkaran:       K = 2πr,       L = πr²
```

**Contoh:**
```
Panjang sebuah persegi panjang 5 lebih dari lebarnya.
Kelilingnya 38. Temukan dimensinya.

Misal: lebar = x, panjang = x + 5

2(x + x + 5) = 38
2(2x + 5) = 38
4x + 10 = 38
4x = 28
x = 7

Lebar = 7, Panjang = 12
Verifikasi: 2(7 + 12) = 2(19) = 38 ✓
```

---

## Ringkasan / Summary

| Topik | Kunci |
|-------|-------|
| Persamaan linear | ax + b = c, solusi tunggal |
| Kontradiksi | 0 = c (c ≠ 0), tidak ada solusi |
| Identitas | 0 = 0, solusi tak hingga |
| Persamaan literal | Isolasi variabel tertentu |
| Proporsi | a/b = c/d ↔ ad = bc |
| Masalah d-r-t | d = rt |
| Masalah campuran | c₁v₁ + c₂v₂ = c_f·v_f |
