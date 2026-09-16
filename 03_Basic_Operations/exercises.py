"""
=============================================================================
exercises.py — Latihan: Operasi Dasar / Exercises: Basic Operations
=============================================================================
Berisi 12 latihan dengan berbagai tingkat kesulitan, petunjuk, dan solusi.
Contains 12 exercises with varying difficulty levels, hints, and solutions.

Cara penggunaan / Usage:
  Coba selesaikan setiap latihan sebelum melihat solusi!
  Try to solve each exercise before looking at the solution!

  Jalankan file ini untuk melihat semua solusi:
  Run this file to see all solutions:
    python3 exercises.py

Tingkat kesulitan / Difficulty:
  [★☆☆] = Mudah / Easy
  [★★☆] = Sedang / Medium
  [★★★] = Sulit / Hard
=============================================================================
"""

from fractions import Fraction
import math

# ===========================================================================
# HELPER FUNCTIONS
# ===========================================================================

def check(problem_num: str, student_answer, correct_answer, tolerance=0):
    """
    Memeriksa jawaban dengan opsional toleransi untuk float.
    Checks answer with optional tolerance for floats.
    """
    if tolerance > 0:
        correct = abs(float(student_answer) - float(correct_answer)) <= tolerance
    else:
        correct = student_answer == correct_answer

    status = "✓ BENAR!" if correct else f"✗ SALAH (jawaban: {correct_answer})"
    print(f"  [{problem_num}] {status}")
    return correct

def section(title: str):
    print(f"\n{'='*65}")
    print(f"  {title}")
    print(f"{'='*65}")

def hint(text: str):
    print(f"  💡 PETUNJUK / HINT: {text}")

def solution_header(problem_num: str, title: str):
    print(f"\n--- Soal {problem_num}: {title} ---")


# ===========================================================================
# EXERCISE 1: Verifikasi Sifat Komutatif dan Asosiatif
#             Verify Commutative and Associative Properties    [★☆☆]
# ===========================================================================

section("SOAL 1 [★☆☆]: Verifikasi Sifat / Property Verification")

print("""
  PERTANYAAN / QUESTION:
  Untuk a = 15, b = 23, c = 7:
  (a) Apakah a + b == b + a? Hitung kedua sisi.
      Is a + b == b + a? Calculate both sides.
  (b) Apakah (a + b) + c == a + (b + c)? Hitung kedua sisi.
      Is (a + b) + c == a + (b + c)? Calculate both sides.
  (c) Apakah a - b == b - a? Mengapa ya/tidak?
      Is a - b == b - a? Why yes/no?
  (d) Apakah (a - b) - c == a - (b - c)? Mengapa ya/tidak?
      Is (a - b) - c == a - (b - c)? Why yes/no?
""")
hint("Sifat komutatif: a ○ b = b ○ a. Pengurangan TIDAK komutatif.")

solution_header("1", "Verifikasi Sifat")
a, b, c = 15, 23, 7

print(f"  a={a}, b={b}, c={c}")

# (a) Komutatif penjumlahan / Additive commutativity
lhs_a = a + b
rhs_a = b + a
print(f"\n  (a) a+b = {lhs_a}, b+a = {rhs_a}")
print(f"      Sama? {lhs_a == rhs_a} → Penjumlahan KOMUTATIF ✓")
check("1a", lhs_a == rhs_a, True)

# (b) Asosiatif penjumlahan / Additive associativity
lhs_b = (a + b) + c
rhs_b = a + (b + c)
print(f"\n  (b) (a+b)+c = ({a}+{b})+{c} = {a+b}+{c} = {lhs_b}")
print(f"      a+(b+c) = {a}+({b}+{c}) = {a}+{b+c} = {rhs_b}")
print(f"      Sama? {lhs_b == rhs_b} → Penjumlahan ASOSIATIF ✓")
check("1b", lhs_b == rhs_b, True)

# (c) Komutatif pengurangan / Subtraction commutativity
lhs_c = a - b
rhs_c = b - a
print(f"\n  (c) a-b = {lhs_c}, b-a = {rhs_c}")
print(f"      Sama? {lhs_c == rhs_c} → Pengurangan TIDAK KOMUTATIF ✓")
check("1c", lhs_c == rhs_c, False)

# (d) Asosiatif pengurangan / Subtraction associativity
lhs_d = (a - b) - c
rhs_d = a - (b - c)
print(f"\n  (d) (a-b)-c = ({a}-{b})-{c} = {a-b}-{c} = {lhs_d}")
print(f"      a-(b-c) = {a}-({b}-{c}) = {a}-{b-c} = {rhs_d}")
print(f"      Sama? {lhs_d == rhs_d} → Pengurangan TIDAK ASOSIATIF ✓")
check("1d", lhs_d == rhs_d, False)


