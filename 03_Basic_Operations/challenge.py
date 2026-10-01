"""
challenge.py — Tantangan Tingkat Lanjut: Operasi Dasar
Phase 1 — Topic 1.3

6 Challenge tingkat lanjut — implementasikan SEMUA dari nol!
Urutkan kesulitan: Ch4 → Ch5 → Ch3 → Ch6 → Ch1 → Ch2
"""
import time
from typing import List, Tuple

print("=" * 70)
print("CHALLENGE 1.3 — OPERASI DASAR TINGKAT LANJUT")
print("=" * 70)

# ═══════════════════════════════════════════════════════════════════════
# [Ch4] FAST EXPONENTIATION (Binary Method) — MULAI DARI SINI!
# ═══════════════════════════════════════════════════════════════════════
# KONSEP:
#   Algoritma Squaring Berulang: a^n dapat dihitung dalam O(log n) perkalian.
#   Ide: a^n = (a^(n//2))² jika n genap
#             a × (a^(n//2))² jika n ganjil
#
# LANGKAH untuk fast_pow(base, exp, mod=None):
#   1. Jika exp == 0: return 1
#   2. Jika exp ganjil: return base × fast_pow(base, exp-1, mod)
#      ATAU (lebih efisien dengan iterasi):
#      result = 1
#      while exp > 0:
#          if exp % 2 == 1: result *= base
#          base *= base
#          exp //= 2
#   3. Jika ada mod: terapkan % mod di setiap langkah
#
# IMPLEMENTASIKAN:
print("\n[Ch4] Fast Exponentiation")

def fast_pow(base, exp, mod=None):
    """
    Hitung base^exp (mod m) menggunakan binary exponentiation.
    Kompleksitas: O(log exp)
    """
    # TODO: implementasikan binary exponentiation
    pass

# TODO: uncomment untuk uji
# print(f"  2^10 = {fast_pow(2, 10)}")             # harus: 1024
# print(f"  3^100 mod 1000 = {fast_pow(3, 100, 1000)}")  # harus: 1
# print(f"  2^1000 = {fast_pow(2, 1000)}")         # bilangan sangat besar
# Jawaban: 2^10=1024, 3^100 mod 1000 = 1


# ═══════════════════════════════════════════════════════════════════════
# [Ch5] SIEVE OF ERATOSTHENES
# ═══════════════════════════════════════════════════════════════════════
# KONSEP:
#   Algoritma klasik untuk menemukan semua bilangan prima ≤ N.
#   Tandai kelipatan setiap prima sebagai BUKAN prima.
#
# LANGKAH untuk sieve(n):
#   1. Buat array is_prime = [True] * (n+1)
#   2. is_prime[0] = is_prime[1] = False
#   3. Loop p dari 2 sampai sqrt(n):
#      a. Jika is_prime[p]: tandai semua kelipatan p (mulai p*p) sebagai False
#   4. Return list semua p yang is_prime[p] == True
#
# IMPLEMENTASIKAN:
print("\n[Ch5] Sieve of Eratosthenes")

def sieve(n):
    """Kembalikan list semua bilangan prima <= n."""
    # TODO: implementasikan Sieve of Eratosthenes
    pass

# TODO: uncomment untuk uji
# primes_100 = sieve(100)
# print(f"  Prima <= 100: {len(primes_100)} bilangan")
# print(f"  5 prima pertama: {primes_100[:5]}")    # [2,3,5,7,11]
# print(f"  5 prima terakhir: {primes_100[-5:]}")   # [79,83,89,97]
# Jawaban: 25 prima, [2,3,5,7,11,...,97]


