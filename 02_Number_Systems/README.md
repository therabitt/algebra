# 📊 Topic 1.1: Number Systems (Sistem Bilangan)

> Fondasi dari semua matematika — memahami jenis-jenis bilangan dan hubungannya.
> The foundation of all mathematics — understanding types of numbers and their relationships.

---

## Apa itu Sistem Bilangan? / What are Number Systems?

**Bahasa Indonesia:**
Sistem bilangan adalah cara kita mengklasifikasikan dan mengorganisir bilangan berdasarkan sifat-sifatnya. Setiap "jenis" bilangan memiliki properti yang unik dan membentuk hierarki yang indah: dari bilangan paling sederhana (bilangan asli) hingga yang paling kompleks (bilangan kompleks).

**English:**
A number system is how we classify and organize numbers based on their properties. Each "type" of number has unique properties and forms a beautiful hierarchy: from the simplest numbers (natural numbers) to the most complex (complex numbers).

---

## 🔢 Jenis-Jenis Bilangan / Types of Numbers

### 1. Bilangan Asli / Natural Numbers (N)
Bilangan yang digunakan untuk menghitung: {1, 2, 3, 4, 5, ...}

### 2. Bilangan Cacah / Whole Numbers (W)
Bilangan asli ditambah nol: {0, 1, 2, 3, 4, ...}

### 3. Bilangan Bulat / Integers (Z)
Semua bilangan bulat positif, nol, dan negatif: {..., -3, -2, -1, 0, 1, 2, 3, ...}

### 4. Bilangan Rasional / Rational Numbers (Q)
Bilangan yang dapat dinyatakan sebagai p/q dimana p, q termasuk Z dan q != 0.
p = pembilang/ numerator
q = penyebut/ denominator
Contoh: 1/2, -3/4, 0.75, 0.333..., 5

### 5. Bilangan Irasional / Irrational Numbers
Bilangan nyata yang TIDAK dapat dinyatakan sebagai p/q.
ciri utama: jika diubah ke bentuk desimal angka di belakang koma tidak akan pernah habis dan polanya acak (tidak berulang)
Contoh: sqrt(2), pi, e, sqrt(3), phi (golden ratio)

### 6. Bilangan Nyata / Real Numbers (R)
Semua bilangan rasional DAN irasional. Mencakup seluruh garis bilangan.

### 7. Bilangan Kompleks / Complex Numbers (C)
Bilangan dalam bentuk a + bi, dimana a, b termasuk R dan i = sqrt(-1).
Contoh: 3 + 4i, -1 + 2i, 5 + 0i (= 5)

---

## Hierarki Sistem Bilangan / Number System Hierarchy

```
C (Complex Numbers / Bilangan Kompleks)
|
+-- R (Real Numbers / Bilangan Nyata)
|   |
|   +-- Q (Rational Numbers / Bilangan Rasional)
|   |   |
|   |   +-- Z (Integers / Bilangan Bulat)
|   |   |   |
|   |   |   +-- W (Whole Numbers / Bilangan Cacah)
|   |   |   |   |
|   |   |   |   +-- N (Natural Numbers / Bilangan Asli)
|   |   |   |       {1, 2, 3, 4, 5, ...}
|   |   |   |
|   |   |   +-- Negative Integers: {..., -3, -2, -1}
|   |   |
|   |   +-- Non-integer Rationals: {1/2, 3/4, -2/5, ...}
|   |
|   +-- Irrational Numbers: {sqrt(2), pi, e, sqrt(3), phi, ...}
|
+-- Non-real Complex: {3+4i, -1+2i, 0+i, ...}

Subset Relations: N c W c Z c Q c R c C
```

---

## Apa yang Akan Kamu Pelajari / What You Will Learn

Setelah menyelesaikan topik ini, kamu akan mampu:

- [x] Mengklasifikasikan bilangan ke dalam sistem yang tepat
- [ ] Memahami mengapa setiap subset ada dan apa yang ditambahkannya
- [ ] Melakukan operasi pada setiap jenis bilangan menggunakan Python
- [x] Membuktikan bahwa sqrt(2) adalah irasional secara algoritmik
- [ ] Bekerja dengan bilangan kompleks dan bidang kompleks
- [ ] Memahami representasi desimal dan pecahan berulang
- [ ] Menggunakan notasi interval dan fungsi lantai/langit-langit
- [ ] Memvisualisasikan hierarki dan properti bilangan

---

## File yang Disertakan / Files Included

| File | Tujuan |
|---|---|
| README.md | Gambaran umum topik ini (file ini) |
| theory.md | Teori mendalam: definisi formal, aksioma, bukti |
| examples.py | Implementasi Python lengkap dari semua konsep |
| exercises.py | 10+ soal latihan dengan petunjuk dan solusi |
| visualizations.py | Visualisasi matplotlib: garis bilangan, diagram Venn, bidang kompleks |
| challenge.py | Tantangan lanjutan: implementasi kelas Fraction kustom, dll. |
| notes.md | Catatan pribadi mengenai topik yang dipelajari |
| proof_sqrt2_irrational.py | Pembuktian formal dan komputasional bahwa √2 irasional (proof by contradiction) |


---

## Estimasi Waktu / Time Estimate

- Membaca README + Theory: ~45 menit
- Menjalankan & memahami examples.py: ~45 menit
- Mengerjakan exercises.py: ~45 menit
- Melihat visualizations.py: ~15 menit
- Tantangan challenge.py: ~30-60 menit

**Total: ~3 jam**

---

## Topik Berikutnya / Next Topic

Setelah menyelesaikan ini, lanjut ke:
**[1.2 Variables & Expressions](../02_Variables_Expressions/README.md)**

---

*Topic 1.1: Number Systems — MathCode Learning Project*
