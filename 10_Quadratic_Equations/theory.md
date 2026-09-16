# 📖 Teori Persamaan Kuadrat (Quadratic Equations Theory)

## 1. Bentuk Standar / Standard Form

Persamaan kuadrat dalam satu variabel x memiliki bentuk umum:

$$ax^2 + bx + c = 0, \quad a \neq 0$$

Di mana:
- **a** = koefisien kuadrat (leading coefficient)
- **b** = koefisien linear
- **c** = konstanta (constant term)
- **x** = variabel/peubah

**Contoh:**
- 2x² - 5x + 3 = 0  → a=2, b=-5, c=3
- x² - 9 = 0        → a=1, b=0, c=-9 (tidak ada suku linear)
- x² + 4x = 0       → a=1, b=4, c=0 (tidak ada konstanta)

---

## 2. Hubungan dengan Parabola / Parabola Connection

Fungsi kuadrat f(x) = ax² + bx + c mendefinisikan sebuah **parabola** pada bidang koordinat.

- Jika **a > 0**: parabola terbuka ke atas (minimum)
- Jika **a < 0**: parabola terbuka ke bawah (maksimum)
- Akar persamaan kuadrat = titik potong parabola dengan sumbu-x (x-intercepts)
- **Poros simetri (Axis of Symmetry):** x = -b/(2a)
- **Vertex (titik puncak):** V = (-b/2a, f(-b/2a))

---

## 3. Metode Penyelesaian / Methods of Solving

### 3a. Faktorisasi / Factoring

Metode paling cepat jika tersedia faktorisasi integer.

**Prinsip Nol:** Jika A · B = 0, maka A = 0 atau B = 0.

**Langkah:**
1. Tulis dalam bentuk standar: ax² + bx + c = 0
2. Faktorkan ruas kiri
3. Set setiap faktor = 0
4. Selesaikan

**Contoh:** x² - 5x + 6 = 0
- Cari dua bilangan yang produknya 6 dan jumlahnya -5 → (-2)(-3)
- (x - 2)(x - 3) = 0
- x = 2 atau x = 3

**Bentuk umum faktorisasi:** a(x - r₁)(x - r₂) = 0

---

### 3b. Melengkapkan Kuadrat / Completing the Square

**Derivasi lengkap:**

Mulai dari: ax² + bx + c = 0

**Langkah 1:** Bagi semua suku dengan a:
$$x^2 + \frac{b}{a}x + \frac{c}{a} = 0$$

**Langkah 2:** Pindahkan konstanta ke kanan:
$$x^2 + \frac{b}{a}x = -\frac{c}{a}$$

**Langkah 3:** Tambahkan (b/2a)² ke kedua ruas:
$$x^2 + \frac{b}{a}x + \left(\frac{b}{2a}\right)^2 = -\frac{c}{a} + \left(\frac{b}{2a}\right)^2$$

**Langkah 4:** Ruas kiri adalah kuadrat sempurna:
$$\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2}$$

**Langkah 5:** Ambil akar kuadrat kedua ruas:
$$x + \frac{b}{2a} = \pm\frac{\sqrt{b^2 - 4ac}}{2a}$$

**Langkah 6:** Selesaikan x:
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

Ini adalah **rumus kuadrat**!

---

### 3c. Rumus Kuadrat / Quadratic Formula

Derivasi dari melengkapkan kuadrat menghasilkan:

$$\boxed{x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}}$$

Rumus ini **selalu berlaku** untuk semua persamaan kuadrat (asalkan a ≠ 0).

---

### 3d. Metode Grafik / Graphical Method

1. Gambar grafik y = ax² + bx + c
2. Titik potong dengan sumbu-x adalah akar persamaan
3. Jika parabola memotong x-axis di 2 titik → 2 akar real berbeda
4. Jika parabola menyentuh x-axis di 1 titik → 1 akar real kembar
5. Jika parabola tidak memotong x-axis → tidak ada akar real

---

## 4. Diskriminan / Discriminant

$$\boxed{D = b^2 - 4ac}$$

| Nilai D | Jenis Akar | Geometri |
|---------|-----------|---------|
| D > 0 | Dua akar real berbeda: x₁ ≠ x₂ | Parabola memotong x-axis di 2 titik |
| D = 0 | Satu akar real kembar: x₁ = x₂ = -b/2a | Parabola menyentuh x-axis di vertex |
| D < 0 | Dua akar kompleks konjugat | Parabola tidak memotong x-axis |

**Kasus D < 0 — Akar Kompleks:**
$$x = \frac{-b \pm i\sqrt{4ac - b^2}}{2a} = \frac{-b}{2a} \pm \frac{\sqrt{|D|}}{2a}i$$

---

## 5. Rumus Vieta / Vieta's Formulas

Jika x₁ dan x₂ adalah akar-akar ax² + bx + c = 0, maka:

$$\boxed{x_1 + x_2 = -\frac{b}{a}} \quad \text{(Jumlah akar / Sum of roots)}$$

$$\boxed{x_1 \cdot x_2 = \frac{c}{a}} \quad \text{(Hasil kali akar / Product of roots)}$$

**Bukti:**
Jika akar-akarnya x₁ dan x₂, maka persamaan dapat ditulis:
a(x - x₁)(x - x₂) = 0
= a[x² - (x₁+x₂)x + x₁x₂] = 0
= ax² - a(x₁+x₂)x + a(x₁x₂) = 0

Bandingkan dengan ax² + bx + c = 0:
- b = -a(x₁+x₂)  →  x₁+x₂ = -b/a  ✓
- c = a(x₁x₂)    →  x₁·x₂ = c/a   ✓

