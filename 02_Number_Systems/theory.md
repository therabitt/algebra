# 1.1 Sistem Bilangan (Number Systems) — Teori Lengkap

## Apa itu Sistem Bilangan?

Sistem bilangan adalah cara kita mengklasifikasikan, mengorganisir, dan bekerja dengan
bilangan-bilangan. Setiap "sistem" adalah himpunan bilangan dengan sifat-sifat tertentu.

---

## Hierarki Sistem Bilangan

```
C (Bilangan Kompleks)
└── R (Bilangan Real)
    ├── Q (Bilangan Rasional)
    │   ├── Z (Bilangan Bulat)
    │   │   ├── W (Bilangan Cacah)
    │   │   │   └── N (Bilangan Asli / Natural)
    │   │   └── {..., -3, -2, -1}
    │   └── {p/q | p,q ∈ Z, q ≠ 0}
    └── Irasional (√2, π, e, ...)
```

> Notasi: N ⊂ W ⊂ Z ⊂ Q ⊂ R ⊂ C

---

## 1. Bilangan Asli (Natural Numbers) — N

**Definisi:** Bilangan yang digunakan untuk menghitung: {1, 2, 3, 4, 5, ...}
(Beberapa definisi menyertakan 0, tergantung konvensi — di sini N = {1,2,3,...})

**Sifat-sifat:**
- Tertutup terhadap penjumlahan: a,b ∈ N → a+b ∈ N
- Tertutup terhadap perkalian: a,b ∈ N → a×b ∈ N
- TIDAK tertutup terhadap pengurangan: 3-5 = -2 ∉ N
- TIDAK tertutup terhadap pembagian: 3/4 ∉ N
- **Well-Ordering Principle**: setiap himpunan non-kosong bilangan asli punya elemen terkecil

**Prinsip Induksi Matematika:** Jika P(1) benar, dan P(k)→P(k+1), maka P(n) benar untuk semua n ∈ N.
> metode pembuktian rumus atau pernyataan matematika yang berlaku untuk semua bilangan asli atau bilangan bulat tertentu.
> metode ini bekerja seperti efek domino. 

---

## 2. Bilangan Cacah (Whole Numbers) — W

**Definisi:** Bilangan asli ditambah nol: W = {0, 1, 2, 3, ...}

**Peran Nol:** Nol adalah elemen identitas penjumlahan: a + 0 = a untuk semua a.
Nol bukan positif, bukan negatif — netral.

---

## 3. Bilangan Bulat (Integers) — Z

**Definisi:** Z = {..., -3, -2, -1, 0, 1, 2, 3, ...}

"Z" dari kata Jerman "Zahlen" (bilangan).

**Sifat-sifat tambahan:**
- Tertutup terhadap pengurangan: a,b ∈ Z → a-b ∈ Z
- Setiap bilangan punya negatif (invers penjumlahan): a + (-a) = 0
- Urutan total: untuk a,b ∈ Z, tepat satu dari: a<b, a=b, a>b

---

## 4. Bilangan Rasional (Rational Numbers) — Q

**Definisi formal:** Q = { p/q | p ∈ Z, q ∈ Z, q ≠ 0 }

"Q" dari kata Latin "Quotiens" (hasil bagi).

**Representasi desimal:** Bilangan rasional selalu memiliki ekspansi desimal yang:
- Berakhir (terminasi): contoh 1/4 = 0.25
- Atau berulang: contoh 1/3 = 0.333... = 0.3̄

**Mengubah desimal berulang ke pecahan:**
Contoh: x = 0.142857142857...
  → 10x = 1.42857142857...
  → 1000000x = 142857.142857...
  → 999999x = 142857
  → x = 142857/999999 = 1/7

**Rumus cepat:**
jumlah digit yang berulang menentukan jumlah angka 9 di bagian penyebut (bawah):

> - 0.333...  → 3/9 = 1/3
> - 0.2525... → 25/99
> - 0.142857... → 142857/999999 = 1/7

---

## 5. Bilangan Irasional (Irrational Numbers)

**Definisi:** Bilangan real yang TIDAK bisa ditulis sebagai p/q (p,q ∈ Z, q≠0).
Ekspansi desimalnya **tidak berakhir** DAN **tidak berulang**.

**Contoh terkenal:**
- √2 ≈ 1.41421356237...
- π ≈ 3.14159265358...
- e ≈ 2.71828182845...
- φ (golden ratio) = (1+√5)/2 ≈ 1.61803398874...

> **Bukti bahwa √2 irasional (proof by contradiction):**
>
> > Asumsikan √2 = p/q dalam bentuk paling sederhana (gcd(p,q)=1).
> > Maka 2 = p²/q² → p² = 2q²
> > Berarti p² genap → p genap → tulis p = 2k
> > Maka (2k)² = 2q² → 4k² = 2q² → q² = 2k²
> > Berarti q² genap → q genap.
> > KONTRADIKSI: p dan q keduanya genap, padahal gcd(p,q)=1.
> > Kesimpulan: √2 tidak rasional. ∎

