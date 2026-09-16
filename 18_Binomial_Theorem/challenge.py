"""
Challenge: Binomial Theorem  |  Phase 1 — Topic 1.19
"""
import math
print("CHALLENGE 1.19 — TEOREMA BINOMIAL")

def C(n,k):
    if k<0 or k>n: return 0
    k=min(k,n-k); r=1
    for i in range(k): r=r*(n-i)//(i+1)
    return r

# Challenge 1: Catalan Numbers from Binomial
print("\n[Ch1] Bilangan Catalan dari Koefisien Binomial")
print("  Catalan(n) = C(2n,n) / (n+1)")
print("  Mengitung banyaknya cara meng-bracket ekspresi, triangulasi poligon, dll.")
def catalan(n): return C(2*n, n) // (n+1)
catalan_nums = [catalan(n) for n in range(10)]
print(f"  C(0..9) = {catalan_nums}")
print(f"  Verifikasi rekursi C(n) = Σ C(i)·C(n-1-i):")
for n in range(2, 6):
    via_sum = sum(catalan(i)*catalan(n-1-i) for i in range(n))
    print(f"    C({n}) = {catalan(n)},  via sum = {via_sum}  ✓{catalan(n)==via_sum}")

# Challenge 2: Multinomial theorem
print("\n[Ch2] Teorema Multinomial")
print("  (x+y+z)^n = Σ n!/(i!j!k!) · x^i · y^j · z^k  (i+j+k=n)")

def multinomial_expand(n):
    """Ekspansi (x+y+z)^n, kembalikan koefisien {(i,j,k): coef}."""
    from math import factorial
    result = {}
    for i in range(n+1):
        for j in range(n-i+1):
            k = n-i-j
            coef = factorial(n) // (factorial(i)*factorial(j)*factorial(k))
            result[(i,j,k)] = coef
    return result

print("  (x+y+z)^3, beberapa suku:")
terms = multinomial_expand(3)
for (i,j,k), coef in sorted(terms.items(), reverse=True)[:8]:
    label = f"{coef}x^{i}y^{j}z^{k}" if coef>1 else f"x^{i}y^{j}z^{k}"
    print(f"    {label}")
print(f"  Total suku: {len(terms)}")
print(f"  Jumlah koefisien: {sum(terms.values())} = 3^3 = {3**3}")

# Challenge 3: Generating function
print("\n[Ch3] Generating Function (1+x)^n")
print("  Kita hitung koefisien pangkat x^k dari (1+x)^n menggunakan konvolusi")

def poly_power(n):
    """Hitung koefisien dari (1+x)^n dengan perkalian polinomial berulang."""
    result = [1]  # (1+x)^0 = 1
    base = [1, 1]  # (1+x)
    for _ in range(n):
        new = [0] * (len(result) + 1)
        for i, a in enumerate(result):
            for j, b in enumerate(base):
                new[i+j] += a * b
        result = new
    return result

for n in [3, 5, 8]:
    coeffs = poly_power(n)
    pascal_row = [C(n,k) for k in range(n+1)]
    print(f"  n={n}: {coeffs}  == Pascal? {coeffs==pascal_row}")

print("\n[Selesai Challenge 1.19]")
