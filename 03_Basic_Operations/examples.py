"""
=============================================================================
examples.py — Operasi Dasar dan Sifat-Sifatnya / Basic Operations & Properties
=============================================================================
Modul ini mendemonstrasikan operasi aritmatika dasar beserta sifat-sifatnya
secara komputasional menggunakan Python.

This module demonstrates basic arithmetic operations and their properties
computationally using Python.

Topik / Topics:
  1. Empat operasi dasar / Four basic operations
  2. Sifat-sifat operasi / Operation properties (assert-based proof)
  3. Urutan operasi / Order of operations
  4. Modulo dan pembagian bulat / Modulo and floor division
  5. Perpangkatan / Exponentiation
  6. Algoritma Euclidean (GCD dari nol) / Euclidean Algorithm (GCD from scratch)
  7. KPK / LCM
  8. Faktorisasi prima / Prime factorization
  9. Verifikasi aksioma field / Field axioms verification
  10. Pertimbangan presisi / Precision considerations
  11. Operasi bitwise / Bitwise operations

Penulis / Author: MathCode Project
=============================================================================
"""

import math
import sys
from fractions import Fraction  # untuk aritmatika presisi tepat / for exact arithmetic

# =============================================================================
# BAGIAN 1: EMPAT OPERASI DASAR / PART 1: FOUR BASIC OPERATIONS
# =============================================================================

print("=" * 70)
print("BAGIAN 1: EMPAT OPERASI DASAR / FOUR BASIC OPERATIONS")
print("=" * 70)

def demonstrate_basic_ops(a, b):
    """
    Demonstrasi empat operasi dasar dengan tipe data yang berbeda.
    Demonstrates four basic operations with different data types.
    """
    print(f"\nOperan / Operands: a = {a}, b = {b}")
    print(f"  Tipe a: {type(a).__name__}, Tipe b: {type(b).__name__}")
    print(f"  Penjumlahan / Addition:       {a} + {b} = {a + b}")
    print(f"  Pengurangan / Subtraction:    {a} - {b} = {a - b}")
    print(f"  Perkalian  / Multiplication:  {a} * {b} = {a * b}")

    # Pembagian — perlu hati-hati dengan tipe / Division — be careful with types
    if b != 0:
        print(f"  Pembagian  / Division:        {a} / {b} = {a / b}")
        print(f"  Pembagian bulat / Floor div:  {a} // {b} = {a // b}")
        print(f"  Modulo / Remainder:           {a} % {b} = {a % b}")
    else:
        print("  Pembagian: TIDAK TERDEFINISI (b = 0) / Division: UNDEFINED")

# Uji dengan berbagai tipe / Test with various types
demonstrate_basic_ops(17, 5)       # integers
demonstrate_basic_ops(3.14, 2.0)   # floats
demonstrate_basic_ops(-7, 3)       # negative integers

# Demonstrasi pembagian dengan nol / Demonstrate division by zero
print("\n--- Pembagian dengan Nol / Division by Zero ---")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"  10 / 0  → ZeroDivisionError: {e}")

try:
    result = 10 // 0
except ZeroDivisionError as e:
    print(f"  10 // 0 → ZeroDivisionError: {e}")

# Float division by zero menghasilkan inf / gives inf
import struct
# Menggunakan Fraction untuk melihat perilaku / using float('inf') directly
inf_result = float('inf')
print(f"  float('inf') = {inf_result}")
print(f"  Ini digunakan dalam konteks limit, bukan operasi nyata.")
print(f"  Used in limit context, not actual arithmetic.")


# =============================================================================
# BAGIAN 2: SIFAT-SIFAT OPERASI (DIBUKTIKAN DENGAN ASSERT)
# PART 2: OPERATION PROPERTIES (PROVEN WITH ASSERT)
# =============================================================================

print("\n" + "=" * 70)
print("BAGIAN 2: SIFAT-SIFAT OPERASI / OPERATION PROPERTIES")
print("=" * 70)

