"""
Exercises: Sequences and Series  |  Phase 1 — Topic 1.12
"""
import math
print("LATIHAN 1.12 — BARISAN DAN DERET")
print("=" * 50)

def arith_nth(a1,d,n): return a1+(n-1)*d
def arith_sum(a1,d,n):
    an = arith_nth(a1,d,n)
    return n*(a1+an)/2
def geo_nth(a1,r,n): return a1*r**(n-1)
def geo_sum(a1,r,n):
    if abs(r-1)<1e-12: return a1*n
    return a1*(1-r**n)/(1-r)
def geo_inf(a1,r): return a1/(1-r) if abs(r)<1 else float("inf")

# Ex 1
print("\n[Ex 1] Barisan aritmetika: a1=7, d=4")
a1,d = 7,4
print(f"  Suku ke-15: {arith_nth(a1,d,15)}")
print(f"  Jumlah 20 suku: {arith_sum(a1,d,20)}")
print(f"  10 suku: {[arith_nth(a1,d,n) for n in range(1,11)]}")

# Ex 2
print("\n[Ex 2] Barisan geometrika: a1=3, r=2")
a1,r = 3,2
print(f"  Suku ke-8: {geo_nth(a1,r,8)}")
print(f"  Jumlah 8 suku: {geo_sum(a1,r,8):.2f}")

# Ex 3
print("\n[Ex 3] Deret tak hingga: a1=12, r=1/3")
S = geo_inf(12, 1/3)
print(f"  S∞ = {12}/(1-{1/3:.4f}) = {S:.6f}")

# Ex 4
print("\n[Ex 4] Cari suku tengah dan jumlah:")
print("  Barisan: 5, 8, 11, 14, ..., 50")
a1,d = 5,3
n = (50-5)//3 + 1
print(f"  Jumlah suku: {n}")
print(f"  Jumlah: {arith_sum(a1,d,n):.0f}")

# Ex 5
print("\n[Ex 5] Barisan Fibonacci")
def fib(n):
    a,b = 0,1
    for _ in range(n): a,b=b,a+b
    return a
first_20 = [fib(i) for i in range(20)]
print(f"  F(0..19): {first_20}")
print(f"  Jumlah 10 pertama: {sum(first_20[:10])}")

# Ex 6
print("\n[Ex 6] Bunga Majemuk sebagai Barisan Geometrika")
P, r_year = 10_000_000, 0.06
r_month = 1 + r_year/12
print(f"  P=Rp{P:,.0f}, bunga 6%/tahun (0.5%/bulan)")
for n_months in [12, 24, 60, 120]:
    A = P * r_month**n_months
    print(f"  {n_months//12} tahun ({n_months} bulan): Rp {A:,.2f}")

print("\n[Selesai]")
