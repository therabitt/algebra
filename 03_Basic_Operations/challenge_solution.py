"""
=============================================================================
challenge.py — Tantangan Tingkat Lanjut / Advanced Challenges
=============================================================================
Modul ini berisi 6 tantangan tingkat lanjut yang mengimplementasikan
konsep matematika dari nol menggunakan Python.

This module contains 6 advanced challenges implementing math concepts
from scratch in Python.

Tantangan / Challenges:
  1. Aritmatika Presisi Arbitrer / Arbitrary Precision Arithmetic
  2. Parser Ekspresi Lengkap / Complete Expression Parser
  3. Varian Algoritma Euclidean / Euclidean Algorithm Variants
  4. Eksponensial Cepat (Metode Biner) / Fast Exponentiation (Binary Method)
  5. Saringan Eratosthenes / Sieve of Eratosthenes
  6. Teorema Sisa Tiongkok / Chinese Remainder Theorem

Semua implementasi dari nol (tanpa library eksternal untuk algoritma inti).
All implementations from scratch (no external libraries for core algorithms).
=============================================================================
"""

import time
from typing import List, Tuple, Dict


# =============================================================================
# KONSEP: Bilangan bulat besar disimpan sebagai array digit dalam basis tertentu, lalu operasi dilakukan digit per digit.
# CHALLENGE 1: ARITMATIKA PRESISI ARBITRER
#              ARBITRARY PRECISION ARITHMETIC
# =============================================================================

print("=" * 70)
print("CHALLENGE 1: ARITMATIKA PRESISI ARBITRER / ARBITRARY PRECISION ARITHMETIC")
print("=" * 70)

class BigInt:
    """
    Implementasi bilangan bulat presisi arbitrer dari nol.
    Arbitrary precision integer implementation from scratch.

    ID: Python sudah mendukung ini secara native, tetapi ini menunjukkan
    prinsip dasarnya: simpan digit dalam basis tertentu.

    EN: Python already supports this natively, but this demonstrates
    the underlying principle: store digits in a chosen base.

    Implementasi ini menggunakan basis 10^9 untuk efisiensi.
    This implementation uses base 10^9 for efficiency.
    """

    BASE = 10**9  # Basis / Base

    def __init__(self, value=0):
        """
        Inisialisasi dari int, str, atau list digit (dalam basis BASE).
        Initialize from int, str, or list of digits (in BASE).
        """
        self.negative = False
        self.digits = []  # Digit dari least significant ke most significant

        if isinstance(value, str):
            value = value.strip()
            if value.startswith('-'):
                self.negative = True
                value = value[1:]
            # Konversi string ke digit basis 10^9
            while value:
                chunk = value[-9:]   # ambil 9 digit terakhir / take last 9 digits
                value = value[:-9]
                self.digits.append(int(chunk))
        elif isinstance(value, int):
            if value < 0:
                self.negative = True
                value = -value
            if value == 0:
                self.digits = [0]
            else:
                while value > 0:
                    self.digits.append(value % self.BASE)
                    value //= self.BASE
        elif isinstance(value, list):
            self.digits = value[:]

        self._normalize()

    def _normalize(self):
        """Hapus leading zeros / Remove leading zeros."""
        while len(self.digits) > 1 and self.digits[-1] == 0:
            self.digits.pop()
        if self.digits == [0]:
            self.negative = False

    def __str__(self):
        """Konversi ke string / Convert to string."""
        if not self.digits or self.digits == [0]:
            return '0'
        result = str(self.digits[-1])  # Most significant digit (tanpa leading zeros)
        for d in reversed(self.digits[:-1]):
            result += str(d).zfill(9)  # Digit lainnya dipad / Other digits padded
        return ('-' if self.negative else '') + result

    def __repr__(self):
        return f"BigInt('{self}')"

    def __abs__(self):
        result = BigInt(self.digits[:])
        result.negative = False
        return result

    def __eq__(self, other):
        if isinstance(other, int):
            other = BigInt(other)
        return self.negative == other.negative and self.digits == other.digits

    def __lt__(self, other):
        if isinstance(other, int):
            other = BigInt(other)
        if self.negative != other.negative:
            return self.negative
        if self.negative:
            return self._abs_gt(other)
        return self._abs_lt(other)

    def _abs_lt(self, other):
        if len(self.digits) != len(other.digits):
            return len(self.digits) < len(other.digits)
        return list(reversed(self.digits)) < list(reversed(other.digits))

    def _abs_gt(self, other):
        return other._abs_lt(self)

    def __add__(self, other):
        """Penjumlahan / Addition."""
        if isinstance(other, int):
            other = BigInt(other)

        # Tangani tanda / Handle signs
        if self.negative == other.negative:
            result = BigInt(self._add_abs(self.digits, other.digits))
            result.negative = self.negative
            return result
        else:
            if self._abs_lt(other):
                result = BigInt(self._sub_abs(other.digits, self.digits))
                result.negative = other.negative
            else:
                result = BigInt(self._sub_abs(self.digits, other.digits))
                result.negative = self.negative
            return result

    def __mul__(self, other):
        """
        Perkalian menggunakan algoritma grade-school.
        Multiplication using grade-school algorithm.
        Kompleksitas / Complexity: O(n²) di mana n = jumlah digit
        """
        if isinstance(other, int):
            other = BigInt(other)

        result_digits = [0] * (len(self.digits) + len(other.digits))

        # Kalikan setiap digit dari self dengan setiap digit dari other
        # Multiply each digit of self with each digit of other
        for i, d1 in enumerate(self.digits):
            carry = 0
            for j, d2 in enumerate(other.digits):
                product = d1 * d2 + result_digits[i+j] + carry
                result_digits[i+j] = product % self.BASE
                carry = product // self.BASE
            if carry:
                result_digits[i+len(other.digits)] += carry

        result = BigInt(result_digits)
        result.negative = self.negative != other.negative
        result._normalize()
        return result

    @staticmethod
    def _add_abs(a, b):
        """Penjumlahan nilai mutlak / Add absolute values."""
        result = []
        carry = 0
        for i in range(max(len(a), len(b))):
            ai = a[i] if i < len(a) else 0
            bi = b[i] if i < len(b) else 0
            total = ai + bi + carry
            result.append(total % BigInt.BASE)
            carry = total // BigInt.BASE
        if carry:
            result.append(carry)
        return result

    @staticmethod
    def _sub_abs(a, b):
        """Pengurangan |a| - |b| dimana |a| >= |b| / Subtract |a| - |b| where |a| >= |b|."""
        result = []
        borrow = 0
        for i in range(len(a)):
            ai = a[i]
            bi = b[i] if i < len(b) else 0
            diff = ai - bi - borrow
            if diff < 0:
                diff += BigInt.BASE
                borrow = 1
            else:
                borrow = 0
            result.append(diff)
        return result

    def factorial(n: int) -> 'BigInt':
        """n! menggunakan BigInt / n! using BigInt."""
        result = BigInt(1)
        for i in range(2, n+1):
            result = result * BigInt(i)
        return result


