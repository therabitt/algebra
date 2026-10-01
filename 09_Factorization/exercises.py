"""
Exercises: Factorization  |  Phase 1 — Topic 1.10
"""
print("LATIHAN 1.10 — FAKTORISASI")
print("=" * 50)

# KONSEP:
# Faktorisasi adalah kebalikan dari ekspansi. Tujuannya mengubah bentuk 
# penjumlahan/pengurangan menjadi perkalian faktor-faktor.
# Beberapa pola umum: a^2 - b^2 = (a-b)(a+b), a^2 + 2ab + b^2 = (a+b)^2
# 
# LANGKAH:
# 1. Identifikasi bentuk ekspresi (selisih kuadrat, kuadrat sempurna, dll)
# 2. Terapkan rumus faktorisasi yang sesuai
# 3. Verifikasi dengan mengekspansi kembali hasil faktorisasi

# IMPLEMENTASIKAN:
try:
    import sympy as sp
    x = sp.Symbol("x")
    problems = [
        ("x^2 - 16",           x**2-16,       "(x+4)(x-4)"),
        ("x^2 + 8x + 16",      x**2+8*x+16,   "(x+4)^2"),
        ("2x^2 + 7x + 3",      2*x**2+7*x+3,  "(2x+1)(x+3)"),
        ("x^3 - 27",           x**3-27,        "(x-3)(x^2+3x+9)"),
        ("x^2 - 5x + 6",       x**2-5*x+6,    "(x-2)(x-3)"),
        ("6x^2 - 11x + 4",     6*x**2-11*x+4, "(2x-1)(3x-4)"),
        ("x^4 - 81",           x**4-81,        "(x^2+9)(x+3)(x-3)"),
        ("4x^2 - 12x + 9",     4*x**2-12*x+9, "(2x-3)^2"),
    ]
    print(f"  {'Ekspresi':>25} | {'Faktorisasi':>25} | {'Benar?':>8}")
    print("-" * 70)
    for label, expr, expected in problems:
        # TODO: Lakukan faktorisasi pada 'expr' menggunakan sympy (sp.factor)
        # TODO: Lakukan verifikasi dengan mengekspansi kembali hasilnya
        pass

except ImportError:
    print("[Manual solutions]")
    # TODO: Tulis hasil faktorisasi manual jika sympy tidak tersedia
    pass

print("\n[Selesai]")