# Menggunakan Fraction untuk menghindari kesalahan floating-point
# Using Fraction to avoid floating-point errors
def test_properties(a_val, b_val, c_val):
    """
    Verifikasi semua sifat operasi menggunakan bilangan rasional tepat.
    Verifies all operation properties using exact rational numbers.

    Menggunakan fractions.Fraction untuk presisi sempurna.
    Uses fractions.Fraction for perfect precision.
    """
    a = Fraction(a_val)
    b = Fraction(b_val)
    c = Fraction(c_val)

    print(f"\nNilai uji / Test values: a={a}, b={b}, c={c}")

    # --- SIFAT PENJUMLAHAN / ADDITION PROPERTIES ---
    print("\n  [+] Sifat Penjumlahan / Addition Properties:")

    # Komutatif / Commutative
    assert a + b == b + a, "Komutatif penjumlahan gagal!"
    print(f"      Komutatif: {a}+{b} = {b}+{a} = {a+b}  ✓")

    # Asosiatif / Associative
    assert (a + b) + c == a + (b + c), "Asosiatif penjumlahan gagal!"
    print(f"      Asosiatif: ({a}+{b})+{c} = {a}+({b}+{c}) = {(a+b)+c}  ✓")

    # Identitas / Identity
    zero = Fraction(0)
    assert a + zero == a, "Identitas penjumlahan gagal!"
    print(f"      Identitas: {a} + 0 = {a}  ✓")

    # Invers / Inverse
    assert a + (-a) == zero, "Invers penjumlahan gagal!"
    print(f"      Invers: {a} + ({-a}) = {a+(-a)}  ✓")

    # --- SIFAT PERKALIAN / MULTIPLICATION PROPERTIES ---
    print("\n  [*] Sifat Perkalian / Multiplication Properties:")

    # Komutatif / Commutative
    assert a * b == b * a, "Komutatif perkalian gagal!"
    print(f"      Komutatif: {a}*{b} = {b}*{a} = {a*b}  ✓")

    # Asosiatif / Associative
    assert (a * b) * c == a * (b * c), "Asosiatif perkalian gagal!"
    print(f"      Asosiatif: ({a}*{b})*{c} = {a}*({b}*{c}) = {(a*b)*c}  ✓")

    # Identitas / Identity
    one = Fraction(1)
    assert a * one == a, "Identitas perkalian gagal!"
    print(f"      Identitas: {a} * 1 = {a}  ✓")

    # Invers multiplikatif / Multiplicative inverse (only if a != 0)
    if a != 0:
        assert a * Fraction(1, a) == one, "Invers perkalian gagal!"
        print(f"      Invers: {a} * (1/{a}) = {a * Fraction(1,a)}  ✓")

    # Properti nol / Zero property
    assert a * zero == zero, "Properti nol gagal!"
    print(f"      Properti nol: {a} * 0 = {a*zero}  ✓")

    # --- SIFAT DISTRIBUTIF / DISTRIBUTIVE PROPERTY ---
    print("\n  [D] Sifat Distributif / Distributive Property:")

    # a * (b + c) = a*b + a*c
    left_side  = a * (b + c)
    right_side = (a * b) + (a * c)
    assert left_side == right_side, "Distributif gagal!"
    print(f"      {a} * ({b}+{c}) = {a}*{b} + {a}*{c}")
    print(f"      {a} * {b+c}   = {a*b} + {a*c}")
    print(f"      {left_side} = {right_side}  ✓")

    # --- PENGURANGAN TIDAK KOMUTATIF / SUBTRACTION NOT COMMUTATIVE ---
    print("\n  [-] Pengurangan Tidak Komutatif / Subtraction Not Commutative:")
    if a != b:
        sub_ab = a - b
        sub_ba = b - a
        print(f"      {a} - {b} = {sub_ab}")
        print(f"      {b} - {a} = {sub_ba}")
        print(f"      {sub_ab} ≠ {sub_ba}  (tidak komutatif / not commutative) ✓")
    else:
        print(f"      a = b = {a}, pengecualian / exception case")

    print("\n  Semua sifat terverifikasi! / All properties verified!")

# Uji dengan berbagai nilai / Test with various values
test_properties(3, 5, 7)
test_properties('1/2', '3/4', '2/3')  # pecahan / fractions (as strings for Fraction)
test_properties(-4, 7, -2)


# =============================================================================
# BAGIAN 3: URUTAN OPERASI / PART 3: ORDER OF OPERATIONS
# =============================================================================

print("\n" + "=" * 70)
print("BAGIAN 3: URUTAN OPERASI / ORDER OF OPERATIONS (PEMDAS/BODMAS)")
print("=" * 70)