# Demonstrasi / Demonstration
print("\nBigInt Arithmetic:")
a_big = BigInt("123456789012345678901234567890")
b_big = BigInt("987654321098765432109876543210")

print(f"  a = {a_big}")
print(f"  b = {b_big}")
print(f"  a + b = {a_big + b_big}")

# Verifikasi dengan Python native int
a_py = 123456789012345678901234567890
b_py = 987654321098765432109876543210
assert str(a_big + b_big) == str(a_py + b_py)
print(f"  Verifikasi ✓ (cocok dengan Python native int)")

# Perkalian / Multiplication
c_big = BigInt("99999")
d_big = BigInt("99999")
print(f"\n  {c_big} × {d_big} = {c_big * d_big}")
assert str(c_big * d_big) == str(99999 * 99999)
print(f"  Verifikasi ✓")

# Faktorial besar / Large factorial
print(f"\nFaktorial besar / Large factorials:")
for n_fact in [10, 20, 50]:
    result = BigInt.factorial(n_fact)
    expected = 1
    for i in range(2, n_fact+1):
        expected *= i
    assert str(result) == str(expected)
    result_str = str(result)
    print(f"  {n_fact}! = {result_str[:30]}... ({len(result_str)} digit)")
print(f"  Verifikasi semua faktorial ✓")


# =============================================================================
# KONSEP: Parser ekspresi menggunakan recursive descent: expr → term → factor → atom.
# CHALLENGE 2: PARSER EKSPRESI MATEMATIKA LENGKAP
#              COMPLETE MATHEMATICAL EXPRESSION PARSER
# =============================================================================

print("\n" + "=" * 70)
print("CHALLENGE 2: PARSER EKSPRESI / EXPRESSION PARSER")
print("=" * 70)

class Token:
    """Token untuk lexer / Token for lexer."""
    NUMBER = 'NUMBER'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MUL = 'MUL'
    DIV = 'DIV'
    FLOORDIV = 'FLOORDIV'
    MOD = 'MOD'
    POW = 'POW'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    EOF = 'EOF'

    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'