# ===========================================================================
# EXERCISE 2: Urutan Operasi / Order of Operations              [★☆☆]
# ===========================================================================

section("SOAL 2 [★☆☆]: Urutan Operasi / Order of Operations")

print("""
  PERTANYAAN / QUESTION:
  Hitung ekspresi berikut TANPA Python (tulis langkah-langkahnya):
  Calculate the following WITHOUT Python (write the steps):

  (a) 3 + 4 × 2
  (b) (3 + 4) × 2
  (c) 2 ** 3 + 1
  (d) 10 - 2 × 3 + 1
  (e) 2 ** 2 ** 3  (hati-hati! / careful!)
  (f) 100 / 10 / 2
""")
hint("Ingat PEMDAS: Kurung → Eksponen → Kali/Bagi → Tambah/Kurang")
hint("** adalah kanan-asosiatif / ** is right-associative")

solution_header("2", "Urutan Operasi")

problems = [
    ("3 + 4 × 2",     "3 + (4×2) = 3+8",          3 + 4*2,      "3+4*2"),
    ("(3+4) × 2",     "(3+4)×2 = 7×2",              (3+4)*2,      "(3+4)*2"),
    ("2^3 + 1",       "(2^3)+1 = 8+1",               2**3+1,       "2**3+1"),
    ("10-2×3+1",      "10-(2×3)+1 = 10-6+1",        10-2*3+1,     "10-2*3+1"),
    ("2^(2^3)",       "2^(2^3)=2^8 [kanan-asosiatif]",2**2**3,     "2**2**3"),
    ("100/10/2",      "(100/10)/2=10/2 [kiri-asosiatif]",100/10/2, "100/10/2"),
]

for expr_str, steps, answer, py_expr in problems:
    result = eval(py_expr)
    print(f"\n  {expr_str}")
    print(f"    Langkah: {steps} = {result}")
    check(f"2", result, answer)


# ===========================================================================
# EXERCISE 3: Masalah GCD / GCD Problems                        [★★☆]
# ===========================================================================

section("SOAL 3 [★★☆]: FPB / GCD Problems")

print("""
  PERTANYAAN / QUESTION:
  Hitung FPB menggunakan Algoritma Euclidean. Tunjukkan langkah-langkahnya!
  Calculate GCD using Euclidean Algorithm. Show the steps!

  (a) GCD(56, 98)
  (b) GCD(144, 89)   ← bilangan Fibonacci! / Fibonacci numbers! (kasus tersulit / hardest case)
  (c) GCD(1071, 462)
  (d) GCD(100, 75)

  BONUS: Mengapa GCD(Fn, Fn-1) membutuhkan banyak langkah?
         Why does GCD(Fn, Fn-1) require many steps?
""")
hint("GCD(a,b) = GCD(b, a mod b). Terus sampai b=0.")

def gcd_steps(a, b):
    """GCD dengan langkah / GCD with steps."""
    original = (a, b)
    steps = []
    while b:
        steps.append(f"GCD({a},{b})=GCD({b},{a%b})")
        a, b = b, a % b
    steps.append(f"GCD({a},0)={a}")
    return a, steps

solution_header("3", "FPB / GCD")

cases = [(56, 98), (144, 89), (1071, 462), (100, 75)]
for a, b in cases:
    result, steps = gcd_steps(a, b)
    print(f"\n  GCD({a}, {b}):")
    for step in steps:
        print(f"    {step}")
    print(f"    = {result}  ({len(steps)-1} langkah / steps)")
    check("3", result, math.gcd(a, b))

print(f"\n  BONUS: GCD(F_n, F_n-1) membutuhkan n langkah karena")
print(f"  setiap langkah mengurangi indeks Fibonacci satu demi satu.")
print(f"  Ini adalah kasus TERBURUK untuk Algoritma Euclidean!")
print(f"  Inilah yang membuat Lame membuktikan kompleksitas O(log min(a,b)).")


# ===========================================================================
# EXERCISE 4: Aritmatika Modular / Modular Arithmetic           [★★☆]
# ===========================================================================

section("SOAL 4 [★★☆]: Aritmatika Modular / Modular Arithmetic")

