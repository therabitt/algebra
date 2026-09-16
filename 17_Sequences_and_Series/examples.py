"""
Module  : Sequences and Series (Barisan dan Deret)
Phase   : 1 - Algebra  |  Topic: 1.12
Jalankan: python3 examples.py
"""
import math

print("=" * 60)
print("BARISAN DAN DERET — CONTOH IMPLEMENTASI")
print("=" * 60)

# ─── 1. Barisan Aritmetika ────────────────────────────────────
print("\n[1] Barisan Aritmetika: a_n = a_1 + (n-1)d")

def arithmetic_sequence(a1, d, n):
    """Generate n suku barisan aritmetika."""
    return [a1 + (k-1)*d for k in range(1, n+1)]

def arithmetic_nth(a1, d, n):
    """Suku ke-n barisan aritmetika."""
    return a1 + (n-1)*d

def arithmetic_sum(a1, d, n):
    """Jumlah n suku pertama: Sn = n(a1 + an)/2"""
    an = arithmetic_nth(a1, d, n)
    return n * (a1 + an) // 2 if (n*(a1+an)) % 2 == 0 else n*(a1+an)/2

a1, d = 3, 5
print(f"  a1={a1}, d={d}")
print(f"  10 suku pertama: {arithmetic_sequence(a1, d, 10)}")
print(f"  Suku ke-20: {arithmetic_nth(a1, d, 20)}")
print(f"  Jumlah 10 suku: {arithmetic_sum(a1, d, 10)}")
print(f"  Verifikasi: n(a1+an)/2 = 10*({a1}+{arithmetic_nth(a1,d,10)})/2 = {10*(a1+arithmetic_nth(a1,d,10))//2}")

# ─── 2. Barisan Geometrika ────────────────────────────────────
print("\n[2] Barisan Geometrika: a_n = a_1 * r^(n-1)")

def geometric_sequence(a1, r, n):
    return [a1 * r**(k-1) for k in range(1, n+1)]

def geometric_nth(a1, r, n):
    return a1 * r**(n-1)

def geometric_sum_finite(a1, r, n):
    """Sn = a1(1-r^n)/(1-r)  untuk r != 1"""
    if abs(r - 1) < 1e-12:
        return a1 * n
    return a1 * (1 - r**n) / (1 - r)

def geometric_sum_infinite(a1, r):
    """S = a1/(1-r)  untuk |r| < 1"""
    if abs(r) >= 1:
        return float("inf")
    return a1 / (1 - r)

a1, r = 2, 3
print(f"  a1={a1}, r={r}")
print(f"  8 suku: {geometric_sequence(a1, r, 8)}")
print(f"  Suku ke-6: {geometric_nth(a1, r, 6)}")
print(f"  Jumlah 6 suku: {geometric_sum_finite(a1, r, 6):.2f}")

a1_inf, r_inf = 4, 0.5
S_inf = geometric_sum_infinite(a1_inf, r_inf)
print(f"\n  Deret tak hingga: a1={a1_inf}, r={r_inf}")
print(f"  S = a1/(1-r) = {a1_inf}/(1-{r_inf}) = {S_inf}")
print(f"  Verifikasi (100 suku): {geometric_sum_finite(a1_inf, r_inf, 100):.8f}")

# ─── 3. Barisan Fibonacci ─────────────────────────────────────
print("\n[3] Barisan Fibonacci: F(n) = F(n-1) + F(n-2)")

# Metode 1: Rekursif (lambat untuk n besar)
def fib_recursive(n):
    if n <= 1: return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# Metode 2: Iteratif (O(n))
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a+b
    return a

# Metode 3: Formula Binet (O(1)) — tapi ada floating point error untuk n besar
phi = (1 + math.sqrt(5)) / 2
def fib_binet(n):
    return round(phi**n / math.sqrt(5))

print(f"  20 suku Fibonacci: {[fib_iterative(i) for i in range(20)]}")
print(f"\n  Binet's formula: F(n) = φ^n/√5 (dibulatkan)")
print(f"  φ (golden ratio) = {phi:.10f}")
for n in [10, 20, 30]:
    fi = fib_iterative(n); fb = fib_binet(n)
    print(f"  F({n}) iteratif={fi}, binet={fb}, sama?{fi==fb}")

# ─── 4. Rasio Fibonacci -> Golden Ratio ──────────────────────
print("\n[4] F(n)/F(n-1) -> Golden Ratio φ")
for n in range(2, 16):
    ratio = fib_iterative(n) / fib_iterative(n-1)
    print(f"  F({n})/F({n-1}) = {ratio:.8f}  (φ = {phi:.8f})")

# ─── 5. Notasi Sigma ─────────────────────────────────────────
print("\n[5] Notasi Sigma (Penjumlahan)")
print("  Σ(k=1 to n) k = n(n+1)/2")
for n in [5, 10, 100]:
    direct = sum(range(1, n+1))
    formula = n*(n+1)//2
    print(f"  Σk (k=1..{n}) = {direct} = {formula}  ✓{direct==formula}")

print("  Σk^2 = n(n+1)(2n+1)/6")
for n in [5, 10]:
    direct = sum(k**2 for k in range(1, n+1))
    formula = n*(n+1)*(2*n+1)//6
    print(f"  Σk² (k=1..{n}) = {direct} = {formula}  ✓{direct==formula}")

# ─── 6. Konvergensi Deret Tak Hingga ─────────────────────────
print("\n[6] Konvergensi Deret Tak Hingga")
# 1 + 1/2 + 1/4 + 1/8 + ... = 2
partial_sums = []
s = 0
for k in range(50):
    s += (0.5)**k
    if k < 10 or k == 49:
        partial_sums.append((k, s))
print("  Σ(1/2)^k untuk k=0..∞:")
for k, s in partial_sums:
    print(f"  n={k:>3}: S = {s:.10f}  (menuju 2? {abs(s-2):.2e})")

print("\n[Selesai]")
