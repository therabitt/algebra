"""
Challenge: Factorization  |  Phase 1 — Topic 1.10
"""
print("CHALLENGE 1.10 — FAKTORISASI")

# KONSEP: Faktorisasi tingkat lanjut menggunakan identitas aljabar dan algoritma polinom.
# ALGORITMA & KONSEP:
# Ch1: Identitas Sophie Germain a^4 + 4b^4 = (a^2+2b^2+2ab)(a^2+2b^2-2ab).
# Ch2: GCD (FPB) Polinomial bisa dicari menggunakan Euclidean Algorithm untuk polinomial.
# Ch3: Akar dari polinomial derajat n adalah n buah (termasuk kompleks).

# LANGKAH:
# 1. Implementasikan faktorisasi x^4 + 4 dengan Identitas Sophie Germain
# 2. Cari GCD dari dua polinomial (x^3-x) dan (x^2-1)
# 3. Cari akar kompleks dari x^4 + 1 = 0

# IMPLEMENTASIKAN:
try:
    import sympy as sp
    x = sp.Symbol("x")
    
    print("\n[Ch1] Faktorisasi atas berbagai bilangan:")
    expr = x**4 + 4
    print(f"  {expr}:")
    # TODO: Gunakan Identitas Sophie Germain untuk memfaktorkan x^4 + 4
    # TODO: Verifikasi dengan melakukan ekspansi
    pass
    
    print("\n[Ch2] GCF Polinomial:")
    from sympy import gcd, Poly
    # TODO: Cari GCD dari x^3 - x dan x^2 - 1 menggunakan sympy
    pass
    
    print("\n[Ch3] Akar kompleks menggunakan faktorisasi:")
    expr2 = x**4 + 1
    # TODO: Selesaikan persamaan x^4 + 1 = 0 untuk mendapatkan akar kompleksnya
    pass

except ImportError:
    print("sympy diperlukan untuk challenge ini: pip install sympy")

print("\n[Selesai Challenge 1.10]")