print("""
  PERTANYAAN / QUESTION:
  (a) Jika hari ini Senin, hari apa 100 hari lagi?
      If today is Monday, what day is it in 100 days?

  (b) Jam berapa 250 jam dari sekarang pukul 09:00?
      What time is it 250 hours from now at 09:00?

  (c) Hitung: (2024 × 365 + 100) mod 7
      [0=Sen/Mon, 1=Sel/Tue, 2=Rab/Wed, 3=Kam/Thu, 4=Jum/Fri, 5=Sab/Sat, 6=Min/Sun]

  (d) Apakah 1234567 habis dibagi 9?
      Is 1234567 divisible by 9?
      [Petunjuk: Bilangan habis dibagi 9 jika jumlah digitnya habis dibagi 9]
      [Hint: A number is divisible by 9 if its digit sum is divisible by 9]

  (e) Temukan x: 3x ≡ 1 (mod 7)   [invers multiplikatif / multiplicative inverse]
      Find x: 3x ≡ 1 (mod 7)
""")
hint("Gunakan mod untuk 'membungkus' nilai / Use mod to 'wrap' values")

solution_header("4", "Aritmatika Modular")

days = ['Senin/Mon', 'Selasa/Tue', 'Rabu/Wed', 'Kamis/Thu', 'Jumat/Fri', 'Sabtu/Sat', 'Minggu/Sun']

# (a)
days_ahead = 100
start = 0  # Senin / Monday
result_day = (start + days_ahead) % 7
print(f"\n  (a) 100 hari dari Senin: (0 + 100) mod 7 = {result_day} → {days[result_day]}")
check("4a", result_day, (0+100)%7)

# (b)
hours_ahead = 250
start_hour = 9
result_hour = (start_hour + hours_ahead) % 24
print(f"\n  (b) 250 jam dari pukul 09:00: (9 + 250) mod 24 = {result_hour}:00")
check("4b", result_hour, (9+250)%24)

# (c)
val_c = (2024 * 365 + 100) % 7
print(f"\n  (c) (2024×365+100) mod 7 = {2024*365+100} mod 7 = {val_c} → {days[val_c]}")
check("4c", val_c, (2024*365+100)%7)

# (d)
n = 1234567
digit_sum = sum(int(d) for d in str(n))
div_by_9 = digit_sum % 9 == 0
direct = n % 9 == 0
print(f"\n  (d) {n}: jumlah digit = {'+'.join(str(d) for d in str(n))} = {digit_sum}")
print(f"      {digit_sum} mod 9 = {digit_sum % 9} → {'Habis' if div_by_9 else 'Tidak habis'} dibagi 9")
print(f"      Verifikasi langsung: {n} mod 9 = {n%9}")
assert div_by_9 == direct
check("4d", div_by_9, False)

# (e) Cari invers 3 mod 7 dengan brute force
print(f"\n  (e) Cari x: 3x ≡ 1 (mod 7)")
for x in range(1, 7):
    if (3 * x) % 7 == 1:
        print(f"      x = {x}: 3×{x} = {3*x}, {3*x} mod 7 = {(3*x)%7} ✓")
        check("4e", x, 5)
        break


# ===========================================================================
# EXERCISE 5: Hukum Perpangkatan / Laws of Exponents             [★★☆]
# ===========================================================================

section("SOAL 5 [★★☆]: Hukum Perpangkatan / Laws of Exponents")

print("""
  PERTANYAAN / QUESTION:
  Sederhanakan ekspresi berikut (tunjukkan hukum yang digunakan):
  Simplify the following (show which law is used):

  (a) 2^5 × 2^3
  (b) (3^4)^2
  (c) 5^0 × 7^3
  (d) 4^(-2) × 4^5
  (e) (2 × 3)^4
  (f) (2/3)^3
  (g) 8^(2/3)
""")
hint("Gunakan hukum: a^m × a^n = a^(m+n), (a^m)^n = a^(mn), a^0 = 1, a^(-n) = 1/a^n")

solution_header("5", "Hukum Perpangkatan")

# (a) a^m * a^n = a^(m+n)
a5a = 2**5 * 2**3
print(f"\n  (a) 2^5 × 2^3 = 2^(5+3) = 2^8 = {a5a}")
check("5a", a5a, 256)

# (b) (a^m)^n = a^(mn)
a5b = (3**4)**2
print(f"  (b) (3^4)^2 = 3^(4×2) = 3^8 = {a5b}")
check("5b", a5b, 6561)

# (c) a^0 = 1
a5c = 5**0 * 7**3
print(f"  (c) 5^0 × 7^3 = 1 × 343 = {a5c}")
check("5c", a5c, 343)