def explain_order_of_operations():
    """
    Demonstrasi urutan operasi langkah demi langkah.
    Step-by-step demonstration of order of operations.
    """

    # Ekspresi: 2 + 3 * 4 ** 2 - (6 / 2)
    # ID: Kita evaluasi langkah demi langkah
    # EN: We evaluate step by step
    expr_str = "2 + 3 * 4 ** 2 - (6 / 2)"
    print(f"\nEkspresi / Expression: {expr_str}")
    print("Langkah evaluasi / Evaluation steps:")
    print("  1. Kurung / Parentheses: (6 / 2) = 3.0")
    print("     → 2 + 3 * 4 ** 2 - 3.0")
    print("  2. Eksponen / Exponents: 4 ** 2 = 16")
    print("     → 2 + 3 * 16 - 3.0")
    print("  3. Perkalian / Multiplication: 3 * 16 = 48")
    print("     → 2 + 48 - 3.0")
    print("  4. Kiri ke kanan / Left to right: 2 + 48 = 50, then 50 - 3.0 = 47.0")
    result = eval(expr_str)
    print(f"  Hasil Python / Python result: {result}")
    assert result == 47.0, f"Hasil tidak cocok: {result}"
    print(f"  Verifikasi: 47.0 ✓")

    # Contoh jebakan urutan / Tricky order example
    print(f"\nContoh jebakan / Tricky example:")
    print("  2 ** 3 ** 2  →  Python evaluasi kanan ke kiri untuk ** !")
    print("               →  (Right-to-left for **!)")
    result2 = 2 ** 3 ** 2
    print(f"  2 ** 3 ** 2 = 2 ** (3 ** 2) = 2 ** 9 = {result2}")
    result3 = (2 ** 3) ** 2
    print(f"  (2 ** 3) ** 2 = 8 ** 2 = {result3}")
    print(f"  {result2} ≠ {result3}  (urutan evaluasi penting! / evaluation order matters!)")

    # Unary minus / unary plus
    print(f"\nUnary Operators:")
    x = 5
    print(f"  -(-{x}) = {-(-x)}  (double negative = positive)")
    print(f"  -(3 + 4) = {-(3+4)}  (unary minus distributes)")

explain_order_of_operations()


# =============================================================================
# BAGIAN 4: MODULO DAN PEMBAGIAN BULAT
# PART 4: MODULO AND FLOOR DIVISION
# =============================================================================

print("\n" + "=" * 70)
print("BAGIAN 4: MODULO DAN PEMBAGIAN BULAT / MODULO AND FLOOR DIVISION")
print("=" * 70)

def demonstrate_modulo():
    """
    Demonstrasi modulo dengan berbagai skenario.
    Demonstrates modulo with various scenarios.
    """
    print("\nHubungan dasar / Fundamental relation: a = b * (a // b) + (a % b)")
    print()

    test_cases = [(17, 5), (23, 7), (-7, 3), (7, -3), (-7, -3)]
    for a, b in test_cases:
        q = a // b   # hasil bagi bulat / floor quotient
        r = a % b    # sisa / remainder
        verify = b * q + r
        # Verifikasi hubungan dasar / Verify fundamental relation
        assert verify == a, f"Relasi gagal untuk ({a}, {b})"
        print(f"  {a:4d} = {b:3d} × {q:3d} + {r:2d}   "
              f"[{a}//({b})={q}, {a}%({b})={r}]  ✓")

    print("\nAritmatika Jam / Clock Arithmetic:")
    print("  Hari kerja dalam seminggu (mod 7) / Day of week (mod 7):")
    days = ['Senin/Mon', 'Selasa/Tue', 'Rabu/Wed', 'Kamis/Thu',
            'Jumat/Fri', 'Sabtu/Sat', 'Minggu/Sun']
    start_day = 0  # Senin = 0 / Monday = 0
    for days_ahead in [1, 7, 8, 14, 365]:
        day_idx = (start_day + days_ahead) % 7
        print(f"    Senin + {days_ahead:3d} hari = {days[day_idx]}")

    print("\nModulo dalam Kriptografi / Modulo in Cryptography:")
    # Caesar cipher contoh / Caesar cipher example
    message = "HELLO"
    shift = 3
    encrypted = ""
    for char in message:
        # Geser alfabet dengan wrap menggunakan modulo
        # Shift alphabet with wrap using modulo
        shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
        encrypted += chr(shifted)
    print(f"  Caesar Cipher: '{message}' dengan shift {shift} → '{encrypted}'")

    print("\nSifat Modulo / Modulo Properties:")
    a, b, n = 17, 8, 5
    print(f"  a={a}, b={b}, n={n}")
    print(f"  (a+b) mod n = {(a+b) % n}")
    print(f"  ((a mod n) + (b mod n)) mod n = {((a%n) + (b%n)) % n}")
    assert (a+b) % n == ((a%n) + (b%n)) % n
    print(f"  Sifat penjumlahan modulo terbukti! / Addition property proven! ✓")

demonstrate_modulo()


# =============================================================================
# BAGIAN 5: PERPANGKATAN / PART 5: EXPONENTIATION
# =============================================================================

