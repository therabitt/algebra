"""
Challenge: Number Systems — Tingkat Lanjut
Phase 1 — Topic 1.1

Tantangan ini membutuhkan pemahaman lebih dalam dan implementasi dari nol.
Implementasikan semua class dan fungsi di bawah ini!
"""
import math

print("=" * 60)
print("CHALLENGE 1.1 — NUMBER SYSTEMS")
print("=" * 60)

# ─────────────────────────────────────────────────────────────
# [Ch1] IMPLEMENTASI KELAS FRACTION (PECAHAN) DARI NOL
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   Bilangan rasional p/q disimpan dalam bentuk paling sederhana.
#   GCD digunakan untuk menyederhanakan: 6/9 → 2/3
#   Operasi: tambah (+), kurang (-), kali (*), bagi (/)
#
# LANGKAH untuk gcd(a, b):
#   1. Algoritma Euclidean: while b: a,b = b, a%b
#   2. Return a
#
# LANGKAH untuk MyFraction.__init__:
#   1. Jika denominator < 0: balik tanda keduanya
#   2. common = gcd(|numerator|, denominator)
#   3. self.p = numerator // common
#   4. self.q = denominator // common
#
# LANGKAH untuk MyFraction.__add__:
#   1. (p1/q1) + (p2/q2) = (p1*q2 + p2*q1) / (q1*q2)
#   2. return MyFraction(p1*q2 + p2*q1, q1*q2)  ← otomatis disederhanakan
#
# IMPLEMENTASIKAN:
print("\n[Ch1] Implementasi kelas Fraction dari nol")

def gcd(a, b):
    """Euclidean algorithm untuk GCD."""
    # TODO: implementasikan Euclidean Algorithm
    pass

class MyFraction:
    """Bilangan rasional p/q dalam bentuk paling sederhana."""

    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator tidak boleh nol!")
        # TODO: normalisasi tanda, sederhanakan dengan gcd
        pass

    def __repr__(self):
        if self.q == 1:
            return str(self.p)
        return f"{self.p}/{self.q}"

    def __add__(self, other):
        if isinstance(other, int): other = MyFraction(other)
        # TODO: implementasikan penjumlahan pecahan: (p1*q2 + p2*q1) / (q1*q2)
        pass

    def __sub__(self, other):
        if isinstance(other, int): other = MyFraction(other)
        # TODO: implementasikan pengurangan pecahan
        pass

    def __mul__(self, other):
        if isinstance(other, int): other = MyFraction(other)
        # TODO: implementasikan perkalian pecahan: (p1*p2) / (q1*q2)
        pass

    def __truediv__(self, other):
        if isinstance(other, int): other = MyFraction(other)
        # TODO: implementasikan pembagian: kalikan dengan invers (p2/q2 → q2/p2)
        pass

    def __eq__(self, other):
        if isinstance(other, int): other = MyFraction(other)
        # TODO: cek kesamaan: p1==p2 dan q1==q2
        pass

    def __float__(self):
        return self.p / self.q

# TODO: setelah mengimplementasikan, uncomment kode uji di bawah:
# a = MyFraction(1, 3)
# b = MyFraction(1, 6)
# print(f"a = {a}, b = {b}")
# print(f"a + b = {a + b}")    # harus: 1/2
# print(f"a × b = {a * b}")    # harus: 1/18
# print(f"a / b = {a / b}")    # harus: 2
# Jawaban: a=1/3, b=1/6, a+b=1/2, a*b=1/18, a/b=2


# ─────────────────────────────────────────────────────────────
# [Ch2] CONTINUED FRACTION (PECAHAN BERKELANJUTAN)
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   x = a0 + 1/(a1 + 1/(a2 + 1/(a3 + ...)))
#   Setiap bilangan real bisa ditulis sebagai CF.
#   Konvergen CF adalah aproksimasi rasional terbaik.
#
# LANGKAH untuk continued_fraction(x, max_terms):
#   1. Loop max_terms kali:
#      a. a = int(x)  ← ambil bagian bulat
#      b. terms.append(a)
#      c. frac = x - a  ← ambil sisa pecahan
#      d. if abs(frac) < 1e-10: break  ← sudah habis
#      e. x = 1.0 / frac  ← balik pecahan untuk iterasi berikutnya
#
# LANGKAH untuk cf_to_fraction(terms):
#   1. Mulai dari belakang: result = MyFraction(terms[-1])
#   2. Loop mundur: result = 1/result + terms[i]
#
# IMPLEMENTASIKAN:
print("\n[Ch2] Continued Fraction Expansion")

def continued_fraction(x, max_terms=10):
    """Hitung representasi CF dari x. Return list koefisien [a0, a1, a2, ...]"""
    terms = []
    # TODO: implementasikan algoritma CF di atas
    return terms