# (d) a^m / a^n = a^(m-n)
a5d = 4**(-2) * 4**5
print(f"  (d) 4^(-2) × 4^5 = 4^(-2+5) = 4^3 = {4**3}  ({a5d})")
check("5d", round(a5d), 64)

# (e) (ab)^n = a^n × b^n
a5e = (2*3)**4
print(f"  (e) (2×3)^4 = 2^4 × 3^4 = {2**4} × {3**4} = {a5e}")
check("5e", a5e, 1296)

# (f) (a/b)^n = a^n/b^n
a5f = Fraction(2,3)**3
print(f"  (f) (2/3)^3 = 2^3/3^3 = 8/27 = {a5f}")
check("5f", a5f, Fraction(8,27))

# (g) a^(m/n) = (n-th root of a)^m
a5g = 8**(2/3)
print(f"  (g) 8^(2/3) = (∛8)^2 = 2^2 = 4  ({a5g:.6f})")
check("5g", round(a5g, 6), 4.0)


# ===========================================================================
# EXERCISE 6: Faktorisasi Prima / Prime Factorization            [★★☆]
# ===========================================================================

section("SOAL 6 [★★☆]: Faktorisasi Prima / Prime Factorization")

print("""
  PERTANYAAN / QUESTION:
  (a) Faktorisasikan bilangan berikut ke faktor prima:
      Factorize the following numbers into prime factors:
      i)  180    ii) 504    iii) 1800

  (b) Gunakan faktorisasi prima untuk menemukan GCD dan LCM dari:
      Use prime factorization to find GCD and LCM of:
      GCD(180, 504) dan LCM(180, 504)

  (c) Berapa banyak faktor (divisor) yang dimiliki 180?
      How many factors (divisors) does 180 have?
      [Petunjuk: Jika n = p1^a1 × p2^a2 × ..., maka jumlah faktor = (a1+1)(a2+1)...]
      [Hint: If n = p1^a1 × p2^a2 × ..., then # of factors = (a1+1)(a2+1)...]
""")

def prime_factorization(n):
    factors = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    f = 3
    while f * f <= n:
        while n % f == 0:
            factors[f] = factors.get(f, 0) + 1
            n //= f
        f += 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

solution_header("6", "Faktorisasi Prima")

# (a)
for n in [180, 504, 1800]:
    f = prime_factorization(n)
    fmt = ' × '.join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(f.items()))
    product = 1
    for p, e in f.items():
        product *= p**e
    assert product == n
    print(f"  {n} = {fmt}  ✓")

# (b)
n1, n2 = 180, 504
f1, f2 = prime_factorization(n1), prime_factorization(n2)
all_primes = set(f1.keys()) | set(f2.keys())

gcd_factors = {}
lcm_factors = {}
for p in all_primes:
    e1, e2 = f1.get(p, 0), f2.get(p, 0)
    if min(e1, e2) > 0:
        gcd_factors[p] = min(e1, e2)
    lcm_factors[p] = max(e1, e2)

gcd_val = 1
for p, e in gcd_factors.items():
    gcd_val *= p**e
lcm_val = 1
for p, e in lcm_factors.items():
    lcm_val *= p**e

gcd_fmt = ' × '.join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(gcd_factors.items()))
lcm_fmt = ' × '.join(f"{p}^{e}" if e > 1 else str(p) for p, e in sorted(lcm_factors.items()))

print(f"\n  GCD({n1},{n2}) = {gcd_fmt} = {gcd_val}  (pangkat minimum / min exponents)")
print(f"  LCM({n1},{n2}) = {lcm_fmt} = {lcm_val}  (pangkat maksimum / max exponents)")
check("6b-GCD", gcd_val, math.gcd(n1,n2))
check("6b-LCM", lcm_val, math.lcm(n1,n2))

# (c)
f180 = prime_factorization(180)
num_factors = 1
for e in f180.values():
    num_factors *= (e + 1)
print(f"\n  180 = {' × '.join(f'{p}^{e}' for p,e in sorted(f180.items()))}")
print(f"  Jumlah faktor = {' × '.join(f'({e}+1)' for e in f180.values())} = {num_factors}")
# Verifikasi / Verify
actual = sum(1 for i in range(1, 181) if 180 % i == 0)
assert num_factors == actual
check("6c", num_factors, 18)


# ===========================================================================
# EXERCISE 7: Masalah Kata / Word Problems                       [★★☆]
# ===========================================================================

section("SOAL 7 [★★☆]: Masalah Kata / Word Problems")

