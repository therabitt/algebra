"""
Exercises: Binomial Theorem  |  Phase 1 — Topic 1.19
"""
import math
print("LATIHAN 1.19 — TEOREMA BINOMIAL")
print("=" * 50)

def C(n,k):
    if k<0 or k>n: return 0
    k=min(k,n-k)
    r=1
    for i in range(k): r=r*(n-i)//(i+1)
    return r

# Ex 1: Pascal row
print("\n[Ex 1] Tulis baris ke-7 Segitiga Pascal:")
row7 = [C(7,k) for k in range(8)]
print(f"  {row7}")
print(f"  Jumlah: {sum(row7)} = 2^7 = {2**7}")

# Ex 2: Expand
print("\n[Ex 2] Ekspansi:")
print("  (x+y)^5:")
terms = [f"{C(5,k)}x^{5-k}y^{k}" if k>0 and k<5
         else (f"{C(5,k)}x^{5-k}" if k==0 else f"{C(5,k)}y^{k}")
         for k in range(6)]
print(f"  = {' + '.join(terms)}")

print("  (2x-3)^4: (a=2x, b=-3)")
terms2 = [C(4,k) * (2**(4-k)) * ((-3)**k) for k in range(5)]
# labels: k=0: a^4, k=1: a^3b, ...
for k in range(5):
    coef = C(4,k) * (2**(4-k)) * ((-3)**k)
    pow_x = 4-k
    s = f"{'+' if coef>=0 else ''}{coef}x^{pow_x}" if pow_x>0 else f"{coef}"
    print(f"    k={k}: {s}")

# Ex 3: Find specific term
print("\n[Ex 3] Temukan suku spesifik:")
print("  Dalam (3x - 1/x)^6, temukan suku yang tidak memuat x:")
print("  T_{k+1} = C(6,k)·(3x)^(6-k)·(-1/x)^k")
print("  = C(6,k)·3^(6-k)·(-1)^k · x^(6-k) · x^(-k)")
print("  = C(6,k)·3^(6-k)·(-1)^k · x^(6-2k)")
print("  Suku bebas x: 6-2k=0  ->  k=3")
k=3; n=6
coef = C(n,k) * (3**(n-k)) * ((-1)**k)
print(f"  k=3: C(6,3)·3^3·(-1)^3 = {C(6,3)}·{3**3}·{(-1)**3} = {coef}")

# Ex 4: Approximation
print("\n[Ex 4] Gunakan aproksimasi binomial:")
print("  (1.02)^8 ≈ 1 + 8(0.02) = 1.16  (aproksimasi orde 1)")
exact = 1.02**8
approx1 = 1 + 8*0.02
approx2 = 1 + 8*0.02 + math.comb(8,2)*0.02**2  # orde 2
print(f"  Aprox orde 1: {approx1:.6f}")
print(f"  Aprox orde 2: {approx2:.6f}")
print(f"  Nilai exact:  {exact:.6f}")
print(f"  Error orde 1: {abs(exact-approx1)/exact*100:.4f}%")
print(f"  Error orde 2: {abs(exact-approx2)/exact*100:.4f}%")

# Ex 5: Binomial probability
print("\n[Ex 5] Probabilitas: ujian 20 soal, P(benar)=0.7, P(≥15 benar)?")
n, p = 20, 0.7
prob_ge15 = sum(C(n,k)*(p**k)*((1-p)**(n-k)) for k in range(15,n+1))
print(f"  P(X≥15) = {prob_ge15:.6f} = {prob_ge15*100:.2f}%")

print("\n[Selesai]")