print("\n" + "=" * 70)
print("BAGIAN 5: PERPANGKATAN / EXPONENTIATION")
print("=" * 70)

def demonstrate_exponentiation():
    """
    Mendemonstrasikan hukum-hukum perpangkatan.
    Demonstrates laws of exponentiation.
    """
    print("\nHukum Perpangkatan / Laws of Exponentiation:")

    # Hukum 1: a^m * a^n = a^(m+n)
    a, m, n = 2, 3, 4
    lhs = a**m * a**n
    rhs = a**(m+n)
    assert lhs == rhs
    print(f"\n  Hukum 1: a^m × a^n = a^(m+n)")
    print(f"    {a}^{m} × {a}^{n} = {a**m} × {a**n} = {lhs}")
    print(f"    {a}^({m}+{n}) = {a}^{m+n} = {rhs}  ✓")

    # Hukum 2: (a^m)^n = a^(m*n)
    a, m, n = 3, 2, 4
    lhs = (a**m)**n
    rhs = a**(m*n)
    assert lhs == rhs
    print(f"\n  Hukum 2: (a^m)^n = a^(m×n)")
    print(f"    ({a}^{m})^{n} = {a**m}^{n} = {lhs}")
    print(f"    {a}^({m}×{n}) = {a}^{m*n} = {rhs}  ✓")

    # Hukum 3: a^0 = 1
    for base in [2, 5, 100, -7, 0.5]:
        assert base**0 == 1
    print(f"\n  Hukum 3: a^0 = 1 (untuk a ≠ 0 / for a ≠ 0)")
    print(f"    2^0={2**0}, 5^0={5**0}, 100^0={100**0}, (-7)^0={(-7)**0}  ✓")

    # Hukum 4: a^(-n) = 1/a^n
    a, n = 2, 3
    neg_exp = a**(-n)
    recip = 1 / a**n
    assert abs(neg_exp - recip) < 1e-10
    print(f"\n  Hukum 4: a^(-n) = 1/a^n")
    print(f"    {a}^(-{n}) = {neg_exp} = 1/{a**n} = {recip}  ✓")

    # Hukum 5: a^(1/n) = n-th root
    print(f"\n  Hukum 5: a^(1/n) = ⁿ√a (akar ke-n / n-th root)")
    for a, n in [(4, 2), (8, 3), (16, 4), (32, 5)]:
        root = a ** (1/n)
        print(f"    {a}^(1/{n}) = {root:.6f}  (verifikasi: {root:.6f}^{n} = {root**n:.6f})")

    # Hukum 6: a^(m/n) = (n-th root of a)^m
    a, m, n = 8, 2, 3
    frac_exp = a ** (m/n)
    root_then_power = (a ** (1/n)) ** m
    print(f"\n  Hukum 6: a^(m/n) = (ⁿ√a)^m")
    print(f"    {a}^({m}/{n}) = {frac_exp:.6f}")
    print(f"    (∛{a})^{m} = {root_then_power:.6f}")
    assert abs(frac_exp - root_then_power) < 1e-10
    print(f"    Terbukti! / Proven! ✓")

    # Pertumbuhan Eksponensial / Exponential Growth
    print(f"\nPertumbuhan Eksponensial / Exponential Growth:")
    print(f"  n  |  2^n  |  3^n  |  10^n")
    print(f"  " + "-"*35)
    for n in range(1, 11):
        print(f"  {n:2d} | {2**n:5d} | {3**n:5d} | {10**n:10d}")

demonstrate_exponentiation()


# =============================================================================
# BAGIAN 6: ALGORITMA EUCLIDEAN (IMPLEMENTASI DARI NOL)
# PART 6: EUCLIDEAN ALGORITHM (IMPLEMENTED FROM SCRATCH)
# =============================================================================

print("\n" + "=" * 70)
print("BAGIAN 6: FPB - ALGORITMA EUCLIDEAN / GCD - EUCLIDEAN ALGORITHM")
print("=" * 70)

def gcd_recursive(a: int, b: int) -> int:
    """
    FPB (Faktor Persekutuan Terbesar) menggunakan Algoritma Euclidean rekursif.
    GCD (Greatest Common Divisor) using recursive Euclidean Algorithm.

    Teorema / Theorem: GCD(a, b) = GCD(b, a mod b), dengan / with GCD(a, 0) = a

    Kompleksitas Waktu / Time Complexity: O(log(min(a, b)))

    Parameter / Parameters:
        a, b: bilangan bulat non-negatif / non-negative integers

    Mengembalikan / Returns: GCD(|a|, |b|)
    """
    # Tangani bilangan negatif / Handle negative numbers
    a, b = abs(a), abs(b)

    # Kasus dasar: GCD(a, 0) = a
    if b == 0:
        return a

    # Langkah rekursif: GCD(a, b) = GCD(b, a mod b)
    # Kita ganti (a, b) dengan (b, a mod b)
    # We replace (a, b) with (b, a mod b)
    return gcd_recursive(b, a % b)