print("""
  PERTANYAAN / QUESTION:
  Terjemahkan ke operasi matematika dan selesaikan:
  Translate to math operations and solve:

  (a) Toko menjual 3 jenis produk: A seharga Rp15.000, B seharga Rp22.500,
      dan C seharga Rp8.750. Pelanggan membeli 4A, 2B, dan 5C.
      Total belanja? Kembalian dari Rp200.000?

  (b) Sebuah tangki berisi 5/8 penuh. Ditambah 1/4 tangki. Seberapa penuh sekarang?
      A tank is 5/8 full. 1/4 tank more is added. How full is it now?

  (c) Layar ponsel memiliki dimensi 6.1 × 2.8 inci. Berapa luas permukaannya?
      Berapa diagonal layarnya? (Gunakan Teorema Pythagoras)

  (d) Berapa bilangan bulat antara 1 dan 1000 yang habis dibagi 3 ATAU 5?
      How many integers between 1 and 1000 are divisible by 3 OR 5?
      (Gunakan Prinsip Inklusi-Eksklusi / Use Inclusion-Exclusion Principle)
""")

solution_header("7", "Masalah Kata")

# (a)
a_price, b_price, c_price = 15000, 22500, 8750
a_qty, b_qty, c_qty = 4, 2, 5
total = a_price*a_qty + b_price*b_qty + c_price*c_qty
paid = 200000
change = paid - total
print(f"\n  (a) Total = {a_price}×{a_qty} + {b_price}×{b_qty} + {c_price}×{c_qty}")
print(f"         = {a_price*a_qty:,} + {b_price*b_qty:,} + {c_price*c_qty:,}")
print(f"         = Rp {total:,}")
print(f"      Kembalian = Rp{paid:,} - Rp{total:,} = Rp{change:,}")
check("7a", total, 130000)

# (b)
tank1 = Fraction(5, 8)
tank2 = Fraction(1, 4)
tank_total = tank1 + tank2
print(f"\n  (b) 5/8 + 1/4 = {tank1} + {tank2} = {tank_total}")
print(f"      {'Penuh/Full' if tank_total >= 1 else f'{float(tank_total)*100:.1f}% penuh/full'}")
check("7b", tank_total, Fraction(7, 8))

# (c)
import math as m
w, h = 6.1, 2.8
area = w * h
diagonal = m.sqrt(w**2 + h**2)
print(f"\n  (c) Layar {w}\" × {h}\":")
print(f"      Luas = {w} × {h} = {area:.2f} in²")
print(f"      Diagonal = √({w}² + {h}²) = √({w**2:.2f} + {h**2:.2f}) = √{w**2+h**2:.2f} = {diagonal:.4f}\"")
check("7c", round(area, 2), round(6.1*2.8, 2))

# (d) Inklusi-Eksklusi / Inclusion-Exclusion
div3 = sum(1 for i in range(1, 1001) if i % 3 == 0)
div5 = sum(1 for i in range(1, 1001) if i % 5 == 0)
div15 = sum(1 for i in range(1, 1001) if i % 15 == 0)
div3_or_5 = div3 + div5 - div15  # Inklusi-Eksklusi
print(f"\n  (d) Bilangan habis dibagi 3: {div3}")
print(f"      Bilangan habis dibagi 5: {div5}")
print(f"      Bilangan habis dibagi 15 (keduanya): {div15}")
print(f"      Habis dibagi 3 ATAU 5 = {div3} + {div5} - {div15} = {div3_or_5}")
print(f"      (Prinsip Inklusi-Eksklusi: |A∪B| = |A| + |B| - |A∩B|)")
check("7d", div3_or_5, 467)


# ===========================================================================
# EXERCISE 8: Sifat Bilangan Negatif / Properties of Negatives   [★☆☆]
# ===========================================================================

section("SOAL 8 [★☆☆]: Sifat Bilangan Negatif / Properties of Negatives")

print("""
  PERTANYAAN / QUESTION:
  Tanpa Python, tentukan tanda hasilnya (+/-):
  Without Python, determine the sign of the result (+/-):

  (a) (-3) × (-5)
  (b) (-2)^5
  (c) (-1)^100
  (d) (-3) × 4 × (-2) × (-1)
  (e) |(-7) × 3 - (-4)|
""")
hint("(-) × (-) = (+), (-) × (+) = (-). Hitungan tanda terlebih dahulu!")

solution_header("8", "Sifat Bilangan Negatif")

