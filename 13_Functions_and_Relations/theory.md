# 📖 Teori Fungsi dan Relasi (Functions and Relations Theory)

## 1. Definisi Relasi / Definition of a Relation

**Relasi** dari himpunan A ke himpunan B adalah himpunan sembarang pasangan terurut (a, b)
di mana a ∈ A dan b ∈ B.

$$R \subseteq A \times B = \{(a, b) \mid a \in A, b \in B\}$$

**Contoh:**
- R = {(1, 2), (1, 3), (2, 4)} adalah relasi dari {1, 2} ke {2, 3, 4}
- R = {(x, y) | x² + y² = 1} adalah relasi lingkaran satuan

---

## 2. Domain, Kodomain, dan Range / Domain, Codomain, and Range

Untuk relasi R ⊆ A × B:

- **Domain (Daerah Asal):** Himpunan semua nilai pertama (nilai x)
  $$\text{dom}(R) = \{a \in A \mid \exists b \in B : (a, b) \in R\}$$

- **Kodomain:** Himpunan B (himpunan yang menjadi target/tujuan)

- **Range / Daerah Hasil:** Himpunan semua nilai kedua yang benar-benar dicapai
  $$\text{range}(R) = \{b \in B \mid \exists a \in A : (a, b) \in R\}$$

**Catatan penting:** Range ⊆ Kodomain (range adalah subset dari kodomain)

---

## 3. Definisi Fungsi / Definition of a Function

**Fungsi** f dari A ke B (ditulis f: A → B) adalah relasi khusus di mana setiap elemen
domain dipetakan ke **tepat satu** elemen kodomain.

$$f : A \to B \iff \forall a \in A, \exists! b \in B : f(a) = b$$

**Syarat fungsi:**
1. Setiap elemen domain harus memiliki pasangan (total)
2. Setiap elemen domain memiliki **tepat satu** pasangan (well-defined)

**Uji Garis Vertikal (Vertical Line Test):**
Grafik relasi adalah fungsi ⟺ setiap garis vertikal x = k memotong grafik di paling banyak satu titik.

---

## 4. Notasi Fungsi / Function Notation

$$f(x) = \text{ekspresi dalam } x$$

- f: nama fungsi
- x: variabel bebas (argumen/input)
- f(x): nilai fungsi pada x (output)
- "f dari x" atau "f di x"

**Notasi alternatif:** y = f(x)

**Contoh evaluasi:**
- f(x) = x² + 2x - 1
- f(3) = (3)² + 2(3) - 1 = 9 + 6 - 1 = 14
- f(-1) = (-1)² + 2(-1) - 1 = 1 - 2 - 1 = -2
- f(a+1) = (a+1)² + 2(a+1) - 1 = a² + 4a + 2

---

## 5. Mengevaluasi Fungsi / Evaluating Functions

**Substitusi langsung:** Ganti variabel dengan nilai yang diberikan.

**Evaluasi pada ekspresi:**
- f(x+h): ganti x dengan (x+h) — penting untuk turunan!
- f(2x): ganti x dengan 2x
- f(x²): ganti x dengan x²

**Perbedaan Bagi (Difference Quotient) — preview kalkulus:**
$$\frac{f(x+h) - f(x)}{h}$$

---

## 6. Jenis Fungsi Berdasarkan Sifat / Types of Functions

### 6a. Fungsi Injektif (One-to-One)

$$f(x_1) = f(x_2) \implies x_1 = x_2$$

Equivalently: $x_1 \neq x_2 \implies f(x_1) \neq f(x_2)$

Tidak ada dua input berbeda yang menghasilkan output yang sama.

**Uji Garis Horizontal (Horizontal Line Test):**
f injektif ⟺ setiap garis horizontal y = k memotong grafik di paling banyak satu titik.

**Contoh:** f(x) = 2x + 1 (injektif), f(x) = x² (BUKAN injektif karena f(2) = f(-2) = 4)

---

### 6b. Fungsi Surjektif (Onto)

$$\forall b \in B, \exists a \in A : f(a) = b$$

Range = Kodomain. Setiap elemen kodomain punya preimage.

