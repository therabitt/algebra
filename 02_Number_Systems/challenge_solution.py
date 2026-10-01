"""
Challenge: Number Systems — Tingkat Lanjut
Phase 1 — Topic 1.1

Tantangan ini membutuhkan pemahaman lebih dalam dan implementasi
dari nol (tanpa banyak library bantuan).
"""

import math

print("=" * 60)
print("CHALLENGE 1.1 — NUMBER SYSTEMS")
print("=" * 60)

# ─────────────────────────────────────────────────────────────
# KONSEP: Pecahan = pasangan bilangan bulat (pembilang, penyebut) yang disederhanakan oleh GCD.
# Challenge 1: Implementasi Kelas Fraction dari Nol
# ─────────────────────────────────────────────────────────────
print("\n[Challenge 1] Implementasi kelas Fraction (Pecahan) dari nol")

def gcd(a, b):
    """Euclidean algorithm untuk GCD."""
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

class MyFraction:
    """Representasi bilangan rasional p/q dalam bentuk paling sederhana."""
    
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator tidak boleh nol!")
        # Normalisasi tanda: tanda selalu di pembilang
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        # Sederhanakan dengan GCD
        common = gcd(abs(numerator), denominator)
        self.p = numerator // common
        self.q = denominator // common
    
    def __repr__(self):
        if self.q == 1:
            return str(self.p)
        return f"{self.p}/{self.q}"
    
    def __add__(self, other):
        if isinstance(other, int):
            other = MyFraction(other)
        return MyFraction(self.p * other.q + other.p * self.q, self.q * other.q)
    
    def __sub__(self, other):
        if isinstance(other, int):
            other = MyFraction(other)
        return MyFraction(self.p * other.q - other.p * self.q, self.q * other.q)
    
    def __mul__(self, other):
        if isinstance(other, int):
            other = MyFraction(other)
        return MyFraction(self.p * other.p, self.q * other.q)
    
    def __truediv__(self, other):
        if isinstance(other, int):
            other = MyFraction(other)
        return MyFraction(self.p * other.q, self.q * other.p)
    
    def __eq__(self, other):
        if isinstance(other, int):
            other = MyFraction(other)
        return self.p == other.p and self.q == other.q
    
    def __float__(self):
        return self.p / self.q

# Test MyFraction
a = MyFraction(1, 3)
b = MyFraction(1, 6)
print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")
print(f"a × b = {a * b}")
print(f"a / b = {a / b}")
print(f"float(a) = {float(a):.6f}")

# ─────────────────────────────────────────────────────────────
# KONSEP: Setiap bilangan real dapat ditulis sebagai pecahan berkelanjutan x=a0+1/(a1+1/(a2+...))
# Challenge 2: Continued Fraction Expansion
# ─────────────────────────────────────────────────────────────
print("\n" + "-" * 40)
print("[Challenge 2] Continued Fraction (Pecahan Berkelanjutan)")
print("Setiap bilangan real dapat ditulis sebagai:")
print("x = a0 + 1/(a1 + 1/(a2 + 1/(a3 + ...)))")

def continued_fraction(x, max_terms=10):
    """Hitung representasi pecahan berkelanjutan dari x."""
    terms = []
    for _ in range(max_terms):
        a = int(x)
        terms.append(a)
        frac = x - a
        if abs(frac) < 1e-10:
            break
        x = 1.0 / frac
    return terms

def cf_to_fraction(terms):
    """Konversi kembali continued fraction ke pecahan."""
    if not terms:
        return MyFraction(0)
    result = MyFraction(terms[-1])
    for t in reversed(terms[:-1]):
        result = MyFraction(1) / result
        result = MyFraction(t) + result
    return result

for num, name in [(math.sqrt(2), "√2"), (math.pi, "π"), (1.618033988749895, "φ")]:
    cf = continued_fraction(num, 8)
    approx = cf_to_fraction(cf)
    print(f"\n{name} ≈ continued fraction: {cf}")
    print(f"  Approx sebagai pecahan: {approx} ≈ {float(approx):.8f}")
    print(f"  Nilai asli            : {num:.8f}")

