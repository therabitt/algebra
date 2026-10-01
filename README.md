# Phase 01 — Algebra (Aljabar) `[🟢 Fondasi]` `[⭐ SNBT]`

> **Landasan semua matematika.** Kuasai aljabar, dan semua cabang lain akan terbuka.
>
> *"If you can code it, you truly understand it."*

**Status:** ✅ Selesai — 19/19 topik · 114 file

---

## Daftar Topik — Urutan Belajar Final

| No   | Folder                                    | Topik                              | Tier       | Prasyarat | Status     |
|------|-------------------------------------------|------------------------------------|------------|-----------|------------|
| 1.01 | `01_Sets_and_Logic`                       | Himpunan & Logika                  | 🟦 Fondasi | —         | ✅ Selesai |
| 1.02 | `02_Number_Systems`                       | Sistem Bilangan                    | 🟦 Fondasi | 1.01      | ✅ Selesai |
| 1.03 | `03_Basic_Operations`                     | Operasi Dasar                      | 🟦 Fondasi | 1.02      | ✅ Selesai |
| 1.04 | `04_Algebraic_Expressions`                | Ekspresi Aljabar                   | 🟦 Fondasi | 1.03      | ✅ Selesai |
| 1.05 | `05_Absolute_Value`                       | Nilai Mutlak                       | 🟦 Fondasi | 1.02, 1.03| ✅ Selesai |
| 1.06 | `06_Linear_Equations`                     | Persamaan Linear                   | 🟩 Linear  | 1.04      | ✅ Selesai |
| 1.07 | `07_Linear_Inequalities`                  | Pertidaksamaan Linear              | 🟩 Linear  | 1.05, 1.06| ✅ Selesai |
| 1.08 | `08_Systems_of_Equations`                 | Sistem Persamaan                   | 🟩 Linear  | 1.06      | ✅ Selesai |
| 1.09 | `09_Factorization`                        | Faktorisasi                        | 🟧 Kuadrat | 1.04      | ✅ Selesai |
| 1.10 | `10_Quadratic_Equations`                  | Persamaan Kuadrat                  | 🟧 Kuadrat | 1.09      | ✅ Selesai |
| 1.11 | `11_Complex_Numbers`                      | Bilangan Kompleks                  | 🟧 Kuadrat | 1.10      | ✅ Selesai |
| 1.12 | `12_Quadratic_and_Rational_Inequalities`  | Pertidaksamaan Kuadrat & Rasional  | 🟧 Kuadrat | 1.07, 1.10, 1.15 | ✅ Selesai |
| 1.13 | `13_Functions_and_Relations`              | Fungsi & Relasi                    | 🟨 Fungsi  | 1.06, 1.10| ✅ Selesai |
| 1.14 | `14_Polynomials`                          | Polinomial                         | 🟨 Fungsi  | 1.13, 1.09| ✅ Selesai |
| 1.15 | `15_Rational_Expressions`                 | Pecahan Aljabar                    | 🟨 Fungsi  | 1.14, 1.09| ✅ Selesai |
| 1.16 | `16_Exponents_and_Logarithms`             | Eksponen & Logaritma               | 🟨 Fungsi  | 1.13      | ✅ Selesai |
| 1.17 | `17_Sequences_and_Series`                 | Barisan & Deret                    | 🟥 Lanjut  | 1.13, 1.16| ✅ Selesai |
| 1.18 | `18_Binomial_Theorem`                     | Teorema Binomial                   | 🟥 Lanjut  | 1.01, 1.17| ✅ Selesai |
| 1.19 | `19_Basic_Matrices`                       | Matriks Dasar                      | 🟥 Lanjut  | 1.08      | ✅ Selesai |

---

## Dependency Map

