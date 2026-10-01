"""
Module  : Number Systems (Sistem Bilangan)
Phase   : 1 - Algebra
Topic   : 1.1
Project : MathCode Learning

Deskripsi:
    Implementasi dan eksplorasi semua sistem bilangan:
    N (Asli), W (Cacah), Z (Bulat), Q (Rasional),
    Irasional, R (Real), C (Kompleks).

Jalankan: python3 examples.py
"""

import math
import sympy
import fractions
import decimal
import cmath

# ─────────────────────────────────────────────────────────────
# SECTION 1: BILANGAN ASLI (NATURAL NUMBERS) — N = {1, 2, 3, ...}
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("SECTION 1: Bilangan Asli (Natural Numbers)")
print("=" * 60)

# Bilangan asli: digunakan untuk menghitung
natural_numbers = list(range(1, 11))
print(f"10 bilangan asli pertama: {natural_numbers}", type(natural_numbers))

# Sifat: tertutup terhadap penjumlahan dan perkalian
a, b = 7, 5
print(f"\nKlosure terhadap +: {a} + {b} = {a+b}  (masih bil. asli? {(a+b) >= 1})")
print(f"Klosure terhadap ×: {a} × {b} = {a*b}  (masih bil. asli? {(a*b) >= 1})")
print(f"Tidak tertutup - : {a} - {b*2} = {a - b*2}  (negatif, bukan bil. asli!)")

# Well-ordering: setiap himpunan non-kosong punya minimum
subset = {7, 2, 15, 3, 9}
print(f"\nWell-Ordering: min({subset}) = {min(subset)}")

# ─────────────────────────────────────────────────────────────
# SECTION 2: BILANGAN BULAT (INTEGERS) — Z = {..., -2, -1, 0, 1, 2, ...}
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("SECTION 2: Bilangan Bulat (Integers)")
print("=" * 60)

integers = list(range(-5, 6))
print(f"Z dari -5 ke 5: {integers}")

# Klosure terhadap pengurangan (yang tidak dimiliki N)
x, y = 3, 8
print(f"\nKlosure terhadap (-) : {x} - {y} = {x - y}  (ada di Z? Ya!)")

# Bilangan bulat: bisa dibandingkan secara total
nums = [-4, 7, -1, 0, 5, -9]
print(f"Diurutkan: {sorted(nums)}")

# ─────────────────────────────────────────────────────────────
# SECTION 3: BILANGAN RASIONAL — Q = {p/q | q ≠ 0}
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("SECTION 3: Bilangan Rasional (Rational Numbers)")
print("=" * 60)

# Gunakan fractions.Fraction untuk aritmetika tepat (exact)
f1 = fractions.Fraction(1, 3)   # 1/3
f2 = fractions.Fraction(1, 6)   # 1/6
print(f"1/3 = {f1} = {float(f1):.10f}...")
print(f"1/6 = {f2} = {float(f2):.10f}...")
print(f"1/3 + 1/6 = {f1 + f2}  (tepat!)")
print(f"1/3 × 3   = {f1 * 3}   (kembali ke bilangan bulat)")

# Decimal berulang -> pecahan
# 0.333... = 1/3
print(f"\n0.142857... (berulang) = {fractions.Fraction(142857, 999999)} = {fractions.Fraction(1,7)}")

# Pembuktian: desimal berulang selalu rasional
def repeating_decimal_to_fraction(integer_part, repeating_block):
    """
    Mengubah desimal berulang ke pecahan.
    Contoh: 0.142857142857... -> 1/7
    
    Rumus: jika x = 0.aaa... maka 10^n * x - x = a (untuk n digit berulang)
    """
    n = len(repeating_block)
    numerator = int(str(integer_part) + repeating_block) - integer_part
    denominator = int("9" * n)
    return fractions.Fraction(numerator, denominator)

result = repeating_decimal_to_fraction(0, "142857")
print(f"0.142857142857... = {result} ≈ {float(result):.8f}")

# ─────────────────────────────────────────────────────────────
# SECTION 4: BILANGAN IRASIONAL (IRRATIONAL NUMBERS)
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("SECTION 4: Bilangan Irasional (Irrational Numbers)")
print("=" * 60)

print(f"√2  = {math.sqrt(2):.20f}")
print(f"π   = {math.pi:.30f}")
print(f"π   = 3.141592653589793115997963468544")
print(f"e   = {math.e:.20f}")
print(f"φ   = {(1 + math.sqrt(5)) / 2:.20f}  (golden ratio)")

# Demonstrasi bukti √2 irasional (approach komputasional):
# Jika √2 = p/q, cari p dan q terkecil — tidak akan pernah exact
def check_sqrt2_rationality(precision=50):
    """
    Tunjukkan bahwa tidak ada p/q yang persis sama dengan √2.
    Kita cari Fraction yang mendekati √2, tapi selalu ada error.
    """
    sqrt2 = decimal.Decimal(2).sqrt()
    # Konversi ke Fraction — akan menghasilkan approx, bukan exact
    approx = fractions.Fraction(math.sqrt(2)).limit_denominator(10**6)
    actual = float(approx)
    error = abs(actual - math.sqrt(2))
    print(f"\nApproksimasi terbaik √2 ≈ {approx}")
    print(f"Nilai desimalnya      = {actual:.15f}")
    print(f"√2 sebenarnya         = {math.sqrt(2):.15f}")
    print(f"Error                 = {error:.2e}  (tidak pernah nol!)")

check_sqrt2_rationality()

# ─────────────────────────────────────────────────────────────
# SECTION 5: BILANGAN KOMPLEKS (COMPLEX NUMBERS) — C = {a + bi}
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("SECTION 5: Bilangan Kompleks (Complex Numbers)")
print("=" * 60)

