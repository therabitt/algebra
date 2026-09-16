"""
Exercises: Number Systems (Sistem Bilangan)
Phase 1 — Topic 1.1

Petunjuk: Coba kerjakan sendiri dulu sebelum melihat solusi!
Uncomment bagian SOLUTION untuk melihat jawaban.
"""

import math
import fractions

print("=" * 60)
print("LATIHAN 1.1 — SISTEM BILANGAN")
print("=" * 60)

# ─────────────────────────────────────────────────────────────
# Exercise 1: Klasifikasi Bilangan
# ─────────────────────────────────────────────────────────────
print("\n[Exercise 1] Klasifikasikan bilangan berikut ke dalam")
print("sistem bilangan yang tepat (N, W, Z, Q, Irasional, C):")
print("  a) -7")
print("  b) 0")
print("  c) 3/4")
print("  d) √5")
print("  e) 2 + 3i")
print("  f) -3/1")
print("\n# Tulis jawaban kamu di sini:")
# jawaban_1a = ?

# --- SOLUTION ---
# a) -7  → Z (bulat), Q (rasional), R (real), C (kompleks)
# b) 0   → W (cacah), Z (bulat), Q (rasional), R (real), C (kompleks)
# c) 3/4 → Q (rasional), R (real), C (kompleks)  [bukan Z karena bukan bulat]
# d) √5  → Irasional, R (real), C (kompleks)
# e) 2+3i→ C (kompleks) saja
# f) -3/1→ Z (bulat), Q (rasional), R (real), C (kompleks)

def solution_1():
    numbers = {
        "-7"  : (-7, "Z, Q, R, C"),
        "0"   : (0,  "W, Z, Q, R, C"),
        "3/4" : (fractions.Fraction(3,4), "Q, R, C"),
        "√5"  : (math.sqrt(5), "Irasional, R, C"),
        "2+3i": (complex(2,3), "C only"),
        "-3/1": (-3, "Z, Q, R, C"),
    }
    print("\n  SOLUTION 1:")
    for name, (val, systems) in numbers.items():
        print(f"  {name:8} ∈ {systems}")

solution_1()

# ─────────────────────────────────────────────────────────────
# Exercise 2: Desimal Berulang ke Pecahan
# ─────────────────────────────────────────────────────────────
print("\n" + "-" * 40)
print("[Exercise 2] Ubah desimal berulang berikut menjadi pecahan:")
print("  a) 0.666...")
print("  b) 0.272727...")
print("  c) 0.583333...")
print("  Hint: Jika x = 0.aaa..., maka 10x - x = a, sehingga x = a/9")

def solution_2():
    print("\n  SOLUTION 2:")
    # a) x = 0.666... → 10x = 6.666... → 9x = 6 → x = 6/9 = 2/3
    a = fractions.Fraction(6, 9)
    print(f"  a) 0.666... = {a} = {float(a):.6f}")
    
    # b) x = 0.272727... → 100x = 27.272727... → 99x = 27 → x = 27/99 = 3/11
    b = fractions.Fraction(27, 99)
    print(f"  b) 0.272727... = {b} = {float(b):.6f}")
    
    # c) x = 0.5833... → non-repeating part 5, repeating 3
    # 10x = 5.833... → 100x = 58.333... → 90x = 53 → x = 53/90
    c = fractions.Fraction(53, 90)
    print(f"  c) 0.58333... = {c} = {float(c):.6f}")

solution_2()

# ─────────────────────────────────────────────────────────────
# Exercise 3: Operasi Bilangan Kompleks
# ─────────────────────────────────────────────────────────────
print("\n" + "-" * 40)
print("[Exercise 3] Hitung operasi bilangan kompleks berikut:")
print("  z1 = 4 + 3i,  z2 = 2 - i")
print("  a) z1 + z2")
print("  b) z1 × z2")
print("  c) |z1|")
print("  d) z1 / z2  (dalam bentuk a + bi)")

def solution_3():
    z1 = complex(4, 3)
    z2 = complex(2, -1)
    print("\n  SOLUTION 3:")
    print(f"  a) z1 + z2 = {z1 + z2}")
    print(f"  b) z1 × z2 = {z1 * z2}")
    print(f"  c) |z1|   = {abs(z1)}")
    div = z1 / z2
    print(f"  d) z1/z2  = {div.real:.4f} + {div.imag:.4f}i")

solution_3()

# ─────────────────────────────────────────────────────────────
# Exercise 4: Keanggotaan Interval
# ─────────────────────────────────────────────────────────────
print("\n" + "-" * 40)
print("[Exercise 4] Tentukan apakah x = 4 ada di interval berikut:")
print("  a) [2, 4]   b) (2, 4)   c) [4, 7)   d) (4, 7]")

def solution_4():
    x = 4
    print("\n  SOLUTION 4 (x = 4):")
    print(f"  a) [2, 4] : {2 <= x <= 4}  (ya, titik ujung tertutup)")
    print(f"  b) (2, 4) : {2 < x < 4}  (tidak, ujung terbuka)")
    print(f"  c) [4, 7) : {4 <= x < 7}  (ya, ujung kiri tertutup)")
    print(f"  d) (4, 7] : {4 < x <= 7}  (tidak, ujung kiri terbuka)")

solution_4()

# ─────────────────────────────────────────────────────────────
# Exercise 5: Floor dan Ceiling
# ─────────────────────────────────────────────────────────────
print("\n" + "-" * 40)
print("[Exercise 5] Hitung ⌊x⌋ dan ⌈x⌉ untuk:")
print("  a) x = 2.9   b) x = -1.2   c) x = 5.0   d) x = -3.0")

def solution_5():
    import math
    values = [2.9, -1.2, 5.0, -3.0]
    print("\n  SOLUTION 5:")
    for v in values:
        print(f"  x = {v:5.1f}: ⌊x⌋ = {math.floor(v):3d}, ⌈x⌉ = {math.ceil(v):3d}")

solution_5()

# ─────────────────────────────────────────────────────────────
# Exercise 6: Sifat Klosure
# ─────────────────────────────────────────────────────────────
print("\n" + "-" * 40)
print("[Exercise 6] Tunjukkan mana yang tertutup (TRUE/FALSE):")
print("  Gunakan contoh angka untuk membuktikan atau menyangkal.")
print("  a) N tertutup terhadap pengurangan")
print("  b) Z tertutup terhadap perkalian")
print("  c) Q tertutup terhadap pembagian")
print("  d) Irasional tertutup terhadap perkalian")

def solution_6():
    print("\n  SOLUTION 6:")
    # a) N: 2 - 5 = -3, bukan N → FALSE
    print(f"  a) N tertutup -? FALSE (contoh: 2 - 5 = {2-5}, bukan asli)")
    # b) Z: a*b selalu bulat → TRUE
    print(f"  b) Z tertutup ×? TRUE  (bulat × bulat = bulat selalu)")
    # c) Q: p/q ÷ r/s = ps/qr, asal pembagi ≠ 0 → TRUE
    print(f"  c) Q tertutup ÷? TRUE  (asal pembagi ≠ 0)")
    # d) Irasional: √2 × √2 = 2 (rasional!) → FALSE
    val = math.sqrt(2) * math.sqrt(2)
    print(f"  d) Irasional ×? FALSE (√2 × √2 = {val} = 2, rasional!)")

solution_6()

print("\n[Selesai] Semua latihan diselesaikan!")
print("Lanjut ke: visualizations.py atau challenge.py")