```
01_Sets_and_Logic
    │
    ▼
02_Number_Systems
    │
    ├──────────────────────┐
    ▼                      ▼
03_Basic_Operations    05_Absolute_Value
    │                      │
    └──────────┬───────────┘
               ▼
        04_Algebraic_Expressions
               │
    ┌──────────┤
    │          ▼
    │    06_Linear_Equations ─────────► 08_Systems_of_Equations ──► 19_Basic_Matrices
    │          │
    │          ▼
    │    07_Linear_Inequalities
    │          │
    └──► 09_Factorization
               │
               ▼
         10_Quadratic_Equations ──────► 11_Complex_Numbers
               │
               ▼
         12_Quad. & Rat. Inequalities
               │
               ▼
         13_Functions_and_Relations
         ┌─────┼──────────┐
         ▼     ▼          ▼
       14_Poly 15_Rational 16_Exp & Log
               │
               └─────────► 17_Sequences_and_Series
                                    │
                                    ▼
                           18_Binomial_Theorem
```

---

## Logika 5 Tier

> Tier di bawah adalah pengelompokan internal Phase 1 — berbeda dari level global kurikulum.
> Phase 01 secara keseluruhan berada di level **[🟢 Fondasi]** setara SMA / SNBT.

### 🟦 Tier 1 — Fondasi (Topik 1.01–1.05)
Tidak butuh prasyarat aljabar apapun. Ini adalah **bahasa dan bilangan** — fondasi paling dasar.
- **1.01 Sets & Logic** — cara berpikir matematis (proposisi, himpunan, kuantifikasi)
- **1.02 Number Systems** — jenis bilangan: ℕ, ℤ, ℚ, ℝ, ℂ
- **1.03 Basic Operations** — +, −, ×, ÷ dan sifat-sifatnya (GCD, LCM)
- **1.04 Algebraic Expressions** — menggeneralisasi angka ke variabel x, y
- **1.05 Absolute Value** — sifat bilangan, jarak, norma

### 🟩 Tier 2 — Linear (Topik 1.06–1.08)
Belajar menyelesaikan persamaan satu variabel, lalu dua variabel secara bersamaan.
- **1.06 Linear Equations** — ax + b = c — paling dasar
- **1.07 Linear Inequalities** — ax + b > c — ekstensi dengan tanda
- **1.08 Systems of Equations** — dua persamaan, dua variabel (substitusi & eliminasi)

> ℹ️ *Mengapa Systems ada di sini?* Sistem 2×2 linear **hanya butuh Persamaan Linear** — cukup substitusi & eliminasi. Matriks adalah alat lanjut yang dipelajari di 1.19 setelah ada konteks.

### 🟧 Tier 3 — Kuadrat (Topik 1.09–1.12)
Naik ke derajat 2: faktorisasi → kuadrat → kompleks → pertidaksamaan.
- **1.09 Factorization** — HARUS sebelum kuadrat! GCF, a²−b², completing the square
- **1.10 Quadratic Equations** — gunakan faktorisasi + rumus ABC
- **1.11 Complex Numbers** — muncul alami saat D < 0: `√(negatif)` = bilangan kompleks
- **1.12 Quad. & Rational Inequalities** — sign chart, |f(x)| > g(x)

> ℹ️ *Mengapa Complex ada di sini?* Bilangan kompleks **paling natural diperkenalkan** saat diskriminan negatif muncul di quadratic. Euler formula (e^iθ) adalah topik lanjut dalam modul kompleks itu sendiri.

### 🟨 Tier 4 — Fungsi (Topik 1.13–1.16)
Abstraksi ke konsep fungsi, lalu tiga cabang paralel yang bisa dipelajari dalam urutan bebas.
- **1.13 Functions & Relations** — domain, range, komposisi, invers ← WAJIB dulu
- **1.14 Polynomials** — generalisasi kuadrat ke derajat n (paralel dari 1.13)
- **1.15 Rational Expressions** — polinomial dalam pecahan (paralel dari 1.13)
- **1.16 Exponents & Logarithms** — operasi baru: aˣ dan logₐ(x) (paralel dari 1.13)

> ℹ️ *Topik 1.14, 1.15, 1.16 bisa dipelajari dalam urutan bebas* — ketiganya langsung extend dari Functions tanpa saling bergantung satu sama lain.

### 🟥 Tier 5 — Lanjut (Topik 1.17–1.19)
Topik-topik yang membutuhkan pemahaman matang dari tier sebelumnya.
- **1.17 Sequences & Series** — pola bilangan, konvergensi, Σ
- **1.18 Binomial Theorem** — ekspansi (a+b)ⁿ, distribusi binomial
- **1.19 Basic Matrices** — representasi matriks dari sistem, transformasi 2D