z1 = complex(3, 4)    # 3 + 4i
z2 = complex(1, -2)   # 1 - 2i

print(f"z1 = {z1}  -> Re={z1.real}, Im={z1.imag}")
print(f"z2 = {z2}  -> Re={z2.real}, Im={z2.imag}")

# Operasi dasar
print(f"\nz1 + z2 = {z1 + z2}")
print(f"z1 - z2 = {z1 - z2}")
print(f"z1 × z2 = {z1 * z2}")
print(f"z1 / z2 = {z1 / z2:.4f}")

# Modulus dan argumen
print(f"\n|z1| = {abs(z1)}  (= √(3²+4²) = √25 = 5)")
print(f"arg(z1) = {cmath.phase(z1):.4f} radian = {math.degrees(cmath.phase(z1)):.2f}°")

# Konjugat
z1_conj = z1.conjugate()
print(f"\nKonjugat z1 = {z1_conj}")
print(f"z1 × z1_conj = {z1 * z1_conj}  (= |z1|² = 25)")

# Formula Euler: e^(iπ) + 1 = 0
euler = cmath.exp(complex(0, math.pi)) + 1
print(f"\nFormula Euler: e^(iπ) + 1 = {euler:.10f}  (≈ 0)")

# ─────────────────────────────────────────────────────────────
# SECTION 6: CLASSIFIER — Tentukan jenis bilangan
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("SECTION 6: Number System Classifier")
print("=" * 60)


def classify_number(x):
    systems = []
    
    # Bilangan kompleks — semua bilangan adalah kompleks
    systems.append("Complex (C)")
    
    # Konversi ke tipe sympy jika memungkinkan untuk deteksi simbolik irasional
    sym_x = sympy.sympify(x)
    
    # Cek apakah real (bagian imajiner = 0)
    # Gunakan fungsi bawaan sympy untuk mengecek komponen imajiner
    if sym_x.is_real is False:
        return systems  # Hanya kompleks
        
    systems.append("Real (R)")
    
    # STRATEGI BARU: Deteksi irasional menggunakan keunggulan simbolik sympy
    # Modul sympy tahu secara mutlak bahwa sqrt(2) dan pi adalah irasional
    if sym_x.is_irrational:
        systems.append("Irrational")
        return systems
        
    # Jika lolos ke bawah, berarti bilangan tersebut pasti Rasional
    systems.append("Rational (Q)")
    
    # Untuk pengecekan Integer ke bawah, kita kembalikan ke float/int biasa
    # agar tidak bentrok dengan tipe data khusus sympy
    val = float(sym_x)
    
    if int(val) == val:
        systems.append("Integer (Z)")
        if val >= 0:
            systems.append("Whole (W)")
            if val > 0:
                systems.append("Natural (N)")
                
    return systems

# Saat mendaftarkan test_numbers, ganti fungsi math biasa 
# menjadi fungsi simbolik milik sympy agar tipenya terbaca benar
test_numbers = [
    (5, "5"),
    (0, "0"),
    (-3, "-3"),
    (0.5, "0.5 = 1/2"),
    (sympy.sqrt(2), "√2"),  # Ganti math.sqrt menjadi sympy.sqrt
    (sympy.pi, "π"),       # Ganti math.pi menjadi sympy.pi
    (complex(0, 1), "i"),
]

for num, label in test_numbers:
    cats = classify_number(num)
    print(f"{label:15} ∈ {' ⊂ '.join(reversed(cats))}")

# ─────────────────────────────────────────────────────────────
# SECTION 7: NOTASI INTERVAL
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("SECTION 7: Notasi Interval dan Keanggotaan")
print("=" * 60)

def in_interval(x, a, b, left_open=False, right_open=False):
    """
    Cek apakah x ada dalam interval (a,b), [a,b], [a,b), atau (a,b].
    left_open=True  → kurung kiri terbuka: x > a
    right_open=True → kurung kanan terbuka: x < b
    """
    left_ok  = (x > a) if left_open  else (x >= a)
    right_ok = (x < b) if right_open else (x <= b)
    return left_ok and right_ok

# Test berbagai interval
test_x = 3.5
print(f"x = {test_x}")
print(f"x ∈ (1, 5)  ? {in_interval(test_x, 1, 5, True, True)}")
print(f"x ∈ [1, 5]  ? {in_interval(test_x, 1, 5, False, False)}")
print(f"x ∈ [3.5, 7)? {in_interval(test_x, 3.5, 7, False, True)}")
print(f"x ∈ (3.5, 7)? {in_interval(test_x, 3.5, 7, True, True)}")

# ─────────────────────────────────────────────────────────────
# SECTION 8: FUNGSI LANTAI DAN PLAFON
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 60)
print("SECTION 8: Floor ⌊x⌋ dan Ceiling ⌈x⌉")
print("=" * 60)

def my_floor(x):
    """Floor tanpa math.floor — implementasi manual."""
    return int(x) if x >= 0 else int(x) - (1 if x != int(x) else 0)

def my_ceiling(x):
    """Ceiling tanpa math.ceil — implementasi manual."""
    fl = my_floor(x)
    return fl if x == fl else fl + 1

values = [3.7, -2.3, 5.0, -0.1, 0.9]
print(f"{'x':>8} | {'⌊x⌋':>6} | {'⌈x⌉':>6} | {'check floor':>12} | {'check ceil':>12}")
print("-" * 60)
for v in values:
    print(f"{v:>8.1f} | {my_floor(v):>6} | {my_ceiling(v):>6} | {math.floor(v):>12} | {math.ceil(v):>12}")

print("\n[Selesai] Semua contoh bilangan telah dijalankan!")
print("Lanjut ke: exercises.py")