cases8 = [
    ("(-3)×(-5)", (-3)*(-5), "(-)(-)=(+): hasilnya positif"),
    ("(-2)^5", (-2)**5, "(-2)^5 = (-)^(ganjil/odd) = (-)"),
    ("(-1)^100", (-1)**100, "(-1)^(genap/even) = (+)"),
    ("(-3)×4×(-2)×(-1)", (-3)*4*(-2)*(-1), "3 faktor negatif = negatif / 3 negative factors = negative"),
    ("|(-7)×3-(-4)|", abs((-7)*3-(-4)), "nilai mutlak selalu ≥ 0 / abs val always ≥ 0"),
]

for expr, result, explanation in cases8:
    sign = "+" if result > 0 else ("-" if result < 0 else "0")
    print(f"  {expr} = {result:5}  [{sign}] — {explanation}")


# ===========================================================================
# EXERCISE 9: Sifat Distributif / Distributive Property          [★★☆]
# ===========================================================================

section("SOAL 9 [★★☆]: Sifat Distributif / Distributive Property")

print("""
  PERTANYAAN / QUESTION:
  Gunakan sifat distributif untuk menyederhanakan perhitungan mental:
  Use the distributive property for mental calculation simplification:

  (a) 7 × 99 = 7 × (100 - 1) = ?
  (b) 13 × 102 = 13 × (100 + 2) = ?
  (c) 25 × 44 = 25 × (40 + 4) = ?
  (d) Buktikan: (a+b)^2 = a^2 + 2ab + b^2 dengan a=3, b=4
      Prove: (a+b)^2 = a^2 + 2ab + b^2 with a=3, b=4
  (e) Faktorkan menggunakan distributif: 15x + 25y = 5(?)
      Factor using distributive: 15x + 25y = 5(?)
""")

solution_header("9", "Sifat Distributif")

# (a)
r9a = 7 * (100-1)
print(f"  (a) 7×99 = 7×(100-1) = 7×100 - 7×1 = 700 - 7 = {r9a}")
check("9a", r9a, 7*99)

# (b)
r9b = 13 * (100+2)
print(f"  (b) 13×102 = 13×(100+2) = 1300 + 26 = {r9b}")
check("9b", r9b, 13*102)

# (c)
r9c = 25*(40+4)
print(f"  (c) 25×44 = 25×(40+4) = 1000 + 100 = {r9c}")
check("9c", r9c, 25*44)

# (d)
a9, b9 = 3, 4
lhs9d = (a9 + b9)**2
rhs9d = a9**2 + 2*a9*b9 + b9**2
print(f"  (d) a={a9}, b={b9}:")
print(f"      (a+b)^2 = ({a9+b9})^2 = {lhs9d}")
print(f"      a^2+2ab+b^2 = {a9**2}+2({a9})({b9})+{b9**2} = {a9**2}+{2*a9*b9}+{b9**2} = {rhs9d}")
check("9d", lhs9d == rhs9d, True)

# (e)
print(f"  (e) 15x + 25y = 5(3x + 5y)  [faktor bersama 5 / common factor 5]")
print(f"      Verifikasi: 5×3x=15x ✓, 5×5y=25y ✓")


# ===========================================================================
# EXERCISE 10: Properti Kesamaan dan Ketidaksamaan
#              Properties of Equality and Inequality              [★★☆]
# ===========================================================================

section("SOAL 10 [★★☆]: Kesamaan & Ketidaksamaan / Equality & Inequality")

print("""
  PERTANYAAN / QUESTION:
  (a) Jika 3x + 7 = 22, temukan x (tunjukkan setiap langkah operasi)
      If 3x + 7 = 22, find x (show each operation step)

  (b) Selesaikan: 2x - 5 > 11 (ingat, apakah tanda berubah? / does sign change?)
      Solve: 2x - 5 > 11

  (c) Selesaikan: -3x ≤ 15 (HATI-HATI dengan tanda perkalian negatif!)
      Solve: -3x ≤ 15 (CAREFUL with negative multiplication!)

  (d) Apakah sifat transitif berlaku? Jika a < b dan b < c, apakah a < c?
      Uji dengan: a=2, b=5, c=8
      Does transitivity hold? If a < b and b < c, is a < c?
      Test with: a=2, b=5, c=8
""")
hint("Operasi ke dua sisi kesamaan tidak mengubah kesetaraan. Perkalian dengan negatif MEMBALIK tanda ketidaksamaan!")

solution_header("10", "Kesamaan & Ketidaksamaan")