---

## Panduan Memulai

```bash
# Mulai dari Tier 1:
cd /home/therabitt/Projects/Math/01_Algebra/01_Sets_and_Logic

# Baca teori:
cat theory.md

# Jalankan contoh:
python3 examples.py

# Kerjakan latihan:
python3 exercises.py

# Visualisasi:
python3 visualizations.py

# Challenge lanjut:
python3 challenge.py

# Lanjut ke topik berikutnya:
cd ../02_Number_Systems
```

### Alur Pembelajaran Per Topik

```
[1] Baca README.md           → Orientasi topik
[2] Baca theory.md           → Pahami konsep mendalam
[3] Jalankan examples.py     → Lihat kode berjalan
[4] Kerjakan exercises.py    → Uji pemahaman
[5] Jalankan visualizations.py → Visualisasi konsep
[6] Coba challenge.py        → Tantang diri sendiri
[7] Buat catatan notes.md    → Insight yang didapat tentang materi
[8] Lanjut ke topik berikutnya
```

### Checklist Per Topik
- [ ] README.md (overview, 2 menit)
- [ ] theory.md (konsep + formula lengkap)
- [ ] examples.py (jalankan, pahami komentar)
- [ ] exercises.py (kerjakan SENDIRI dulu baru lihat jawaban)
- [ ] visualizations.py (lihat grafik)
- [ ] challenge.py (implementasi dari nol — tes sesungguhnya!)
- [ ] notes.md (tulis insight & catatan pribadi)
- [ ] Lanjut ke topik berikutnya ✅

---

## Estimasi Waktu

| Tier       | Topik    | Estimasi    |
|------------|----------|-------------|
| 🟦 Fondasi | 5 topik  | 2–3 hari    |
| 🟩 Linear  | 3 topik  | 2–3 hari    |
| 🟧 Kuadrat | 4 topik  | 3–5 hari    |
| 🟨 Fungsi  | 4 topik  | 3–5 hari    |
| 🟥 Lanjut  | 3 topik  | 3–4 hari    |
| **Total**  | **19 topik** | **~2–3 minggu** |

---

## Teknologi

```
Python 3.x         — bahasa utama
math, fractions    — built-in standard library
numpy              — komputasi numerik
sympy              — matematika simbolik
matplotlib         — visualisasi grafis
scipy              — metode numerik lanjutan
```

Install: `pip install numpy sympy matplotlib scipy`

---

## Struktur Setiap Topik

```
XX_Topic_Name/
├── README.md           ← Ringkasan, learning objectives
├── theory.md           ← Teori lengkap, definisi, sifat, rumus
├── examples.py         ← Kode contoh terdokumentasi
├── exercises.py        ← Latihan soal dengan petunjuk dan jawaban
├── visualizations.py   ← Visualisasi matplotlib
├── challenge.py        ← Tantangan tingkat lanjut
└── notes.md            ← Catatan pribadi tentang materi yang dipelajari
```

---

## Lanjut ke Phase Berikutnya

Setelah menyelesaikan semua 19 topik Aljabar, kamu siap untuk phase-phase yang prasyarat langsungnya ada di sini:

| Phase | Topik | Prasyarat dari Aljabar |
|-------|-------|------------------------|
| Phase 02: Geometry      | Koordinat, vektor, transformasi | Fungsi, Sistem Persamaan, Matriks |
| Phase 03: Trigonometry  | sin/cos/tan, identitas          | Fungsi, Bilangan Kompleks, Eksponen |
| Phase 04: Calculus      | Limit, turunan, integral        | SEMUA — terutama Fungsi & Eksponen |
| Phase 05: Statistics    | Distribusi, probabilitas        | Barisan, Binomial, Eksponen |
| Phase 06: Linear Algebra | Ruang vektor, eigenvalue       | Matriks, Sistem Persamaan |
| Phase 07: Discrete Math | Logika, graf, kombinatorik      | Sets & Logic, Bilangan, Barisan |

> Phase 08 ke atas tidak langsung bergantung pada Aljabar — prasyaratnya ada di phase-phase di atas.

---

*Phase 01 — 19 Topik · 114 File | MathCode Learning Project | v3.1.0 — September 2026*