class Lexer:
    """
    Lexer (Tokenizer): Mengubah string menjadi stream token.
    Lexer (Tokenizer): Converts string to token stream.
    """
    def __init__(self, text):
        self.text = text.replace(' ', '')  # hapus spasi / remove spaces
        self.pos = 0

    def peek(self):
        return self.text[self.pos] if self.pos < len(self.text) else None

    def next_token(self):
        if self.pos >= len(self.text):
            return Token(Token.EOF, None)

        char = self.text[self.pos]

        # Bilangan / Number
        if char.isdigit() or (char == '.' and self.pos+1 < len(self.text) and self.text[self.pos+1].isdigit()):
            num_str = ''
            while self.pos < len(self.text) and (self.text[self.pos].isdigit() or self.text[self.pos] == '.'):
                num_str += self.text[self.pos]
                self.pos += 1
            return Token(Token.NUMBER, float(num_str) if '.' in num_str else int(num_str))

        self.pos += 1

        # Operator dua karakter / Two-char operators
        if char == '*' and self.peek() == '*':
            self.pos += 1
            return Token(Token.POW, '**')
        if char == '/' and self.peek() == '/':
            self.pos += 1
            return Token(Token.FLOORDIV, '//')

        ops = {
            '+': Token.PLUS, '-': Token.MINUS,
            '*': Token.MUL,  '/': Token.DIV,
            '%': Token.MOD,  '^': Token.POW,
            '(': Token.LPAREN, ')': Token.RPAREN,
        }
        if char in ops:
            return Token(ops[char], char)

        raise ValueError(f"Karakter tidak dikenal: '{char}'")

    def tokenize(self):
        tokens = []
        tok = self.next_token()
        while tok.type != Token.EOF:
            tokens.append(tok)
            tok = self.next_token()
        tokens.append(Token(Token.EOF, None))
        return tokens


class Parser:
    """
    Recursive Descent Parser dengan Precedence Climbing.
    Implements correct operator precedence (PEMDAS).

    Grammar / Tata Bahasa:
        expr    : term ((PLUS | MINUS) term)*
        term    : factor ((MUL | DIV | FLOORDIV | MOD) factor)*
        factor  : power (POW factor)?          [right-associative]
        power   : PLUS unary | MINUS unary | atom
        atom    : NUMBER | LPAREN expr RPAREN

    Urutan Prioritas (rendah ke tinggi / low to high):
        + -   →  level 1
        * / % →  level 2
        **    →  level 3 (kanan-asosiatif / right-associative)
        unary →  level 4
        ()    →  level 5
    """

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos]

    def consume(self, type_=None):
        tok = self.current()
        if type_ and tok.type != type_:
            raise SyntaxError(f"Ekspektasi {type_}, dapat {tok.type}")
        self.pos += 1
        return tok

    def parse(self):
        result = self.expr()
        self.consume(Token.EOF)
        return result

    def expr(self):
        """Penjumlahan dan pengurangan / Addition and subtraction."""
        left = self.term()
        while self.current().type in (Token.PLUS, Token.MINUS):
            op = self.consume().type
            right = self.term()
            left = left + right if op == Token.PLUS else left - right
        return left

    def term(self):
        """Perkalian, pembagian, modulo / Multiplication, division, modulo."""
        left = self.factor()
        while self.current().type in (Token.MUL, Token.DIV, Token.FLOORDIV, Token.MOD):
            op = self.consume().type
            right = self.factor()
            if op == Token.MUL:
                left = left * right
            elif op == Token.DIV:
                left = left / right
            elif op == Token.FLOORDIV:
                left = left // right
            elif op == Token.MOD:
                left = left % right
        return left

    def factor(self):
        """Perpangkatan (kanan-asosiatif) / Exponentiation (right-associative)."""
        base = self.unary()
        if self.current().type == Token.POW:
            self.consume(Token.POW)
            exp = self.factor()  # KANAN-asosiatif! / RIGHT-associative!
            return base ** exp
        return base

    def unary(self):
        """Unary plus dan minus / Unary plus and minus."""
        if self.current().type == Token.PLUS:
            self.consume(Token.PLUS)
            return +self.atom()
        elif self.current().type == Token.MINUS:
            self.consume(Token.MINUS)
            return -self.atom()
        return self.atom()

    def atom(self):
        """Bilangan atau sub-ekspresi dalam kurung / Number or parenthesized sub-expression."""
        tok = self.current()
        if tok.type == Token.NUMBER:
            self.consume(Token.NUMBER)
            return tok.value
        elif tok.type == Token.LPAREN:
            self.consume(Token.LPAREN)
            result = self.expr()
            self.consume(Token.RPAREN)
            return result
        else:
            raise SyntaxError(f"Unexpected token: {tok}")


def evaluate(expression: str) -> float:
    """
    Evaluasi ekspresi matematika dengan urutan operasi yang benar.
    Evaluate a mathematical expression with correct order of operations.
    """
    lexer = Lexer(expression)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    return parser.parse()


# Demonstrasi / Demonstration
print("\nParser Ekspresi Matematika / Mathematical Expression Parser:")
print("(Implementasi parser dari nol dengan precedence climbing)")
print()

