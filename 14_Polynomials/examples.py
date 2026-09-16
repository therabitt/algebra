"""
Module  : Polynomials (Polinomial)
Phase   : 1 - Algebra  |  Topic: 1.9
Jalankan: python3 examples.py
"""
print("=" * 60)
print("POLINOMIAL — CONTOH IMPLEMENTASI")
print("=" * 60)

# ─── 1. Representasi Polinomial ───────────────────────────────
print("\n[1] Representasi Polinomial")
print("  P(x) = a_n*x^n + ... + a_1*x + a_0")
print("  Kita simpan sebagai list koefisien (indeks = pangkat):")
print("  3x^2 - 5x + 2  =  [2, -5, 3]  (dari derajat 0 ke n)")

class Polynomial:
    """Polinomial: coeffs[i] = koefisien x^i"""
    def __init__(self, *coeffs):
        self.coeffs = list(coeffs)
        while len(self.coeffs) > 1 and self.coeffs[-1] == 0:
            self.coeffs.pop()

    def degree(self): return len(self.coeffs) - 1

    def __call__(self, x):
        """Evaluasi menggunakan Horner's method"""
        result = 0
        for c in reversed(self.coeffs):
            result = result * x + c
        return result

    def __add__(self, other):
        n = max(len(self.coeffs), len(other.coeffs))
        c1 = self.coeffs + [0]*(n-len(self.coeffs))
        c2 = other.coeffs + [0]*(n-len(other.coeffs))
        return Polynomial(*[a+b for a,b in zip(c1,c2)])

    def __sub__(self, other):
        n = max(len(self.coeffs), len(other.coeffs))
        c1 = self.coeffs + [0]*(n-len(self.coeffs))
        c2 = other.coeffs + [0]*(n-len(other.coeffs))
        return Polynomial(*[a-b for a,b in zip(c1,c2)])

    def __mul__(self, other):
        result = [0]*(len(self.coeffs)+len(other.coeffs)-1)
        for i,a in enumerate(self.coeffs):
            for j,b in enumerate(other.coeffs):
                result[i+j] += a*b
        return Polynomial(*result)

    def __repr__(self):
        terms = []
        for i,c in enumerate(reversed(self.coeffs)):
            d = self.degree()-i
            if c==0: continue
            sign = "+" if c>0 else "-"
            ac = abs(c)
            if d==0: terms.append(f"{sign} {ac}")
            elif d==1: terms.append(f"{sign} {ac}x")
            else: terms.append(f"{sign} {ac}x^{d}")
        result = " ".join(terms).lstrip("+ ").replace("+ -","- ")
        return result or "0"

p1 = Polynomial(2, -5, 3)     # 3x^2 - 5x + 2
p2 = Polynomial(-1, 2, 1)     # x^2 + 2x - 1
print(f"  P1 = {p1}  (derajat {p1.degree()})")
print(f"  P2 = {p2}  (derajat {p2.degree()})")
print(f"  P1+P2 = {p1+p2}")
print(f"  P1*P2 = {p1*p2}")

# ─── 2. Evaluasi dan Horner ───────────────────────────────────
print("\n[2] Evaluasi dengan Horner's Method")
print("  P(x) = 3x^2 - 5x + 2")
print("  Horner: ((3)*x - 5)*x + 2")
for x in [-2, 0, 1, 2, 3]:
    print(f"  P({x}) = {p1(x)}")

# ─── 3. Pembagian Polinomial ──────────────────────────────────
print("\n[3] Pembagian Polinomial Panjang")
def poly_divide(dividend, divisor):
    """
    Bagi polynomial dividend dengan divisor.
    Returns (quotient, remainder) sebagai lists koefisien.
    """
    num = list(reversed(dividend))   # tinggi ke rendah
    den = list(reversed(divisor))
    
    if len(num) < len(den):
        return [0], dividend
    
    quotient = []
    for i in range(len(num) - len(den) + 1):
        coef = num[i] / den[0]
        quotient.append(coef)
        for j in range(len(den)):
            num[i+j] -= coef * den[j]
    
    remainder = list(reversed(num[len(num)-len(den)+1:]))
    return list(reversed(quotient)), remainder

# (x^3 - 2x^2 - 5x + 6) / (x - 3)
dividend = [6, -5, -2, 1]   # 6 - 5x - 2x^2 + x^3 (dari rendah ke tinggi)
divisor  = [-3, 1]           # -3 + x = x - 3
q, r = poly_divide(list(reversed(dividend)), list(reversed(divisor)))
print(f"  (x^3 - 2x^2 - 5x + 6) / (x-3)")
print(f"  Quotient : {q}")
print(f"  Remainder: {r}")

# ─── 4. Teorema Sisa (Remainder Theorem) ─────────────────────
print("\n[4] Teorema Sisa: P(a) = sisa P(x)/(x-a)")
p = Polynomial(6, -5, -2, 1)   # x^3 - 2x^2 - 5x + 6
for a in [3, -2, 1, -1]:
    remainder = p(a)
    print(f"  P({a}) = {remainder}  (sisa P(x)/(x-{a}))")

# ─── 5. Teorema Faktor ────────────────────────────────────────
print("\n[5] Teorema Faktor: (x-a) faktor ↔ P(a)=0")
p_test = Polynomial(-6, 11, -6, 1)  # (x-1)(x-2)(x-3)
print(f"  P(x) = x^3 - 6x^2 + 11x - 6  = (x-1)(x-2)(x-3)")
for a in [1, 2, 3, 4]:
    val = p_test(a)
    is_factor = abs(val) < 1e-10
    print(f"  P({a}) = {val:.0f}  ->  (x-{a}) {'ADALAH' if is_factor else 'bukan'} faktor")

# ─── 6. Rational Root Theorem ─────────────────────────────────
print("\n[6] Rational Root Theorem")
print("  Akar rasional p/q: p | a_0, q | a_n")

def rational_roots(coeffs):
    """Cari semua kandidat akar rasional."""
    from math import gcd
    a0 = abs(int(coeffs[0]))   # constant term
    an = abs(int(coeffs[-1]))  # leading coefficient
    
    # Faktor-faktor a0 dan an
    def factors(n):
        return [i for i in range(1, n+1) if n % i == 0]
    
    p_factors = factors(a0)
    q_factors = factors(an)
    
    candidates = set()
    for p in p_factors:
        for q in q_factors:
            g = gcd(p, q)
            candidates.add(p//g / (q//g))
            candidates.add(-p//g / (q//g))
    return sorted(candidates)

# P(x) = 2x^3 - 3x^2 - 8x + 12
poly_coeffs = [12, -8, -3, 2]  # dari derajat 0 ke 3
candidates = rational_roots(poly_coeffs)
print(f"  P(x) = 2x^3 - 3x^2 - 8x + 12")
print(f"  Kandidat akar rasional: {candidates}")
p_check = Polynomial(*poly_coeffs)
actual_roots = [c for c in candidates if abs(p_check(c)) < 1e-6]
print(f"  Akar aktual: {actual_roots}")

print("\n[Selesai] Lanjut ke exercises.py")