def cf_to_fraction(terms):
    """Konversi list CF kembali ke MyFraction."""
    if not terms:
        return MyFraction(0)
    # TODO: rekonstruksi pecahan dari belakang
    pass

# TODO: uncomment untuk uji
# for num, name in [(math.sqrt(2), "√2"), (math.pi, "π"), (1.618033988749895, "φ (Golden Ratio)")]:
#     cf = continued_fraction(num, 8)
#     approx = cf_to_fraction(cf)
#     print(f"  {name}: CF={cf}")
#     print(f"    Aproksimasi: {approx} ≈ {float(approx):.8f} (asli: {num:.8f})")
# Jawaban √2: CF=[1,2,2,2,2,...], aprox≈1.41421356


# ─────────────────────────────────────────────────────────────
# [Ch3] KERAPATAN BILANGAN RASIONAL
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   Di antara dua bilangan real a dan b (a < b) manapun,
#   selalu ada bilangan rasional (Q rapat/dense di R).
#
# LANGKAH untuk find_rational_between(a, b, n):
#   1. Loop q dari 1 sampai 1000:
#      a. k_min = int(a*q) + 1
#      b. k_max = int(b*q)
#      c. untuk setiap k di range(k_min, k_max+1):
#         - jika a < k/q < b: tambahkan Fraction(k,q) ke list
#         - jika sudah n: return
#
# IMPLEMENTASIKAN:
print("\n[Ch3] Kerapatan Q di R")

def find_rational_between(a, b, n_to_find=5):
    """Temukan n bilangan rasional antara a dan b."""
    rationals = []
    # TODO: implementasikan pencarian rasional antara a dan b
    return rationals

# TODO: uncomment untuk uji
# import fractions as fr
# a, b = min(math.pi, math.e), max(math.pi, math.e)
# print(f"  Antara e≈{a:.6f} dan π≈{b:.6f}:")
# for r in find_rational_between(a, b, 5):
#     print(f"    {r} = {float(r):.8f}")


# ─────────────────────────────────────────────────────────────
# [Ch4] BILANGAN KOMPLEKS DARI NOL
# ─────────────────────────────────────────────────────────────
# KONSEP:
#   Bilangan kompleks z = a + bi, operasi:
#   Penjumlahan: (a+bi)+(c+di) = (a+c)+(b+d)i
#   Perkalian:   (a+bi)(c+di) = (ac-bd) + (ad+bc)i
#   Pembagian:   z1/z2 = z1 × konj(z2) / |z2|²
#   Modulus:     |z| = √(a²+b²)
#   Argumen:     θ = atan2(b, a)
#
# LANGKAH untuk MyComplex.__mul__:
#   real = a*c - b*d
#   imag = a*d + b*c
#   return MyComplex(real, imag)
#
# LANGKAH untuk MyComplex.__truediv__:
#   conj = other.conjugate()
#   num  = self * conj
#   denom = other.modulus()**2
#   return MyComplex(num.real/denom, num.imag/denom)
#
# IMPLEMENTASIKAN:
print("\n[Ch4] Custom Complex Number Class")

class MyComplex:
    """Bilangan kompleks a + bi dari nol."""

    def __init__(self, real=0, imag=0):
        self.real = float(real)
        self.imag = float(imag)

    def __repr__(self):
        sign = "+" if self.imag >= 0 else "-"
        return f"({self.real} {sign} {abs(self.imag)}i)"

    def __add__(self, other):
        # TODO: (a+bi) + (c+di) = (a+c) + (b+d)i
        pass

    def __mul__(self, other):
        # TODO: (a+bi)(c+di) = (ac-bd) + (ad+bc)i
        pass

    def conjugate(self):
        # TODO: konjugat z = a - bi
        pass

    def modulus(self):
        # TODO: |z| = sqrt(a² + b²)
        pass

    def argument(self):
        # TODO: θ = atan2(imag, real) dalam radian
        pass

    def __truediv__(self, other):
        # TODO: z1/z2 = z1 × konj(z2) / |z2|²
        pass

# TODO: uncomment untuk uji
# z1 = MyComplex(3, 4)
# z2 = MyComplex(1, -2)
# print(f"  z1 = {z1}, z2 = {z2}")
# print(f"  z1 + z2 = {z1 + z2}")   # harus: (4 + 2i)
# print(f"  z1 × z2 = {z1 * z2}")   # harus: (11 + -2i)
# print(f"  z1 / z2 = {z1 / z2}")   # harus: (-1 + 2i)
# print(f"  |z1| = {z1.modulus()}")  # harus: 5.0
# print(f"  arg(z1) = {math.degrees(z1.argument()):.2f}°")  # harus: 53.13°

print("\n[Selesai] Implementasikan semua TODO, lalu uncomment kode uji!")