def gcd_iterative(a: int, b: int) -> int:
    """
    FPB menggunakan Algoritma Euclidean iteratif (lebih efisien untuk Python).
    GCD using iterative Euclidean Algorithm (more efficient for Python).

    Python memiliki batas rekursi (default 1000).
    Python has a recursion limit (default 1000).
    """
    a, b = abs(a), abs(b)
    while b != 0:
        # Langkah kunci: ganti (a, b) dengan (b, a mod b)
        # Key step: replace (a, b) with (b, a mod b)
        a, b = b, a % b
        # Ketika b menjadi 0, a adalah GCD / When b becomes 0, a is the GCD
    return a


def gcd_with_steps(a: int, b: int) -> int:
    """
    FPB dengan menampilkan semua langkah.
    GCD showing all steps.
    """
    a, b = abs(a), abs(b)
    print(f"\n  Mencari GCD({a}, {b}) / Finding GCD({a}, {b}):")
    step = 0
    while b != 0:
        old_a, old_b = a, b
        remainder = a % b
        print(f"    Langkah {step+1}: GCD({old_a}, {old_b}) = GCD({old_b}, {old_a} mod {old_b}) = GCD({old_b}, {remainder})")
        a, b = b, remainder
        step += 1
    print(f"    GCD = {a}  (karena b = 0 / because b = 0)")
    return a


# Demonstrasi / Demonstration
print("\nContoh GCD dengan langkah / GCD examples with steps:")
gcd_with_steps(48, 18)
gcd_with_steps(252, 105)
gcd_with_steps(1071, 462)

# Verifikasi dengan math.gcd / Verify with math.gcd
print("\nVerifikasi terhadap math.gcd / Verification against math.gcd:")
test_pairs = [(48, 18), (252, 105), (0, 5), (100, 75), (17, 13), (1000000, 999999)]
for a, b in test_pairs:
    our_gcd = gcd_iterative(a, b)
    lib_gcd = math.gcd(a, b)
    status = "✓" if our_gcd == lib_gcd else "✗"
    print(f"  GCD({a:7d}, {b:7d}) = {our_gcd:6d}  [{status}]")


# =============================================================================
# BAGIAN 7: KPK / PART 7: LCM (LEAST COMMON MULTIPLE)
# =============================================================================

print("\n" + "=" * 70)
print("BAGIAN 7: KPK (KELIPATAN PERSEKUTUAN TERKECIL) / LCM")
print("=" * 70)

def lcm(a: int, b: int) -> int:
    """
    KPK (Kelipatan Persekutuan Terkecil) menggunakan hubungan dengan GCD.
    LCM (Least Common Multiple) using the relation with GCD.

    Rumus / Formula: LCM(a, b) = |a × b| / GCD(a, b)

    Mengapa? / Why?
    Setiap faktor prima muncul dalam LCM pada pangkat maksimumnya dari a atau b.
    Every prime factor appears in LCM at its maximum power from either a or b.
    Sedangkan dalam GCD, pada pangkat minimum.
    While in GCD, at the minimum power.
    Sehingga LCM(a,b) × GCD(a,b) = a × b
    Therefore LCM(a,b) × GCD(a,b) = a × b
    """
    if a == 0 or b == 0:
        return 0
    # Bagi dulu sebelum kali untuk menghindari overflow
    # Divide first before multiply to avoid overflow
    return abs(a) // gcd_iterative(a, b) * abs(b)


def lcm_multiple(*args: int) -> int:
    """
    KPK dari banyak bilangan / LCM of multiple numbers.
    LCM(a, b, c) = LCM(LCM(a, b), c)
    """
    from functools import reduce
    return reduce(lcm, args)


print("\nContoh KPK / LCM Examples:")
pairs = [(4, 6), (12, 8), (7, 13), (100, 75), (21, 14)]
for a, b in pairs:
    result = lcm(a, b)
    # Verifikasi: keduanya harus habis membagi LCM
    # Verify: both must divide LCM evenly
    assert result % a == 0 and result % b == 0, "LCM gagal!"
    print(f"  LCM({a:3d}, {b:3d}) = {result:6d}  "
          f"(GCD={gcd_iterative(a,b)}, a×b={a*b}, LCM×GCD={result*gcd_iterative(a,b)})")