# ═══════════════════════════════════════════════════════════════════════
# [Ch3] VARIAN ALGORITMA EUCLIDEAN
# ═══════════════════════════════════════════════════════════════════════
# KONSEP:
#   Extended Euclidean: Selain GCD, temukan x,y sehingga ax + by = gcd(a,b)
#   Binary GCD (Stein): Gunakan operasi bit — lebih cepat dari Euclidean di hardware.
#
# LANGKAH untuk extended_gcd(a, b):
#   Base case: if b == 0: return a, 1, 0
#   Rekursif: g, x1, y1 = extended_gcd(b, a % b)
#   Kembalikan: g, y1, x1 - (a//b)*y1
#
# LANGKAH untuk binary_gcd(a, b) [Stein's Algorithm]:
#   1. Jika a==0: return b; jika b==0: return a
#   2. Jika keduanya genap: return 2 * binary_gcd(a>>1, b>>1)
#   3. Jika a genap: return binary_gcd(a>>1, b)
#   4. Jika b genap: return binary_gcd(a, b>>1)
#   5. return binary_gcd(|a-b|, min(a,b))
#
# IMPLEMENTASIKAN:
print("\n[Ch3] Varian Algoritma Euclidean")

def extended_gcd(a, b):
    """Extended Euclidean: return (g, x, y) sehingga a*x + b*y = g."""
    # TODO: implementasikan extended Euclidean
    pass

def binary_gcd(a, b):
    """Binary GCD (Stein Algorithm) — menggunakan operasi bit."""
    # TODO: implementasikan Stein's algorithm
    pass

# TODO: uncomment untuk uji
# g, x, y = extended_gcd(35, 15)
# print(f"  GCD(35,15)={g}, x={x}, y={y}")
# print(f"  Verifikasi: 35×{x} + 15×{y} = {35*x + 15*y}")   # harus = g
# print(f"  binary_gcd(48, 18) = {binary_gcd(48, 18)}")       # harus: 6
# Jawaban: g=5, verifikasi=5, binary_gcd=6


# ═══════════════════════════════════════════════════════════════════════
# [Ch6] CHINESE REMAINDER THEOREM (CRT)
# ═══════════════════════════════════════════════════════════════════════
# KONSEP:
#   Sistem kongruensi: x ≡ r1 (mod m1), x ≡ r2 (mod m2), ...
#   Jika semua m_i saling prima: ada solusi unik x (mod M) dimana M = m1*m2*...*mk
#   Solusi: x = Σ r_i × M_i × (M_i^(-1) mod m_i)
#   dimana M_i = M / m_i
#
# LANGKAH untuk crt(remainders, moduli):
#   1. M = product(moduli)
#   2. Untuk setiap i: M_i = M // moduli[i]
#   3. Cari invers: inv_i = M_i^(-1) mod moduli[i]
#      (gunakan extended_gcd: M_i*x ≡ 1 (mod m_i))
#   4. x = sum(r_i * M_i * inv_i) % M
#
# IMPLEMENTASIKAN:
print("\n[Ch6] Chinese Remainder Theorem")

def crt(remainders, moduli):
    """
    Selesaikan sistem kongruensi simultan.
    x ≡ remainders[i] (mod moduli[i]) untuk semua i.
    Prasyarat: semua moduli saling prima.
    Return x (solusi terkecil >= 0).
    """
    # TODO: implementasikan CRT
    pass

# TODO: uncomment untuk uji
# x = crt([2, 3, 2], [3, 5, 7])
# print(f"  x ≡ 2(mod3), 3(mod5), 2(mod7) → x = {x}")  # harus: 23
# print(f"  Verifikasi: {x}%3={x%3}, {x}%5={x%5}, {x}%7={x%7}")
# Jawaban: x=23


