"""
Module  : Binomial Theorem (Teorema Binomial)
Phase   : 1 - Algebra  |  Topic: 1.19
Jalankan: python3 examples.py
"""
import math

print("=" * 60)
print("TEOREMA BINOMIAL — CONTOH IMPLEMENTASI")
print("=" * 60)

# ─── 1. Koefisien Binomial ────────────────────────────────────
print("\n[1] Koefisien Binomial C(n,k) = n! / (k!(n-k)!)")

def comb(n, k):
    """Hitung C(n,k) dari nol menggunakan formula."""
    if k < 0 or k > n: return 0
    if k == 0 or k == n: return 1
    k = min(k, n-k)  # manfaatkan simetri C(n,k)=C(n,n-k)
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result

print(f"  C(5,2)  = {comb(5,2)}   (expected: {math.comb(5,2)})")
print(f"  C(10,3) = {comb(10,3)}  (expected: {math.comb(10,3)})")
print(f"  C(6,0)  = {comb(6,0)}   (expected: 1)")
print(f"  C(6,6)  = {comb(6,6)}   (expected: 1)")
print(f"  C(8,4)  = {comb(8,4)}   (expected: {math.comb(8,4)})")

# ─── 2. Segitiga Pascal ───────────────────────────────────────
print("\n[2] Segitiga Pascal")

def pascal_triangle(n_rows):
    """Buat segitiga Pascal."""
    triangle = []
    for n in range(n_rows):
        row = [comb(n, k) for k in range(n+1)]
        triangle.append(row)
    return triangle

triangle = pascal_triangle(10)
print("  Baris 0-9:")
max_width = len("  ".join(map(str, triangle[9])))
for n, row in enumerate(triangle):
    row_str = "  ".join(f"{v:>3}" for v in row)
    print(f"  n={n}: " + " " * ((max_width - len(row_str))//2) + row_str)

# Verifikasi: Σ C(n,k) = 2^n
print("\n  Verifikasi Σ C(n,k) = 2^n:")
for n in [0,1,2,5,8]:
    total = sum(comb(n,k) for k in range(n+1))
    print(f"  n={n}: Σ={total} = 2^{n}={2**n}  ✓{total==2**n}")

# ─── 3. Ekspansi Binomial ─────────────────────────────────────
print("\n[3] Ekspansi (a+b)^n")

def binomial_expand(a, b, n, var_a="a", var_b="b"):
    """
    Ekspansi (a+b)^n. Jika a,b adalah simbol string, tampilkan koefisien.
    Jika numerik, hitung nilainya.
    """
    terms = []
    for k in range(n+1):
        coef = comb(n, k)
        power_a = n - k
        power_b = k
        if isinstance(a, str):
            term = f"{coef}"
            if power_a > 0:
                term += f"{var_a}"
                if power_a > 1: term += f"^{power_a}"
            if power_b > 0:
                term += f"{var_b}"
                if power_b > 1: term += f"^{power_b}"
            terms.append(term)
        else:
            terms.append(coef * (a**power_a) * (b**power_b))
    return terms

# Simbolis
for n in [2, 3, 4, 5]:
    terms = binomial_expand("a", "b", n)
    print(f"  (a+b)^{n} = {' + '.join(terms)}")

# Numerik
print(f"\n  (2+3)^4:")
terms_num = binomial_expand(2, 3, 4)
print(f"  = {' + '.join(map(str, terms_num))} = {sum(terms_num)}")
print(f"  (2+3)^4 = 5^4 = {5**4}  ✓")

# ─── 4. Suku Umum ────────────────────────────────────────────
print("\n[4] Suku Umum T_{k+1} = C(n,k) · a^(n-k) · b^k")

def general_term(a, b, n, k):
    """Suku ke-(k+1) dari ekspansi (a+b)^n."""
    return comb(n, k) * (a**(n-k)) * (b**k)

# Contoh: (x+2)^7, cari suku ke-4 (k=3)
print("  Ekspansi (x+2)^7, suku ke-4 (k=3):")
print("  T_4 = C(7,3) · x^4 · 2^3")
print(f"      = {comb(7,3)} · x^4 · {2**3}")
print(f"      = {comb(7,3)*2**3}x^4")

# ─── 5. Identitas Binomial ───────────────────────────────────
print("\n[5] Identitas Binomial")

for n in range(1, 8):
    # Alternating sum = 0
    alt_sum = sum((-1)**k * comb(n,k) for k in range(n+1))
    # Row sum = 2^n
    row_sum = sum(comb(n,k) for k in range(n+1))
    print(f"  n={n}: Σ(-1)^k·C(n,k) = {alt_sum:>3} (should be 0)  |  ΣC(n,k) = {row_sum:>3} = 2^n = {2**n}")

# ─── 6. Aproksimasi Binomial ─────────────────────────────────
print("\n[6] Aproksimasi Binomial: (1+x)^n ≈ 1+nx  untuk |x|<<1")

print(f"  {'x':>8} | {'n':>4} | {'Exact':>12} | {'1+nx':>12} | {'Error%':>10}")
approx_cases = [(0.01, 10), (0.05, 20), (0.001, 100), (-0.02, 5)]
for x, n in approx_cases:
    exact = (1+x)**n
    approx = 1 + n*x
    error_pct = abs(exact-approx)/exact * 100
    print(f"  {x:>8.4f} | {n:>4} | {exact:>12.8f} | {approx:>12.8f} | {error_pct:>10.4f}%")

# ─── 7. Distribusi Binomial ──────────────────────────────────
print("\n[7] Distribusi Binomial: P(X=k) = C(n,k)·p^k·(1-p)^(n-k)")

def binomial_prob(n, k, p):
    return comb(n, k) * (p**k) * ((1-p)**(n-k))

print("  Lempar koin adil (p=0.5) sebanyak 10 kali:")
print(f"  {'k (heads)':>12} | {'P(X=k)':>10}")
n, p = 10, 0.5
total_prob = 0
for k in range(n+1):
    prob = binomial_prob(n, k, p)
    total_prob += prob
    bar = "█" * int(prob * 100)
    print(f"  {k:>12} | {prob:>10.4f}  {bar}")
print(f"  Total: {total_prob:.6f} (should be 1.0)")

print("\n[Selesai] Lanjut ke exercises.py")