> **Fact!!**
> Pembuktian kontradiksi pada √2 (akar 2) adalah salah satu pembuktian paling dramatis dalam sejarah matematika kuno oleh Hippasus.
> Pembuktian yang sangat epik karena berhasil menghancurkan keyakinan dasar bangsa Yunani Kuno (kamu Pythagorean)
> yang percaya bahwa seluruh alam semesta bisa dijelaskan dengan bilangan bulat dan rasionya (pecahan).

---

## 6. Bilangan Real (Real Numbers) — R

**Definisi:** Gabungan bilangan rasional DAN irasional.
R = Q ∪ Irasional

**Sifat kelengkapan (Completeness):** Setiap himpunan bilangan real yang dibatasi dari
atas memiliki supremum (batas atas terkecil) di R. Ini yang membedakan R dari Q.

**Garis bilangan:** Setiap titik pada garis bilangan berkorespondensi dengan tepat satu
bilangan real, dan setiap bilangan real berkorespondensi dengan tepat satu titik.

**Sifat kerapatan (Density):** Antara dua bilangan real yang berbeda, selalu ada bilangan
real lain (bahkan tak hingga banyaknya).

**Prinsip Archimedes:** Untuk setiap x ∈ R, ada n ∈ N sehingga n > x.

---

## 7. Bilangan Kompleks (Complex Numbers) — C

**Definisi:** C = { a + bi | a, b ∈ R } di mana i = √(-1), i² = -1

- a disebut bagian real: Re(z) = a
- b disebut bagian imajiner: Im(z) = b
**Kondisi khusus:**
- Jika b=0: z => bilangan real biasa/ z = a + 0i => z = a (real)
- Jika a=0, b≠0: z => bilangan imajiner murni/ z = 0 + bi => z = bi (imajiner)

> ![Notes]
> *bisa disimpulkan!*
> bilangan real adalah bilangan kompleks yang memiliki bagian imajiner (z = a + bi): 0 (z = a + 0i => z = a)

**Bidang kompleks (Complex Plane / Argand Diagram):**
- Sumbu horizontal: bagian real
- Sumbu vertikal: bagian imajiner
- Modulus/ nilai mutlak: |z| = |a + bi| = √(a² + b²) => jarak dari titik asal (0,0) ke titik koordinat bilangan kompleks(z) 
> contoh => z = 3 + 4i
> |z| = √(3²+4²) = √(9+16) = √25 
> |z| = 5
> **kesimpulan**: jarak lurus dari posisi awal (0,0) ke titik z adalah tepat *5* satuan langkah.
- Argumen: θ = arctan(b/a)


**Bentuk polar:** z = r(cos θ + i sin θ) = re^(iθ)

**Formula Euler:** e^(iπ) + 1 = 0 (dianggap persamaan paling indah dalam matematika)

```

    │ (Im)
    │           ● z = 3 + 4i
4   │          ╱│
    │        ╱  │
    │       ╱   │
    │      ╱    │
    │     ╱     │ b
    │   ╱       │
    │  ╱        │
    │ ╱θ        │
0  ─┼───────────┴──────────────── (Re)
    0     a     3

```

---

## 8. Notasi Interval

| Notasi | Makna | Contoh |
|--------|-------|--------|
| (a, b) | a < x < b (terbuka) | (1, 5): 1 < x < 5 |
| [a, b] | a ≤ x ≤ b (tertutup) | [1, 5]: 1 ≤ x ≤ 5 |
| [a, b) | a ≤ x < b (setengah terbuka) | [0, 1): 0 ≤ x < 1 |
| (a, b] | a < x ≤ b | (0, 1]: 0 < x ≤ 1 |
| (a, ∞) | x > a | (3, ∞): x > 3 |
| (-∞, b] | x ≤ b | (-∞, 0]: x ≤ 0 |
| (-∞, ∞) | semua bilangan real | R |

---

## 9. Nilai Mutlak (Absolute Value) — Definisi Awal

|x| = { x,  jika x ≥ 0
      { -x, jika x < 0

Interpretasi geometri: jarak dari x ke titik 0 pada garis bilangan.
Topik ini dibahas lengkap di 1.15.

---

## 10. Fungsi Lantai dan Plafon (Floor & Ceiling)

**Floor:** ⌊x⌋ = bilangan bulat terbesar yang ≤ x
Contoh: ⌊3.7⌋ = 3, ⌊-2.3⌋ = -3

**Ceiling:** ⌈x⌉ = bilangan bulat terkecil yang ≥ x
Contoh: ⌈3.2⌉ = 4, ⌈-2.7⌉ = -2

---

## 11. Sifat-Sifat Operasi (Preview)

Untuk bilangan real a, b, c:
1. Komutatif: a+b = b+a, a×b = b×a
2. Asosiatif: (a+b)+c = a+(b+c), (a×b)×c = a×(b×c)
3. Distributif: a×(b+c) = a×b + a×c
4. Elemen identitas: a+0=a (penjumlahan), a×1=a (perkalian)
5. Invers: a+(-a)=0 (penjumlahan), a×(1/a)=1 jika a≠0 (perkalian)

---

*Topik berikutnya: 1.2 — Operasi Dasar & Sifat-Sifatnya*