# ═══════════════════════════════════════════════════════════════════════
# [Ch1] ARBITRARY PRECISION ARITHMETIC (BigInt) — TANTANGAN TERBESAR!
# ═══════════════════════════════════════════════════════════════════════
# KONSEP:
#   Bilangan bulat besar disimpan sebagai list digit dalam basis B=10^9.
#   Operasi dilakukan digit per digit dengan carry/borrow.
#
# LANGKAH untuk BigInt.__init__(value):
#   1. Jika int: konversi ke list digit basis B (digit dari LSB ke MSB)
#   2. Jika str: parse tanda, lalu split ke chunks 9 digit
#
# LANGKAH untuk BigInt.__add__(other):
#   1. Loop per digit dengan carry
#   2. digit_result = self.digits[i] + other.digits[i] + carry
#   3. new_digit = digit_result % B
#   4. carry = digit_result // B
#
# LANGKAH untuk BigInt.__mul__(other):
#   1. Alokasi result berukuran len(self)+len(other)
#   2. Loop i,j: result[i+j] += self.digits[i] * other.digits[j]
#   3. Propagasi carry
#
# IMPLEMENTASIKAN:
print("\n[Ch1] BigInt — Arbitrary Precision Arithmetic")

class BigInt:
    """Bilangan bulat presisi arbitrer dari nol. Basis: 10^9"""
    BASE = 10**9

    def __init__(self, value=0):
        self.negative = False
        self.digits = []
        # TODO: implementasikan parsing dari int atau str
        pass

    def __repr__(self):
        # TODO: konversi kembali ke string desimal
        pass

    def __add__(self, other):
        # TODO: penjumlahan dengan carry
        pass

    def __mul__(self, other):
        # TODO: perkalian long multiplication
        pass

# TODO: uncomment untuk uji
# a = BigInt("123456789012345678901234567890")
# b = BigInt("987654321098765432109876543210")
# print(f"  a = {a}")
# print(f"  b = {b}")
# print(f"  a+b = {a + b}")
# Jawaban: a+b = 1111111110111111111011111111100


# ═══════════════════════════════════════════════════════════════════════
# [Ch2] EXPRESSION PARSER — TANTANGAN PALING KOMPLEKS!
# ═══════════════════════════════════════════════════════════════════════
# KONSEP:
#   Recursive Descent Parser untuk ekspresi matematika.
#   Grammar:
#     expr   → term (('+' | '-') term)*
#     term   → factor (('*' | '/') factor)*
#     factor → atom ('^' factor)?    ← kanan-asosiatif!
#     atom   → number | '(' expr ')' | '-' atom
#
# LANGKAH untuk Tokenizer.tokenize(text):
#   1. Scan karakter satu per satu
#   2. Kumpulkan digit menjadi NUMBER token
#   3. Operator dan kurung jadi token masing-masing
#
# LANGKAH untuk Parser.parse_expr():
#   1. left = self.parse_term()
#   2. While token is '+' or '-': left = left ± parse_term()
#   3. return left
#
# IMPLEMENTASIKAN:
print("\n[Ch2] Expression Parser")

class Tokenizer:
    def __init__(self, text):
        self.tokens = []
        self.pos = 0
        # TODO: tokenize text menjadi list token

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        if self.pos < len(self.tokens): return self.tokens[self.pos]
        return None

    def consume(self, expected=None):
        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def parse_expr(self):
        # TODO: parsing level addition/subtraction
        pass

    def parse_term(self):
        # TODO: parsing level multiplication/division
        pass

    def parse_factor(self):
        # TODO: parsing level exponentiation (kanan-asosiatif!)
        pass

    def parse_atom(self):
        # TODO: parsing angka, kurung, dan unary minus
        pass

def evaluate(expression):
    """Evaluasi ekspresi matematika sebagai string."""
    t = Tokenizer(expression)
    p = Parser(t.tokens)
    return p.parse_expr()

# TODO: uncomment untuk uji
# tests = ["3 + 4 * 2", "(3+4)*2", "2^3^2", "10 - 2*(3+1)", "((2+3)*4)^2"]
# for expr in tests:
#     try:
#         result = evaluate(expr)
#         expected = eval(expr.replace("^","**"))
#         status = "✓" if abs(result - expected) < 1e-9 else "✗"
#         print(f"  {status} {expr} = {result} (expected {expected})")
#     except Exception as e:
#         print(f"  ERROR: {expr} → {e}")

print("\n[Selesai] Implementasikan semua TODO, urutan: Ch4→Ch5→Ch3→Ch6→Ch1→Ch2")