**Contoh:** f: ℝ → ℝ, f(x) = x³ (surjektif)
f: ℝ → ℝ, f(x) = x² (BUKAN surjektif ke ℝ, karena f(x) ≥ 0)
f: ℝ → [0,∞), f(x) = x² (surjektif ke [0,∞))

---

### 6c. Fungsi Bijektif / Bijective Function

Bijektif = Injektif + Surjektif (one-to-one dan onto).

Fungsi bijektif memiliki **invers yang terdefinisi dengan baik**.

---

## 7. Komposisi Fungsi / Composition of Functions

$$(f \circ g)(x) = f(g(x))$$

Dibaca: "f komposisi g dari x" atau "f setelah g"

**Proses:** Pertama aplikasikan g, lalu aplikasikan f ke hasilnya.

**Domain komposisi:**
$$\text{dom}(f \circ g) = \{x \in \text{dom}(g) \mid g(x) \in \text{dom}(f)\}$$

**Sifat:**
- Komposisi **tidak komutatif**: f∘g ≠ g∘f (pada umumnya)
- Komposisi **asosiatif**: (f∘g)∘h = f∘(g∘h)
- Identitas: f∘I = I∘f = f (di mana I(x) = x)

**Contoh:**
- f(x) = x², g(x) = x + 1
- (f∘g)(x) = f(g(x)) = f(x+1) = (x+1)²
- (g∘f)(x) = g(f(x)) = g(x²) = x² + 1

---

## 8. Fungsi Invers / Inverse Functions

Jika f bijektif, inversnya f⁻¹ didefinisikan oleh:

$$f^{-1}(y) = x \iff f(x) = y$$

**Properti fundamental:**
$$(f \circ f^{-1})(x) = x \quad \text{dan} \quad (f^{-1} \circ f)(x) = x$$

**Mencari invers secara aljabar:**
1. Tulis y = f(x)
2. Tukar x dan y: x = f(y)
3. Selesaikan untuk y → ini adalah f⁻¹(x)
4. Verifikasi: f(f⁻¹(x)) = x

**Grafik:** Grafik f⁻¹ adalah refleksi grafik f terhadap garis y = x.

**Domain dan Range:**
- dom(f⁻¹) = range(f)
- range(f⁻¹) = dom(f)

---

## 9. Mencari Invers Secara Aljabar / Finding Inverse Algebraically

**Contoh 1:** f(x) = 3x + 2
1. y = 3x + 2
2. x = 3y + 2  (tukar x dan y)
3. x - 2 = 3y
4. y = (x-2)/3
5. f⁻¹(x) = (x-2)/3

**Verifikasi:** f(f⁻¹(x)) = 3·(x-2)/3 + 2 = (x-2) + 2 = x ✓

**Contoh 2:** f(x) = (x+1)/(x-2)
1. y = (x+1)/(x-2)
2. x = (y+1)/(y-2)
3. x(y-2) = y+1
4. xy - 2x = y + 1
5. xy - y = 2x + 1
6. y(x-1) = 2x + 1
7. f⁻¹(x) = (2x+1)/(x-1)

---

## 10. Fungsi Genap dan Ganjil / Even and Odd Functions

**Fungsi Genap (Even):**
$$f(-x) = f(x), \quad \forall x \in \text{dom}(f)$$

Grafik simetri terhadap sumbu-y.
Contoh: f(x) = x², f(x) = cos(x), f(x) = |x|

**Fungsi Ganjil (Odd):**
$$f(-x) = -f(x), \quad \forall x \in \text{dom}(f)$$

Grafik simetri terhadap titik asal (origin).
Contoh: f(x) = x³, f(x) = sin(x), f(x) = x

**Catatan:**
- Sebagian besar fungsi bukan genap maupun ganjil
- Hanya f(x) = 0 yang genap sekaligus ganjil
- Domain harus simetri terhadap 0 untuk fungsi genap/ganjil

---

## 11. Fungsi Monoton / Monotonic Functions

Pada interval I:

**Monoton naik (Increasing):** x₁ < x₂ ⟹ f(x₁) < f(x₂)
**Monoton turun (Decreasing):** x₁ < x₂ ⟹ f(x₁) > f(x₂)
**Konstan (Constant):** f(x₁) = f(x₂) untuk semua x₁, x₂ ∈ I