# (a)
print(f"\n  (a) 3x + 7 = 22")
print(f"      -7 dari kedua sisi / subtract 7 from both sides:")
print(f"      3x = 22 - 7 = 15")
print(f"      Bagi dengan 3 / divide both sides by 3:")
print(f"      x = 15 / 3 = {15//3}")
x_10a = 5
assert 3*x_10a + 7 == 22
check("10a", x_10a, 5)

# (b)
print(f"\n  (b) 2x - 5 > 11")
print(f"      +5 ke kedua sisi / add 5 to both sides:")
print(f"      2x > 16")
print(f"      Bagi dengan 2 (positif, tanda tetap / positive, sign stays):")
print(f"      x > 8")
check("10b", 9 > 8, True)  # test x=9

# (c)
print(f"\n  (c) -3x ≤ 15")
print(f"      Bagi dengan -3 (NEGATIF → BALIK TANDA! / NEGATIVE → FLIP SIGN!):")
print(f"      x ≥ -5  [tanda ≤ berubah menjadi ≥ / ≤ becomes ≥]")
# Verifikasi
assert -3 * (-5) <= 15    # x = -5: batas / boundary
assert -3 * (-4) <= 15    # x = -4 > -5: harus berlaku / must hold
assert not (-3 * (-6) <= 15)  # x = -6 < -5: tidak berlaku / should not hold
print(f"      Verifikasi x=-5: -3×(-5)={-3*(-5)} ≤ 15 ✓")
print(f"      Verifikasi x=-4: -3×(-4)={-3*(-4)} ≤ 15 ✓")
print(f"      Verifikasi x=-6: -3×(-6)={-3*(-6)} ≤ 15? {-3*(-6) <= 15} ✓ (tidak berlaku)")
check("10c", True, True)

# (d)
a10, b10, c10 = 2, 5, 8
trans = a10 < b10 < c10
print(f"\n  (d) a={a10} < b={b10} dan b={b10} < c={c10}")
print(f"      Maka a={a10} < c={c10}? {a10 < c10} ✓")
print(f"      Sifat TRANSITIF terpenuhi / Transitivity HOLDS")
check("10d", trans, True)


# ===========================================================================
# EXERCISE 11: Nilai Mutlak / Absolute Value                      [★★☆]
# ===========================================================================

section("SOAL 11 [★★☆]: Nilai Mutlak / Absolute Value")

print("""
  PERTANYAAN / QUESTION:
  (a) Hitung: |3 - 7| + |-4 × 5| - |2 - 2|
  (b) Selesaikan: |x - 3| = 5
  (c) Selesaikan: |2x + 1| ≤ 7
  (d) Apakah ketidaksamaan segitiga berlaku?
      |a + b| ≤ |a| + |b|
      Uji dengan a=3, b=-7 dan a=-4, b=-3
""")

solution_header("11", "Nilai Mutlak")

# (a)
r11a = abs(3-7) + abs(-4*5) - abs(2-2)
print(f"  (a) |3-7| + |-4×5| - |2-2|")
print(f"      = |-4| + |-20| - |0|")
print(f"      = 4 + 20 - 0 = {r11a}")
check("11a", r11a, 24)

# (b) |x-3| = 5 → x-3=5 atau x-3=-5
x1 = 3 + 5  # = 8
x2 = 3 - 5  # = -2
print(f"\n  (b) |x-3| = 5")
print(f"      x-3 = 5  → x = {x1}")
print(f"      x-3 = -5 → x = {x2}")
assert abs(x1-3) == 5 and abs(x2-3) == 5
check("11b", True, True)

# (c) |2x+1| ≤ 7 → -7 ≤ 2x+1 ≤ 7 → -8 ≤ 2x ≤ 6 → -4 ≤ x ≤ 3
print(f"\n  (c) |2x+1| ≤ 7")
print(f"      -7 ≤ 2x+1 ≤ 7")
print(f"      -8 ≤ 2x ≤ 6")
print(f"      -4 ≤ x ≤ 3")
# Verifikasi
for x_test in [-4, 0, 3]:
    assert abs(2*x_test+1) <= 7, f"x={x_test} gagal!"
assert abs(2*(-5)+1) > 7  # luar batas / outside
print(f"      Verifikasi: x=-4,0,3 semuanya memenuhi ✓")
check("11c", True, True)

# (d) Ketidaksamaan segitiga / Triangle inequality
for a_test, b_test in [(3, -7), (-4, -3), (5, 5)]:
    lhs = abs(a_test + b_test)
    rhs = abs(a_test) + abs(b_test)
    holds = lhs <= rhs
    print(f"\n  (d) a={a_test:2d}, b={b_test:2d}: |{a_test}+{b_test}| = {lhs} ≤ |{a_test}|+|{b_test}| = {rhs}? {holds} ✓")
    check("11d", holds, True)