test_exprs = [
    ("2 + 3 * 4",           2 + 3*4),
    ("(2 + 3) * 4",         (2+3)*4),
    ("2 ** 3 ** 2",         2**3**2),   # kanan-asosiatif / right-assoc
    ("2 + 3 * 4 ** 2 - 6 / 2", 2 + 3*4**2 - 6/2),
    ("10 % 3 + 2 * 5",      10%3 + 2*5),
    ("100 // 7 * 7 + 100 % 7", 100//7*7 + 100%7),  # = 100
    ("-3 + 4 * -2",         -3 + 4 * -2),
    ("2 ** (1 + 1 + 1)",    2**(1+1+1)),
]

all_ok = True
for expr_str, expected in test_exprs:
    result = evaluate(expr_str)
    ok = abs(float(result) - float(expected)) < 1e-9
    status = "✓" if ok else "✗"
    print(f"  {status} evaluate('{expr_str}') = {result}  (ekspektasi: {expected})")
    if not ok:
        all_ok = False

print(f"\n  {'Semua ekspresi diparse dengan benar! / All expressions parsed correctly!' if all_ok else 'Ada kesalahan!'}")


# =============================================================================
# KONSEP: Variasi Euclidean: Stein (binary GCD), Extended Euclidean (ax+by=gcd), LCM.
# CHALLENGE 3: VARIAN ALGORITMA EUCLIDEAN
#              EUCLIDEAN ALGORITHM VARIANTS
# =============================================================================

print("\n" + "=" * 70)
print("CHALLENGE 3: VARIAN ALGORITMA EUCLIDEAN / EUCLIDEAN ALGORITHM VARIANTS")
print("=" * 70)

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Algoritma Euclidean yang Diperluas / Extended Euclidean Algorithm.

    Mengembalikan (gcd, x, y) sehingga / Returns (gcd, x, y) such that:
      a*x + b*y = gcd(a, b)  [Identitas Bezout / Bezout's Identity]

    Berguna untuk / Useful for:
    - Menemukan invers modular / Finding modular inverse
    - Memecahkan persamaan Diophantine / Solving Diophantine equations
    - Algoritma RSA

    Kompleksitas / Complexity: O(log min(a, b))
    """
    if b == 0:
        return a, 1, 0  # GCD(a, 0) = a, koefisien: 1*a + 0*0 = a
    else:
        gcd, x, y = extended_gcd(b, a % b)
        # Derivasi / Derivation:
        # Dari langkah rekursif: b*x + (a%b)*y = gcd
        # Substitusi a%b = a - (a//b)*b:
        # b*x + (a - (a//b)*b)*y = gcd
        # a*y + b*(x - (a//b)*y) = gcd
        return gcd, y, x - (a // b) * y


def gcd_binary(a: int, b: int) -> int:
    """
    Algoritma GCD Biner (Binary GCD / Stein's Algorithm).

    Menghindari pembagian modulo menggunakan operasi bitwise.
    Avoids modulo division using bitwise operations.
    Lebih efisien pada hardware yang modulo-nya lambat.
    More efficient on hardware where modulo is slow.

    Properti yang digunakan / Properties used:
    1. GCD(0, n) = n
    2. GCD(even, even) = 2 * GCD(n/2, m/2)
    3. GCD(even, odd)  = GCD(n/2, m)
    4. GCD(odd, odd)   = GCD(|n-m|/2, m)   [atau versi lain]
    """
    if a == 0: return b
    if b == 0: return a

    # Temukan faktor 2 bersama / Find common factor of 2
    shift = 0
    while ((a | b) & 1) == 0:  # keduanya genap / both even
        a >>= 1
        b >>= 1
        shift += 1

    # Hapus semua faktor 2 dari a / Remove all factors of 2 from a
    while (a & 1) == 0:
        a >>= 1

    while b:
        # Hapus faktor 2 dari b / Remove factors of 2 from b
        while (b & 1) == 0:
            b >>= 1

        # Pastikan a <= b / Ensure a <= b
        if a > b:
            a, b = b, a

        # GCD(odd, odd) = GCD((b-a)/2, a)
        b -= a

    return a << shift  # Kembalikan faktor 2 / Restore factor of 2


def modular_inverse(a: int, m: int) -> int:
    """
    Invers modular dari a mod m.
    Modular inverse of a mod m.

    Cari x sehingga / Find x such that: a*x ≡ 1 (mod m)

    Menggunakan extended GCD / Uses extended GCD.
    Solusi ada jika dan hanya jika / Solution exists iff GCD(a, m) = 1.
    """
    gcd, x, _ = extended_gcd(a % m, m)
    if gcd != 1:
        raise ValueError(f"Invers modular tidak ada: GCD({a},{m}) = {gcd} ≠ 1")
    return x % m


# Demonstrasi / Demonstration
print("\nAlgoritma Euclidean yang Diperluas / Extended Euclidean Algorithm:")
print("Format / Format: GCD(a,b) = a*x + b*y  [Identitas Bezout]")
print()

ext_cases = [(35, 15), (161, 28), (252, 105), (1071, 462), (17, 13)]
for a, b in ext_cases:
    g, x, y = extended_gcd(a, b)
    # Verifikasi / Verify
    assert g == a*x + b*y, f"Extended GCD gagal untuk ({a},{b})"
    assert g == __import__('math').gcd(a, b)
    print(f"  GCD({a:4d},{b:3d}) = {g:3d} = {a:4d}×({x:3d}) + {b:3d}×({y:3d}) ✓")

print(f"\nAlgoritma GCD Biner / Binary GCD (Stein's Algorithm):")
for a, b in ext_cases:
    g_bin = gcd_binary(a, b)
    g_ref = __import__('math').gcd(a, b)
    assert g_bin == g_ref
    print(f"  binary_gcd({a:4d},{b:3d}) = {g_bin:3d} ✓")

print(f"\nInvers Modular / Modular Inverse (a*x ≡ 1 mod m):")
inv_cases = [(3, 7), (5, 11), (17, 31), (2, 5), (7, 26)]
for a, m in inv_cases:
    try:
        inv = modular_inverse(a, m)
        assert (a * inv) % m == 1
        print(f"  inverse({a}, {m}) = {inv}   → {a}×{inv} mod {m} = {(a*inv)%m} ✓")
    except ValueError as e:
        print(f"  inverse({a}, {m}): {e}")


# =============================================================================
# KONSEP: Fast exponentiation: a^n = (a^(n/2))² jika n genap, kompleksitas O(log n).
# CHALLENGE 4: EKSPONENSIAL CEPAT (METODE BINER)
#              FAST EXPONENTIATION (BINARY METHOD)
# =============================================================================

print("\n" + "=" * 70)
print("CHALLENGE 4: EKSPONENSIAL CEPAT / FAST EXPONENTIATION (Square-and-Multiply)")
print("=" * 70)

def fast_pow(base: int, exp: int, mod: int = None) -> int:
    """
    Eksponensial cepat menggunakan metode kuadrat-dan-kalikan.
    Fast exponentiation using square-and-multiply method.

    PRINSIP / PRINCIPLE:
    Representasikan eksponen dalam biner.
    Represent exponent in binary.

    Contoh / Example: 3^13 = 3^(1101₂) = 3^8 × 3^4 × 3^1
    Hanya butuh 5 perkalian, bukan 12!
    Only needs 5 multiplications, not 12!

    ALGORITMA / ALGORITHM:
    result = 1
    while exp > 0:
        if exp & 1:    ← bit paling rendah / least significant bit
            result *= base
        base = base²   ← kuadratkan basis / square the base
        exp >>= 1      ← geser kanan / right shift (bagi 2 / divide by 2)

    KOMPLEKSITAS / COMPLEXITY:
    - Naive: O(n) perkalian
    - Fast:  O(log n) perkalian  ← sangat lebih cepat! / much faster!
    """
    if mod:
        return fast_pow_mod(base, exp, mod)

    if exp < 0:
        # Invers untuk eksponen negatif / Inverse for negative exponent
        return 1 / fast_pow(base, -exp)

    result = 1
    while exp > 0:
        if exp & 1:     # Jika bit terakhir adalah 1 / If last bit is 1
            result *= base
        base *= base    # Kuadratkan basis / Square the base
        exp >>= 1       # Bagi eksponen dengan 2 / Divide exponent by 2

    return result


def fast_pow_mod(base: int, exp: int, mod: int) -> int:
    """
    Eksponensial modular cepat / Fast modular exponentiation.
    Menghitung base^exp mod m secara efisien.

    Kunci / Key: (a × b) mod m = ((a mod m) × (b mod m)) mod m
    Ini mencegah angka menjadi sangat besar!
    This prevents numbers from becoming enormous!

    Digunakan dalam / Used in:
    - RSA encryption
    - Diffie-Hellman key exchange
    - Miller-Rabin primality test
    """
    result = 1
    base = base % mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result


def fast_pow_with_trace(base: int, exp: int) -> int:
    """Versi dengan trace untuk demonstrasi / Version with trace for demonstration."""
    binary = bin(exp)[2:]  # Representasi biner eksponen
    print(f"\n  base={base}, exp={exp}, biner/binary={binary}")
    print(f"  Langkah / Steps:")

    result = 1
    current_power = base
    for i, bit in enumerate(reversed(binary)):
        if bit == '1':
            old_result = result
            result *= current_power
            print(f"    bit[{i}]=1: result = {old_result} × {current_power} = {result}")
        else:
            print(f"    bit[{i}]=0: skip, result = {result}")
        current_power *= current_power
        if i < len(binary) - 1:
            print(f"           kuadratkan basis: {current_power // current_power} → {current_power} (basis baru)")

    return result


# Demonstrasi / Demonstration
print("\nEksponensial Cepat / Fast Exponentiation:")
fast_pow_with_trace(2, 13)

print("\nBenchmark: Naive vs Fast Exponentiation:")
import time

def naive_pow(base, exp, mod):
    result = 1
    for _ in range(exp):
        result = (result * base) % mod
    return result

test_cases_pow = [
    (2, 1000, 10**9+7),
    (3, 10000, 10**9+7),
    (7, 100000, 998244353),
]

for base, exp, mod in test_cases_pow:
    t0 = time.perf_counter()
    fast_result = fast_pow_mod(base, exp, mod)
    t1 = time.perf_counter()
    fast_time = (t1 - t0) * 1e6

    # Python's built-in pow(base, exp, mod) juga cepat
    builtin_result = pow(base, exp, mod)

    assert fast_result == builtin_result
    print(f"  {base}^{exp} mod {mod}: result={fast_result}")
    print(f"    Fast pow: {fast_time:.2f} μs  ({int(exp).bit_length()} langkah/steps) ✓")


# =============================================================================
# KONSEP: Sieve of Eratosthenes: tandai semua kelipatan bilangan prima sebagai komposit.
# CHALLENGE 5: SARINGAN ERATOSTHENES / SIEVE OF ERATOSTHENES
# =============================================================================

print("\n" + "=" * 70)
print("CHALLENGE 5: SARINGAN ERATOSTHENES / SIEVE OF ERATOSTHENES")
print("=" * 70)

def sieve_of_eratosthenes(limit: int) -> List[int]:
    """
    Saringan Eratosthenes untuk mencari semua bilangan prima hingga batas.
    Sieve of Eratosthenes to find all primes up to a limit.

    ALGORITMA / ALGORITHM:
    1. Buat array boolean [True] * (limit+1)
       Create boolean array [True] * (limit+1)
    2. Tandai 0 dan 1 sebagai non-prima / Mark 0 and 1 as non-prime
    3. Untuk setiap p dari 2 hingga sqrt(limit):
       For each p from 2 to sqrt(limit):
       - Jika p masih ditandai prima / If p is still marked prime:
         - Tandai semua kelipatan p (mulai dari p²) sebagai non-prima
           Mark all multiples of p (starting from p²) as non-prime
    4. Bilangan yang masih True adalah prima / Numbers still True are prime

    MENGAPA MULAI DARI p²? / WHY START FROM p²?
    Semua kelipatan p yang lebih kecil dari p² sudah ditandai
    oleh faktor prima yang lebih kecil.
    All multiples of p smaller than p² have already been marked
    by smaller prime factors.

    KOMPLEKSITAS / COMPLEXITY:
    - Waktu / Time:  O(n log log n)  ← hampir linear!
    - Ruang / Space: O(n)
    """
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= limit:
        if is_prime[p]:
            # Tandai semua kelipatan p mulai dari p^2
            # Mark all multiples of p starting from p^2
            for multiple in range(p*p, limit+1, p):
                is_prime[multiple] = False
        p += 1

    return [i for i, prime in enumerate(is_prime) if prime]


def segmented_sieve(limit: int) -> List[int]:
    """
    Saringan tersegmen untuk bilangan prima besar.
    Segmented sieve for large prime numbers.
    Lebih efisien memori untuk limit besar.
    More memory efficient for large limits.
    """
    import math
    sqrt_limit = int(math.isqrt(limit))
    small_primes = sieve_of_eratosthenes(sqrt_limit)

    primes = list(small_primes)
    segment_size = max(sqrt_limit, 1000)

    low = sqrt_limit + 1
    while low <= limit:
        high = min(low + segment_size - 1, limit)
        is_prime_seg = [True] * (high - low + 1)

        for p in small_primes:
            # Kelipatan pertama dari p dalam segmen ini
            # First multiple of p in this segment
            start = max(p * p, ((low + p - 1) // p) * p)
            for j in range(start, high + 1, p):
                is_prime_seg[j - low] = False

        primes.extend(low + i for i, v in enumerate(is_prime_seg) if v)
        low += segment_size

    return primes


def prime_counting_function(n: int) -> int:
    """π(n): Jumlah prima ≤ n / Number of primes ≤ n."""
    return len(sieve_of_eratosthenes(n))


# Demonstrasi / Demonstration
print("\nSaringan Eratosthenes / Sieve of Eratosthenes:")
primes_100 = sieve_of_eratosthenes(100)
print(f"\nBilangan prima ≤ 100 / Primes ≤ 100:")
print(f"  {primes_100}")
print(f"  Jumlah / Count: π(100) = {len(primes_100)}")

print(f"\nFungsi Penghitung Prima / Prime Counting Function π(n):")
for n_pi in [10, 100, 1000, 10000, 100000]:
    pi_n = prime_counting_function(n_pi)
    # Aproksimasi / Approximation: n/ln(n) (Prime Number Theorem)
    approx = n_pi / (n_pi.bit_length() * 0.693)  # log(n) ≈ bit_length * ln(2)
    print(f"  π({n_pi:6d}) = {pi_n:4d}  (aproksimasi n/ln(n) ≈ {approx:.0f})")

# Twin primes (prima kembar / twin primes)
print(f"\nPrima Kembar / Twin Primes (p dan p+2 keduanya prima):")
primes_200 = sieve_of_eratosthenes(200)
twins = [(p, p+2) for p, q in zip(primes_200, primes_200[1:]) if q == p+2]
print(f"  {twins[:10]}...")

# Prima Mersenne / Mersenne primes
print(f"\nPrima Mersenne / Mersenne Primes (2^p - 1) hingga p=20:")
mersenne = [(p, 2**p-1) for p in primes_100[:10] if 2**p-1 in set(sieve_of_eratosthenes(2**20))]
for p, m in mersenne:
    print(f"  2^{p} - 1 = {m}  [prima!]")


# =============================================================================
# KONSEP: Chinese Remainder Theorem: solusi unik x ≡ rᵢ (mod mᵢ) jika semua mᵢ saling prima.
# CHALLENGE 6: TEOREMA SISA TIONGKOK / CHINESE REMAINDER THEOREM
# =============================================================================

print("\n" + "=" * 70)
print("CHALLENGE 6: TEOREMA SISA TIONGKOK / CHINESE REMAINDER THEOREM (CRT)")
print("=" * 70)

print("""
DESKRIPSI / DESCRIPTION:
  Teorema Sisa Tiongkok / Chinese Remainder Theorem (CRT):

  Diberikan sistem kongruensi / Given a system of congruences:
    x ≡ r₁ (mod m₁)
    x ≡ r₂ (mod m₂)
    ...
    x ≡ rₖ (mod mₖ)

  Jika semua mᵢ saling koprima (GCD(mᵢ, mⱼ) = 1 untuk i≠j),
  maka terdapat SOLUSI UNIK x (mod M) di mana M = m₁ × m₂ × ... × mₖ.

  If all mᵢ are pairwise coprime, then there exists a UNIQUE solution
  x (mod M) where M = m₁ × m₂ × ... × mₖ.

APLIKASI / APPLICATIONS:
  - Kriptografi RSA / RSA cryptography
  - Komputasi paralel / Parallel computation
  - Penjadwalan / Scheduling problems
  - Pemrograman kompetitif / Competitive programming
""")

def crt(remainders: List[int], moduli: List[int]) -> Tuple[int, int]:
    """
    Teorema Sisa Tiongkok / Chinese Remainder Theorem.

    Parameter / Parameters:
        remainders: [r₁, r₂, ..., rₖ] — sisa-sisa / remainders
        moduli:     [m₁, m₂, ..., mₖ] — modulus / moduli (harus saling koprima)

    Mengembalikan / Returns:
        (x, M) di mana x ≡ rᵢ (mod mᵢ) untuk semua i, dan M = ∏mᵢ

    ALGORITMA / ALGORITHM (Konstruktif):
    1. Hitung M = m₁ × m₂ × ... × mₖ
    2. Untuk setiap i:
       - Hitung Mᵢ = M / mᵢ
       - Hitung yᵢ = invers dari Mᵢ mod mᵢ  (extended GCD)
    3. x = Σ(rᵢ × Mᵢ × yᵢ) mod M
    """
    if len(remainders) != len(moduli):
        raise ValueError("Panjang remainders dan moduli harus sama")

    # Verifikasi saling koprima / Verify pairwise coprime
    for i in range(len(moduli)):
        for j in range(i+1, len(moduli)):
            g, _, _ = extended_gcd(moduli[i], moduli[j])
            if g != 1:
                raise ValueError(f"m[{i}]={moduli[i]} dan m[{j}]={moduli[j]} tidak koprima (GCD={g})")

    # Hitung M = produk semua moduli / Calculate M = product of all moduli
    M = 1
    for m in moduli:
        M *= m

    # Konstruksi solusi / Construct solution
    x = 0
    for r, m in zip(remainders, moduli):
        Mi = M // m               # M tanpa faktor m / M without factor m
        gcd, yi, _ = extended_gcd(Mi, m)   # Invers Mᵢ mod mᵢ
        yi = yi % m               # Pastikan positif / Ensure positive
        x += r * Mi * yi

    return x % M, M


def crt_with_explanation(remainders, moduli):
    """CRT dengan penjelasan langkah demi langkah / CRT with step-by-step explanation."""
    n = len(remainders)
    M = 1
    for m in moduli:
        M *= m

    print(f"\n  Sistem kongruensi / System of congruences:")
    for r, m in zip(remainders, moduli):
        print(f"    x ≡ {r} (mod {m})")

    print(f"\n  M = {'×'.join(str(m) for m in moduli)} = {M}")
    print(f"\n  Langkah konstruksi / Construction steps:")

    x = 0
    for i, (r, m) in enumerate(zip(remainders, moduli)):
        Mi = M // m
        gcd, yi, _ = extended_gcd(Mi, m)
        yi = yi % m
        contrib = r * Mi * yi
        print(f"\n  i={i+1}: r={r}, m={m}, M_{i+1}={Mi}")
        print(f"    yi = invers({Mi} mod {m}) = {yi}  (verif: {Mi}×{yi} mod {m} = {(Mi*yi)%m})")
        print(f"    kontribusi: {r} × {Mi} × {yi} = {contrib}")
        x += contrib

    x = x % M
    print(f"\n  x = ({' + '.join(str(r*M//m*(extended_gcd(M//m,m)[1]%m)) for r,m in zip(remainders,moduli))}) mod {M}")
    print(f"  x = {x % M}")

    # Verifikasi / Verify
    print(f"\n  Verifikasi / Verification:")
    for r, m in zip(remainders, moduli):
        check_val = x % m
        ok = check_val == r % m
        print(f"    {x} mod {m} = {check_val} {'= ' + str(r) + ' ✓' if ok else '≠ ' + str(r) + ' ✗'}")

    return x, M


# Contoh 1: Masalah klasik / Classic problem
print("\nContoh 1 / Example 1: Masalah klasik (bilangan 'Sunzi'):")
print("  Cari x sehingga / Find x such that:")
r1, m1 = [2, 3, 2], [3, 5, 7]
sol1, M1 = crt_with_explanation(r1, m1)
print(f"\n  Solusi unik / Unique solution: x ≡ {sol1} (mod {M1})")

# Contoh 2: Penjadwalan / Scheduling
print("\n" + "-"*50)
print("Contoh 2 / Example 2: Masalah Penjadwalan / Scheduling Problem")
print("  3 acara berulang setiap 5, 7, 11 hari (pairwise coprime).")
print("  Acara A dimulai hari ke-1, B hari ke-3, C hari ke-5.")
print("  3 recurring events every 5, 7, 11 days (pairwise coprime).")
print("  Event A starts day 1, B day 3, C day 5.")
print("  (Catatan: CRT memerlukan moduli yang SALING KOPRIMA!)")
print("  (Note: CRT requires PAIRWISE COPRIME moduli!)")

sch_rem, sch_mod = [1, 3, 5], [5, 7, 11]
sol2, M2 = crt(sch_rem, sch_mod)
print(f"\n  Solusi: Hari ke-{sol2} ketiga acara bertepatan secara bersamaan")
print(f"  (Periode / Period = {M2} hari / days)")
# Verifikasi
for r, m, name in zip(sch_rem, sch_mod, ['A','B','C']):
    assert sol2 % m == r % m
    print(f"  Hari {sol2} mod {m} = {sol2 % m} = {r % m} (acara/event {name}) ✓")

# Benchmark: CRT vs brute force
print(f"\nBenchmark CRT vs brute force:")
remainders_bench = [3, 5, 7]
moduli_bench = [7, 11, 13]

t0 = time.perf_counter()
sol_crt, M_bench = crt(remainders_bench, moduli_bench)
t1 = time.perf_counter()
crt_time = (t1 - t0) * 1e6

# Brute force
t0 = time.perf_counter()
for x_brute in range(M_bench):
    if all(x_brute % m == r for r, m in zip(remainders_bench, moduli_bench)):
        sol_brute = x_brute
        break
t1 = time.perf_counter()
brute_time = (t1 - t0) * 1e6

assert sol_crt == sol_brute
print(f"  CRT:         {crt_time:.2f} μs  (O(k) di mana k=jumlah kongruensi)")
print(f"  Brute force: {brute_time:.2f} μs  (O(M) di mana M={M_bench})")
print(f"  CRT menang ~{brute_time/max(crt_time,0.001):.0f}× lebih cepat! / CRT wins ~{brute_time/max(crt_time,0.001):.0f}× faster!")
print(f"  Solusi / Solution: x = {sol_crt} ✓")


# =============================================================================
# RINGKASAN / SUMMARY
# =============================================================================

print("\n" + "=" * 70)
print("RINGKASAN CHALLENGE / CHALLENGE SUMMARY")
print("=" * 70)
print("""
  Challenge 1: Aritmatika Presisi Arbitrer
    → Implementasi BigInt dengan basis 10^9, operasi +, ×, n!
    → BigInt with base 10^9, operations +, ×, n!

  Challenge 2: Parser Ekspresi Matematika
    → Lexer + Recursive Descent Parser dengan precedence climbing
    → Urutan operasi yang benar termasuk right-associative **
    → Lexer + Recursive Descent Parser with correct PEMDAS

  Challenge 3: Varian Euclidean
    → Extended GCD (Bezout's Identity)
    → Binary GCD (Stein's Algorithm) dengan operasi bitwise
    → Invers modular menggunakan Extended GCD
    → Extended GCD, Binary GCD, Modular Inverse

  Challenge 4: Eksponensial Cepat
    → Square-and-multiply: O(log n) vs naif O(n)
    → Modular exponentiation untuk angka sangat besar
    → Fast Exponentiation: O(log n) vs naive O(n)

  Challenge 5: Saringan Eratosthenes
    → Saringan standar O(n log log n)
    → Saringan tersegmen untuk limit besar
    → Prima kembar dan prima Mersenne
    → Standard Sieve + Segmented Sieve, Twin Primes, Mersenne Primes

  Challenge 6: Teorema Sisa Tiongkok
    → CRT: solusi unik untuk sistem kongruensi
    → Aplikasi: penjadwalan, kriptografi
    → CRT: unique solution for system of congruences

  Semua implementasi dari nol dengan kompleksitas yang optimal!
  All implementations from scratch with optimal complexity!
""")