---

## 6. Sifat Akar / Nature of Roots

Dari diskriminan D = b² - 4ac:

| Kondisi | Jenis Akar |
|---------|-----------|
| D > 0, D adalah kuadrat sempurna | Dua akar rasional berbeda |
| D > 0, D bukan kuadrat sempurna | Dua akar irasional berbeda (conjugate surds) |
| D = 0 | Satu akar rasional kembar |
| D < 0 | Dua akar kompleks konjugat (non-real) |

**Penting:** Koefisien a, b, c harus rasional untuk klasifikasi di atas.

---

## 7. Membentuk Persamaan dari Akar / Forming Equation from Roots

Jika diketahui akar-akarnya x₁ dan x₂:

$$x^2 - (x_1 + x_2)x + x_1 \cdot x_2 = 0$$

Atau: $x^2 - Sx + P = 0$ di mana S = jumlah akar, P = hasil kali akar.

**Contoh:** Akar-akar 3 dan -5:
- S = 3 + (-5) = -2
- P = 3 × (-5) = -15
- Persamaan: x² - (-2)x + (-15) = 0 → **x² + 2x - 15 = 0**

---

## 8. Bentuk Vertex / Vertex Form

$$f(x) = a(x - h)^2 + k$$

Di mana:
- **(h, k)** adalah vertex (titik puncak) parabola
- **h = -b/(2a)** (koordinat x dari vertex)
- **k = f(h) = c - b²/(4a)** (koordinat y dari vertex)

**Konversi dari bentuk standar:**
Gunakan completing the square:
$$ax^2 + bx + c = a\left(x + \frac{b}{2a}\right)^2 + c - \frac{b^2}{4a}$$

**Interpretasi:**
- Parabola y = x² digeser h ke kanan dan k ke atas
- Kemudian diregangkan secara vertikal dengan faktor |a|

---

## 9. Bentuk Intercept / Intercept Form

Jika persamaan memiliki akar x₁ dan x₂:

$$f(x) = a(x - x_1)(x - x_2)$$

Ini langsung menunjukkan x-intercepts (akar) di x₁ dan x₂.

---

## 10. Nilai Maksimum dan Minimum / Maximum and Minimum

Karena f(x) = ax² + bx + c adalah parabola:

- Jika **a > 0**: nilai **minimum** = k = c - b²/(4a), dicapai di x = -b/(2a)
- Jika **a < 0**: nilai **maksimum** = k = c - b²/(4a), dicapai di x = -b/(2a)

**Range (daerah hasil):**
- a > 0: f(x) ≥ k, yaitu **[k, ∞)**
- a < 0: f(x) ≤ k, yaitu **(-∞, k]**

---

## 11. Pertidaksamaan Kuadrat / Quadratic Inequalities

Untuk menyelesaikan ax² + bx + c > 0 (atau <, ≥, ≤):

**Langkah:**
1. Ubah ke bentuk standar dengan 0 di kanan
2. Temukan akar-akar x₁ dan x₂ (x₁ < x₂)
3. Buat garis bilangan dengan x₁ dan x₂ sebagai titik kritis
4. Uji tanda di setiap interval

**Kasus a > 0:**
- ax² + bx + c > 0: x < x₁ atau x > x₂ (luar interval)
- ax² + bx + c < 0: x₁ < x < x₂ (dalam interval)

**Kasus a < 0:** Kebalikannya!

**Jika D < 0:**
- a > 0: ax² + bx + c > 0 untuk semua x (definit positif)
- a < 0: ax² + bx + c < 0 untuk semua x (definit negatif)

---

## 12. Soal Cerita dengan Kuadrat / Word Problems

### Gerak Proyektil / Projectile Motion:
$$h(t) = -\frac{1}{2}gt^2 + v_0 t + h_0$$
- h(t): ketinggian pada waktu t
- g: percepatan gravitasi ≈ 9.8 m/s² (atau 10 m/s²)
- v₀: kecepatan awal
- h₀: ketinggian awal

### Luas Persegi Panjang:
Panjang = (lebar + k), Luas = L → x(x+k) = L → x² + kx - L = 0

### Keuntungan/Profit:
P(x) = -ax² + bx - c (biasanya parabola terbuka ke bawah)

---

## 13. Akar Irasional / Irrational Roots

Jika D > 0 tetapi bukan kuadrat sempurna, akarnya berbentuk:

$$x = \frac{-b \pm \sqrt{D}}{2a}$$

di mana √D adalah irasional. Akar-akar ini selalu berpasangan **conjugate surds**:
jika (p + √q) adalah akar, maka (p - √q) juga akar.

**Contoh:** x² - 2x - 1 = 0
- D = 4 + 4 = 8 (bukan kuadrat sempurna)
- x = (2 ± √8)/2 = (2 ± 2√2)/2 = 1 ± √2

---

## 14. Akar Kompleks / Complex Roots

Jika D < 0, akarnya berbentuk bilangan kompleks konjugat:

$$x = \frac{-b}{2a} \pm \frac{\sqrt{|D|}}{2a}i = \alpha \pm \beta i$$

di mana α = -b/(2a) adalah bagian real, β = √|D|/(2a) adalah bagian imajiner.

**Sifat:** Untuk koefisien real, akar kompleks **selalu berpasangan konjugat**.

**Verifikasi Vieta:**
- Jumlah: (α + βi) + (α - βi) = 2α = -b/a ✓
- Produk: (α + βi)(α - βi) = α² + β² = c/a ✓