# ===========================================================================
# EXERCISE 12: Tantangan Integrasi / Integration Challenge        [★★★]
# ===========================================================================

section("SOAL 12 [★★★]: Tantangan Integrasi / Integration Challenge")

print("""
  PERTANYAAN / QUESTION:
  Hubungkan semua konsep / Connect all concepts:

  (a) KRIPTOGRAFI SEDERHANA: Caesar Cipher
      Enkripsi "MATH" dengan kunci k=13 (ROT-13)
      Kemudian dekripsi kembali. Mengapa dekripsi ROT-13 sama dengan enkripsi?

  (b) BILANGAN SEMPURNA: Bilangan sempurna adalah bilangan yang sama dengan
      jumlah faktor-faktor sejatinya (termasuk 1 tetapi bukan bilangan itu sendiri).
      Temukan bilangan sempurna di antara 1 dan 1000.
      Perfect number = equals sum of its proper divisors.
      Find all perfect numbers between 1 and 1000.

  (c) MODULAR EXPONENTIATION:
      Hitung 3^100 mod 7 menggunakan sifat modulo dan perpangkatan.
      Calculate 3^100 mod 7 using properties of modulo and exponentiation.
      [Petunjuk: Temukan pola 3^1 mod 7, 3^2 mod 7, 3^3 mod 7, ...]
""")

solution_header("12", "Tantangan Integrasi")

# (a) ROT-13
def rot13(text):
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - base + 13) % 26 + base)
        else:
            result += c
    return result

plaintext = "MATH"
encrypted = rot13(plaintext)
decrypted = rot13(encrypted)
print(f"\n  (a) ROT-13:")
print(f"      Plaintext:  {plaintext}")
print(f"      Encrypted:  {encrypted}")
print(f"      Decrypted:  {decrypted}")
print(f"      Mengapa sama? 13+13=26=0 mod 26 (mengenkripsi dua kali = identitas!)")
print(f"      Why same? 13+13=26≡0(mod 26), encrypting twice = identity!")
check("12a", decrypted, plaintext)

# (b) Bilangan sempurna / Perfect numbers
perfect_numbers = []
for n in range(1, 1001):
    proper_divs = [i for i in range(1, n) if n % i == 0]
    if sum(proper_divs) == n:
        perfect_numbers.append((n, proper_divs))

print(f"\n  (b) Bilangan sempurna / Perfect numbers (1-1000):")
for n, divs in perfect_numbers:
    print(f"      {n} = {' + '.join(str(d) for d in divs)}")
check("12b", [n for n, _ in perfect_numbers], [6, 28, 496])

# (c) Modular exponentiation
print(f"\n  (c) 3^100 mod 7:")
print(f"      Pola / Pattern:")
for i in range(1, 8):
    print(f"        3^{i} mod 7 = {3**i % 7}")
print(f"      Pola berulang setiap 6 / Pattern repeats every 6")
print(f"      100 mod 6 = {100 % 6}  → 3^100 mod 7 = 3^{100%6} mod 7 = {3**(100%6) % 7}")
direct = pow(3, 100, 7)  # Python built-in modular exponentiation
print(f"      Verifikasi pow(3,100,7) = {direct}")
check("12c", 3**(100%6) % 7, direct)


# ===========================================================================
# RINGKASAN / SUMMARY
# ===========================================================================

print("\n" + "="*65)
print("  RINGKASAN LATIHAN / EXERCISE SUMMARY")
print("="*65)
print("""
  Soal  1: Sifat komutatif/asosiatif (+, -)      [★☆☆]
  Soal  2: Urutan operasi PEMDAS                  [★☆☆]
  Soal  3: Algoritma Euclidean (FPB)              [★★☆]
  Soal  4: Aritmatika modular                     [★★☆]
  Soal  5: Hukum perpangkatan                    [★★☆]
  Soal  6: Faktorisasi prima                      [★★☆]
  Soal  7: Masalah kata (word problems)           [★★☆]
  Soal  8: Sifat bilangan negatif                 [★☆☆]
  Soal  9: Sifat distributif                      [★★☆]
  Soal 10: Kesamaan dan ketidaksamaan            [★★☆]
  Soal 11: Nilai mutlak                           [★★☆]
  Soal 12: Tantangan integrasi                   [★★★]
""")
