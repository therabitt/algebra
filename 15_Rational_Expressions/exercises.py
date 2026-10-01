"""
Exercises: Rational Expressions  |  Phase 1 — Topic 1.16
"""
print("LATIHAN 1.16 — PECAHAN ALJABAR")
print("=" * 50)

try:
    import sympy as sp
    x = sp.Symbol('x')

    # Ex 1: Simplify
    # KONSEP: Menyederhanakan pecahan aljabar dilakukan dengan memfaktorkan pembilang dan penyebut, lalu mencoret faktor yang sama.
    # LANGKAH:
    # 1. Faktorkan polinomial pada pembilang dan penyebut
    # 2. Hapus faktor persekutuan
    # 3. Cek hasil yang sudah disederhanakan
    # IMPLEMENTASIKAN:
    print("\n[Ex 1] Sederhanakan ekspresi rasional:")
    # TODO: Sederhanakan (x^2-9)/(x-3), (2x^2-5x-3)/(x-3), dan (x^3-8)/(x-2) menggunakan sympy.simplify
    pass

    # Ex 2: Add/Subtract
    # KONSEP: Penjumlahan pecahan aljabar membutuhkan penyebut yang sama (KPK).
    # LANGKAH:
    # 1. Cari KPK dari penyebut-penyebut
    # 2. Kalikan pembilang dengan faktor yang sesuai agar penyebut sama
    # 3. Jumlahkan pembilang dan sederhanakan
    # IMPLEMENTASIKAN:
    print("\n[Ex 2] Hitung:")
    # TODO: Hitung 1/(x-1) + 2/(x+1) dan 3/(x^2-4) - 1/(x+2)
    pass

    # Ex 3: Solve rational equations
    # KONSEP: Persamaan rasional diselesaikan dengan mengalikan kedua ruas dengan KPK penyebut, asalkan solusi tidak membuat penyebut asli menjadi 0.
    # LANGKAH:
    # 1. Susun persamaan menggunakan sympy.Eq
    # 2. Selesaikan terhadap x menggunakan sympy.solve
    # IMPLEMENTASIKAN:
    print("\n[Ex 3] Selesaikan:")
    # TODO: Selesaikan 1/(x-2) = 3/(x+2) dan (x+1)/(x-1) - 2/(x+1) = 2
    pass

    # Ex 4: Partial fractions
    # KONSEP: Dekomposisi pecahan parsial adalah memecah pecahan rasional yang kompleks menjadi penjumlahan pecahan-pecahan sederhana.
    # LANGKAH:
    # 1. Pastikan derajat pembilang < derajat penyebut
    # 2. Faktorkan penyebut
    # 3. Gunakan sympy.apart untuk mendekomposisi
    # IMPLEMENTASIKAN:
    print("\n[Ex 4] Dekomposisi Parsial:")
    # TODO: Hitung partial fractions untuk (3x+5)/((x+1)(x+2)) dan x^2/((x-1)(x+1)^2)
    pass

except ImportError:
    print("  [Manual] sympy diperlukan: pip install sympy")
    pass

print("\n[Selesai]")