print(f"\nKPK dari banyak bilangan / LCM of multiple numbers:")
print(f"  LCM(2, 3, 4, 5) = {lcm_multiple(2, 3, 4, 5)}")
print(f"  LCM(4, 6, 10) = {lcm_multiple(4, 6, 10)}")

# Aplikasi KPK: Pecahan senama / Application: Common denominators
print(f"\nAplikasi / Application — Penjumlahan pecahan / Fraction addition:")
num1, den1 = 1, 4   # 1/4
num2, den2 = 1, 6   # 1/6
common_denom = lcm(den1, den2)
new_num1 = num1 * (common_denom // den1)
new_num2 = num2 * (common_denom // den2)
sum_num = new_num1 + new_num2
g = gcd_iterative(sum_num, common_denom)
print(f"  1/4 + 1/6 = {new_num1}/{common_denom} + {new_num2}/{common_denom} = {sum_num}/{common_denom} = {sum_num//g}/{common_denom//g}")
print(f"  Verifikasi: {Fraction(1,4) + Fraction(1,6)} ✓")


# =============================================================================
# BAGIAN 8: FAKTORISASI PRIMA / PART 8: PRIME FACTORIZATION
# =============================================================================

print("\n" + "=" * 70)
print("BAGIAN 8: FAKTORISASI PRIMA / PRIME FACTORIZATION")
print("=" * 70)

def prime_factorization(n: int) -> dict:
    """
    Faktorisasi prima suatu bilangan.
    Prime factorization of a number.

    Algoritma / Algorithm:
    1. Coba membagi dengan 2 / Try dividing by 2
    2. Coba membagi dengan bilangan ganjil dari 3 ke sqrt(n) / Try odd numbers from 3 to sqrt(n)
    3. Jika n > 1 tersisa, n sendiri adalah prima / If n > 1 remains, n itself is prime

    Mengapa sqrt(n)? / Why sqrt(n)?
    Jika n = a × b dan a ≤ b, maka a ≤ sqrt(n).
    If n = a × b and a ≤ b, then a ≤ sqrt(n).
    Jadi kita hanya perlu memeriksa hingga sqrt(n).
    So we only need to check up to sqrt(n).

    Mengembalikan / Returns: dict {faktor_prima: pangkat} / {prime_factor: exponent}

    Kompleksitas / Complexity: O(sqrt(n))
    """
    if n < 2:
        raise ValueError(f"Faktorisasi prima hanya untuk n ≥ 2, bukan {n}")

    factors = {}

    # Tangani faktor 2 secara terpisah / Handle factor 2 separately
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2

    # Coba faktor ganjil dari 3 / Try odd factors from 3
    # Langkah 2 mengoptimalkan: lewati bilangan genap / Step 2 optimizes: skip even numbers
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors[factor] = factors.get(factor, 0) + 1
            n //= factor
        factor += 2  # hanya bilangan ganjil / only odd numbers

    # Jika n > 1, maka n adalah faktor prima / If n > 1, then n is a prime factor
    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    return factors


def format_factorization(n: int, factors: dict) -> str:
    """Format hasil faktorisasi / Format factorization result."""
    parts = []
    for prime, exp in sorted(factors.items()):
        if exp == 1:
            parts.append(str(prime))
        else:
            parts.append(f"{prime}^{exp}")
    return f"{n} = " + " × ".join(parts)


print("\nFaktorisasi Prima / Prime Factorization:")
numbers = [12, 60, 100, 360, 1000, 9999, 83, 1024]
for n in numbers:
    factors = prime_factorization(n)
    print(f"  {format_factorization(n, factors)}")

    # Verifikasi: kalikan balik semua faktor / Verify: multiply back all factors
    product = 1
    for prime, exp in factors.items():
        product *= prime ** exp
    assert product == n, f"Faktorisasi gagal untuk {n}!"

print("\nMenggunakan faktorisasi untuk GCD dan LCM / Using factorization for GCD and LCM:")
a, b = 360, 252
fa = prime_factorization(a)
fb = prime_factorization(b)
print(f"  {format_factorization(a, fa)}")
print(f"  {format_factorization(b, fb)}")

# GCD = ambil pangkat minimum dari setiap faktor bersama
# GCD = take minimum exponent of each common factor
all_primes = set(fa.keys()) | set(fb.keys())
gcd_factors = {p: min(fa.get(p, 0), fb.get(p, 0)) for p in all_primes if min(fa.get(p,0), fb.get(p,0)) > 0}
lcm_factors = {p: max(fa.get(p, 0), fb.get(p, 0)) for p in all_primes}

gcd_val = 1
for p, e in gcd_factors.items():
    gcd_val *= p**e

lcm_val = 1
for p, e in lcm_factors.items():
    lcm_val *= p**e

print(f"  GCD: faktor bersama pangkat minimum / common factors minimum power = {gcd_val}")
print(f"  LCM: semua faktor pangkat maksimum / all factors maximum power = {lcm_val}")
print(f"  Verifikasi GCD: {gcd_iterative(a, b)} ✓" if gcd_val == gcd_iterative(a, b) else "  ✗ GCD salah!")
print(f"  Verifikasi LCM: {lcm(a, b)} ✓" if lcm_val == lcm(a, b) else "  ✗ LCM salah!")


# =============================================================================
# BAGIAN 9: VERIFIKASI AKSIOMA FIELD
# PART 9: FIELD AXIOMS VERIFICATION
# =============================================================================

print("\n" + "=" * 70)
print("BAGIAN 9: VERIFIKASI AKSIOMA FIELD / FIELD AXIOMS VERIFICATION")
print("=" * 70)

def verify_field_axioms(elements: list, verbose: bool = True) -> bool:
    """
    Verifikasi aksioma field untuk himpunan bilangan rasional.
    Verifies field axioms for a set of rational numbers.

    ID: Aksioma field adalah fondasi formal aljabar.
    EN: Field axioms are the formal foundation of algebra.
    """
    # Konversi ke Fraction untuk presisi tepat / Convert to Fraction for exact precision
    F = [Fraction(x) for x in elements]
    zero = Fraction(0)
    one = Fraction(1)

    if verbose:
        print(f"\n  Himpunan / Set F = {elements}")
        print(f"  Memeriksa aksioma untuk semua elemen / Checking axioms for all elements:")

    all_pass = True

    for a in F:
        for b in F:
            # A1: Penutupan Penjumlahan / Additive Closure
            assert isinstance(a + b, Fraction)

            # A2: Komutatif Penjumlahan / Additive Commutativity
            assert a + b == b + a, f"A2 gagal: {a}+{b}≠{b}+{a}"

            # A4: Identitas Penjumlahan / Additive Identity
            assert a + zero == a, f"A4 gagal: {a}+0≠{a}"

            # A5: Invers Penjumlahan / Additive Inverse
            assert a + (-a) == zero, f"A5 gagal: {a}+({-a})≠0"

            # M1: Penutupan Perkalian / Multiplicative Closure
            assert isinstance(a * b, Fraction)

            # M2: Komutatif Perkalian / Multiplicative Commutativity
            assert a * b == b * a, f"M2 gagal: {a}*{b}≠{b}*{a}"

            # M4: Identitas Perkalian / Multiplicative Identity
            assert a * one == a, f"M4 gagal: {a}*1≠{a}"

            # M5: Invers Perkalian / Multiplicative Inverse (only if a != 0)
            if a != zero:
                inv_a = Fraction(1, 1) / a
                assert a * inv_a == one, f"M5 gagal: {a}*(1/{a})≠1"

            for c in F:
                # A3: Asosiatif Penjumlahan / Additive Associativity
                assert (a + b) + c == a + (b + c), f"A3 gagal"

                # M3: Asosiatif Perkalian / Multiplicative Associativity
                assert (a * b) * c == a * (b * c), f"M3 gagal"

                # D1: Distributif / Distributive
                assert a * (b + c) == a*b + a*c, f"D1 gagal"

    if verbose:
        print(f"  A1 (Penutupan +): ✓")
        print(f"  A2 (Komutatif +): ✓")
        print(f"  A3 (Asosiatif +): ✓")
        print(f"  A4 (Identitas +): ✓  (elemen identitas = 0)")
        print(f"  A5 (Invers +):    ✓")
        print(f"  M1 (Penutupan ×): ✓")
        print(f"  M2 (Komutatif ×): ✓")
        print(f"  M3 (Asosiatif ×): ✓")
        print(f"  M4 (Identitas ×): ✓  (elemen identitas = 1)")
        print(f"  M5 (Invers ×):    ✓  (untuk elemen ≠ 0)")
        print(f"  D1 (Distributif): ✓")
        print(f"  SEMUA AKSIOMA TERPENUHI — (ℚ, +, ×) adalah FIELD! ✓")

    return True

verify_field_axioms(['1/2', '3/4', '-1/3', '2', '-5', '1/7'])


# =============================================================================
# BAGIAN 10: PERTIMBANGAN PRESISI / PART 10: PRECISION CONSIDERATIONS
# =============================================================================

print("\n" + "=" * 70)
print("BAGIAN 10: PERTIMBANGAN PRESISI / PRECISION CONSIDERATIONS")
print("=" * 70)

print("\nMasalah presisi floating-point / Floating-point precision issues:")
print("  (Mengapa kita menggunakan Fraction untuk verifikasi sifat / Why we use Fraction for property verification)")

# Masalah floating-point klasik / Classic floating-point issue
print(f"\n  0.1 + 0.2 = {0.1 + 0.2}")
print(f"  0.1 + 0.2 == 0.3?  {0.1 + 0.2 == 0.3}  ← MENGEJUTKAN! / SURPRISING!")
print(f"  Representasi biner / Binary representation:")
print(f"    0.1 ≈ {0.1:.20f}")
print(f"    0.2 ≈ {0.2:.20f}")
print(f"    0.3 ≈ {0.3:.20f}")
print(f"  0.1 + 0.2 ≈ {0.1 + 0.2:.20f}")

print(f"\nSolusi / Solutions:")
print(f"  1. Gunakan Fraction: Fraction(1,10) + Fraction(2,10) = {Fraction(1,10) + Fraction(2,10)}")
print(f"  2. Bandingkan dengan toleransi / Compare with tolerance:")
eps = 1e-10
result = abs((0.1 + 0.2) - 0.3) < eps
print(f"     |0.1+0.2 - 0.3| < {eps}: {result}")
print(f"  3. Gunakan round(): round(0.1+0.2, 10) = {round(0.1+0.2, 10)}")

print(f"\nRepresentasi bilangan besar / Large number representation:")
print(f"  Python mendukung integer presisi arbitrer / Python supports arbitrary precision integers!")
big = 2 ** 1000
print(f"  2^1000 = {str(big)[:50]}... ({len(str(big))} digit)")
print(f"  Tidak ada overflow! / No overflow!")

print(f"\nEpsilon mesin / Machine epsilon (float64):")
eps_machine = sys.float_info.epsilon
print(f"  sys.float_info.epsilon = {eps_machine}")
print(f"  Ini adalah perbedaan terkecil yang dapat dibedakan dari 1.0")
print(f"  This is the smallest difference distinguishable from 1.0")
print(f"  1.0 + eps = {1.0 + eps_machine}")
print(f"  1.0 + eps/2 = {1.0 + eps_machine/2}  (tidak berubah! / unchanged!)")


# =============================================================================
# BAGIAN 11: OPERASI BITWISE / PART 11: BITWISE OPERATIONS
# =============================================================================

print("\n" + "=" * 70)
print("BAGIAN 11: OPERASI BITWISE / BITWISE OPERATIONS")
print("=" * 70)

print("\nOperasi bitwise adalah operasi matematika pada level bit / Bitwise ops are math at bit level:")
a, b = 12, 10  # 1100, 1010 dalam biner / in binary

print(f"\n  a = {a} = {a:08b}")
print(f"  b = {b} = {b:08b}")
print(f"\n  AND (keduanya 1 / both 1):      a & b  = {a & b:2d} = {(a&b):08b}")
print(f"  OR  (salah satu 1 / either 1):   a | b  = {a | b:2d} = {(a|b):08b}")
print(f"  XOR (berbeda / different):        a ^ b  = {a ^ b:2d} = {(a^b):08b}")
print(f"  NOT (komplemen / complement):    ~a     = {~a:3d} = {~a:08b}")
print(f"  Left shift:                       a << 1 = {a<<1:2d} = {(a<<1):08b}  (× 2)")
print(f"  Right shift:                      a >> 1 = {a>>1:2d} = {(a>>1):08b}  (÷ 2)")

print(f"\nOptimasi dengan bit / Bit-level optimizations:")
n = 17
print(f"  n = {n}")
print(f"  n & 1 = {n & 1}  → {'ganjil/odd' if n & 1 else 'genap/even'}")
print(f"  n << 1 = {n << 1}  → n × 2 = {n*2}")
print(f"  n >> 1 = {n >> 1}  → n ÷ 2 = {n//2} (integer)")
print(f"  n & (n-1) = {n & (n-1)}  → {'n bukan pangkat 2 / n is not power of 2' if n&(n-1) else 'n adalah pangkat 2 / n is power of 2'}")

print(f"\n--- SELESAI / DONE ---")
print(f"Semua contoh berhasil dijalankan! / All examples ran successfully!")
