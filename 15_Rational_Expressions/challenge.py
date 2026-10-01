"""
Challenge: Rational Expressions  |  Phase 1 — Topic 1.16
"""
print("CHALLENGE 1.16 — PECAHAN ALJABAR")

try:
    import sympy as sp
    x = sp.Symbol('x')

    # Challenge 1: Build partial fraction integrator
    # KONSEP: Integral dari fungsi rasional sering kali bisa diselesaikan dengan mendekomposisinya ke pecahan parsial terlebih dahulu.
    # LANGKAH:
    # 1. Dekomposisi integrand (2x+3)/((x+1)(x-2)) menggunakan sympy.apart
    # 2. Integrasikan hasil dekomposisi tersebut
    # 3. Verifikasi dengan menurunkan (diferensiasi) hasil integral
    # IMPLEMENTASIKAN:
    print("\n[Ch1] Integrasi melalui Dekomposisi Parsial")
    print("  ∫ (2x+3)/((x+1)(x-2)) dx")
    # TODO: Hitung dekomposisi, integral, dan verifikasi
    pass

    # Challenge 2: Continued fractions as rational expressions
    # KONSEP: Pecahan berlanjut (continued fractions) dapat disederhanakan menjadi fungsi rasional standar.
    # LANGKAH:
    # 1. Tulis ekspresi pecahan secara berurut atau nested
    # 2. Sederhanakan menggunakan fungsi simplify dari sympy
    # IMPLEMENTASIKAN:
    print("\n[Ch2] Continued Fraction sebagai Ekspresi Rasional")
    print("  1 + 1/(1 + 1/(1 + 1/x))")
    # TODO: Evaluasi dan sederhanakan expr
    pass

    # Challenge 3: Rational function interpolation
    # KONSEP: Padé approximant menggunakan fungsi rasional untuk mengaproksimasi fungsi (biasanya lebih baik dari deret Taylor).
    # LANGKAH:
    # 1. Padé approximant [1,1] untuk e^x adalah (1 + x/2) / (1 - x/2)
    # 2. Hitung nilai aproksimasi tersebut pada titik-titik uji
    # 3. Bandingkan dengan nilai aktual e^x dan aproksimasi Taylor (1 + x)
    # IMPLEMENTASIKAN:
    print("\n[Ch3] Interpolasi Rasional — Padé Approximant")
    import math
    # TODO: Bandingkan e^x dengan Padé approximant dan Taylor approximant
    pass

except ImportError:
    print("  sympy diperlukan: pip install sympy")

print("\n[Selesai Challenge 1.16]")