# ─────────────────────────────────────────────────────────────
# KONSEP: Antara dua bilangan real manapun, selalu ada bilangan rasional (Q rapat di R).
# Challenge 3: Kerapatan Bilangan Rasional
# ─────────────────────────────────────────────────────────────
print("\n" + "-" * 40)
print("[Challenge 3] Kerapatan Q di R")
print("Antara dua bilangan real apapun, selalu ada bilangan rasional.")

def find_rational_between(a, b, n_to_find=5):
    """
    Temukan n bilangan rasional antara a dan b.
    Gunakan median Stern-Brocot atau pendekatan sederhana.
    """
    rationals = []
    # Metode sederhana: cari k/q sehingga a < k/q < b
    for q in range(1, 1000):
        k_min = int(a * q) + 1
        k_max = int(b * q)
        for k in range(k_min, k_max + 1):
            if a < k/q < b:
                import fractions as fr
                frac = fr.Fraction(k, q)
                if frac not in rationals:
                    rationals.append(frac)
                    if len(rationals) >= n_to_find:
                        return rationals
    return rationals

a, b = math.pi, math.e  # Dua irasional!
print(f"\nAntara π ≈ {a:.6f} dan e ≈ {b:.6f}:")
print(f"(perhatikan: π > e, jadi kita cari antara e dan π)")
a, b = min(a, b), max(a, b)
rationals = find_rational_between(a, b, 5)
for r in rationals:
    print(f"  {r} = {float(r):.8f}  ✓ ({float(a):.4f} < {float(r):.4f} < {float(b):.4f})")

# ─────────────────────────────────────────────────────────────
# KONSEP: Bilangan kompleks z=a+bi, operasi perkalian (a+bi)(c+di)=(ac-bd)+(ad+bc)i.
# Challenge 4: Implementasi Bilangan Kompleks dari Nol
# ─────────────────────────────────────────────────────────────
print("\n" + "-" * 40)
print("[Challenge 4] Custom Complex Number Class")

class MyComplex:
    """Bilangan kompleks a + bi dari nol."""
    
    def __init__(self, real=0, imag=0):
        self.real = float(real)
        self.imag = float(imag)
    
    def __repr__(self):
        if self.imag >= 0:
            return f"({self.real} + {self.imag}i)"
        return f"({self.real} - {abs(self.imag)}i)"
    
    def __add__(self, other):
        return MyComplex(self.real + other.real, self.imag + other.imag)
    
    def __mul__(self, other):
        # (a+bi)(c+di) = (ac-bd) + (ad+bc)i
        return MyComplex(
            self.real*other.real - self.imag*other.imag,
            self.real*other.imag + self.imag*other.real
        )
    
    def conjugate(self):
        return MyComplex(self.real, -self.imag)
    
    def modulus(self):
        return math.sqrt(self.real**2 + self.imag**2)
    
    def argument(self):
        return math.atan2(self.imag, self.real)
    
    def __truediv__(self, other):
        # z1/z2 = z1 * conj(z2) / |z2|^2
        conj = other.conjugate()
        num = self * conj
        denom = other.modulus()**2
        return MyComplex(num.real/denom, num.imag/denom)

z1 = MyComplex(3, 4)
z2 = MyComplex(1, -2)
print(f"z1 = {z1}")
print(f"z2 = {z2}")
print(f"z1 + z2 = {z1 + z2}")
print(f"z1 × z2 = {z1 * z2}")
print(f"z1 / z2 = {z1 / z2}")
print(f"|z1|    = {z1.modulus()}")
print(f"arg(z1) = {math.degrees(z1.argument()):.2f}°")

print("\n[Selesai] Semua challenge diselesaikan! Luar biasa!")