**Monoton ketat:** < atau > (strict)
**Monoton lemah:** ≤ atau ≥ (weak/non-strict)

---

## 12. Fungsi Piecewise / Piecewise Functions

Fungsi yang didefinisikan berbeda-beda pada interval berbeda:

$$f(x) = \begin{cases} g_1(x) & \text{jika } x \in I_1 \\ g_2(x) & \text{jika } x \in I_2 \\ \vdots \end{cases}$$

**Contoh — Fungsi Nilai Mutlak:**
$$|x| = \begin{cases} x & \text{jika } x \geq 0 \\ -x & \text{jika } x < 0 \end{cases}$$

**Kontinuitas:** Periksa titik-titik "breakpoint" — apakah nilai kiri = nilai kanan?

---

## 13. Fungsi Nilai Mutlak / Absolute Value Function

$$f(x) = |x|$$

Properti:
- |x| ≥ 0 untuk semua x
- |x| = 0 ⟺ x = 0
- |x| = √(x²)
- |xy| = |x||y|
- |x + y| ≤ |x| + |y|  (Ketidaksamaan segitiga)

**Grafik:** Berbentuk V dengan vertex di (0, 0)

**Persamaan |f(x)| = c:**
- Jika c > 0: f(x) = c atau f(x) = -c
- Jika c = 0: f(x) = 0
- Jika c < 0: tidak ada solusi

---

## 14. Fungsi Tangga / Step Functions

**Fungsi Floor (Lantai):** ⌊x⌋ = bilangan bulat terbesar ≤ x
- ⌊3.7⌋ = 3, ⌊-2.3⌋ = -3

**Fungsi Ceiling (Langit-langit):** ⌈x⌉ = bilangan bulat terkecil ≥ x
- ⌈3.2⌉ = 4, ⌈-2.7⌉ = -2

**Fungsi Bagian Bulat (Round/Nint):** Pembulatan ke bilangan bulat terdekat

**Grafik:** Berbentuk tangga horizontal

---

## 15. Transformasi Fungsi / Function Transformations

Mulai dari fungsi dasar y = f(x):

| Transformasi | Persamaan | Efek pada Grafik |
|---|---|---|
| Geser kanan h | y = f(x - h), h > 0 | Geser kanan h unit |
| Geser kiri h | y = f(x + h), h > 0 | Geser kiri h unit |
| Geser atas k | y = f(x) + k, k > 0 | Geser atas k unit |
| Geser bawah k | y = f(x) - k, k > 0 | Geser bawah k unit |
| Regangan vertikal | y = af(x), a > 1 | Lebih curam (stretch) |
| Kompresi vertikal | y = af(x), 0 < a < 1 | Lebih landai (compress) |
| Refleksi x-axis | y = -f(x) | Balik atas-bawah |
| Refleksi y-axis | y = f(-x) | Balik kiri-kanan |
| Regangan horizontal | y = f(x/b), b > 1 | Lebih lebar |
| Kompresi horizontal | y = f(bx), b > 1 | Lebih sempit |

**Urutan transformasi:** Horizontal (dalam) dulu, lalu vertikal (luar).

---

## 16. Analisis Grafik / Graph Analysis

Untuk suatu fungsi f(x):

**x-intercepts (akar/zeros):** Nilai x di mana f(x) = 0
**y-intercept:** Nilai f(0) (jika 0 dalam domain)
**Ekstrem Lokal:**
- Maksimum lokal di x = c jika f(c) ≥ f(x) untuk x dekat c
- Minimum lokal di x = c jika f(c) ≤ f(x) untuk x dekat c
**Asimtot:** Garis yang didekati grafik tapi tidak pernah disentuh

---

## 17. Uji Garis Vertikal dan Horizontal / Vertical and Horizontal Line Tests

**Uji Garis Vertikal (Apakah ini Fungsi?):**
Suatu grafik merepresentasikan fungsi ⟺ tidak ada garis vertikal yang memotong grafik lebih dari satu kali.

**Uji Garis Horizontal (Apakah Fungsi Injektif?):**
Suatu fungsi bersifat injektif (one-to-one) ⟺ tidak ada garis horizontal yang memotong grafik lebih dari satu kali.

Hanya fungsi yang **lulus uji garis horizontal** yang memiliki invers yang merupakan fungsi.
