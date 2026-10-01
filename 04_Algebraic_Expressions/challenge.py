"""
Challenge: Algebraic Expressions  |  Phase 1 — Topic 1.3
"""
print("CHALLENGE 1.3 — EKSPRESI ALJABAR")
print("=" * 50)

# Challenge 1: Polynomial Arithmetic dari nol
print("\n[Ch1] Kelas Polynomial dari nol")

# KONSEP:
# Polinomial direpresentasikan menggunakan Object-Oriented Programming, di mana
# list koefisien mewakili derajatnya (indeks = derajat x).
# Kita bisa membangun operator overload (__add__, __mul__) di Python agar dapat
# menjumlahkan dan mengalikan polinomial secara native seperti: p1 + p2.

# ALGORITMA:
# 1. Simpan koefisien pada atribut self.c. Indeks 0 = konstanta, Indeks 1 = koef x, dst. Hapus trailing zeros (derajat tinggi yang nol).
# 2. Metode `__call__(x)` menggunakan "Metode Horner" untuk mengevaluasi polinomial pada x tertentu dengan kompleksitas O(n).
# 3. Penjumlahan `__add__` menjumlahkan list term by term (tambahkan list padding jika derajat berbeda).
# 4. Perkalian `__mul__` melakukan konvolusi/perkalian mendistribusikan semua suku dari dua polinomial (O(n*m)).

class Poly:
    """Polinomial direpresentasikan sebagai list koefisien.
       coeffs[i] = koefisien x^i
       Contoh: 3x^2 + 5x - 1 = Poly([-1, 5, 3])
    """
    def __init__(self, coeffs):
        self.c = list(coeffs)
        # TODO: Hapus angka 0 berlebih di belakang list (leading zeros dalam representasi polinomial)
        pass

    def degree(self): 
        # TODO: Kembalikan derajat polinomial (panjang list - 1)
        pass

    def __call__(self, x):
        # Horner's method: lebih efisien
        # TODO: Implementasi Horner's method: f(x) = (...((a_n*x + a_n-1)*x + a_n-2)...)*x + a_0
        pass

    def __add__(self, other):
        # TODO: Samakan panjang list koefisien menggunakan padding 0, lalu jumlahkan indeks-per-indeks.
        pass

    def __mul__(self, other):
        # TODO: Buat list kosong, lalu loop i dan j untuk mengalikan setiap pasangan suku: result[i+j] += a * b.
        pass

    def __repr__(self):
        # TODO: Cetak dengan format representasi yang bagus (misal "3x^2 + 5x - 1")
        return "Polinomial-Representasi"

# IMPLEMENTASIKAN:
# p1 = Poly([-5, 3, 2])   # 2x^2 + 3x - 5
# p2 = Poly([2, 1])       # x + 2
# Test penjumlahan, perkalian, dan substitusi eval p1(3)
pass


# Challenge 2: Parser ekspresi sederhana
print("\n[Ch2] Evaluator ekspresi string sederhana (safe eval)")
import ast, operator, math

# KONSEP:
# Menggunakan modul `ast` (Abstract Syntax Tree) Python untuk mem-parsing string ke dalam struktur pohon.
# Ini lebih aman dari menggunakan fungsi bawaan `eval()` yang bisa mengeksekusi sembarang kode berbahaya.

# LANGKAH:
# 1. Definisikan mapping `SAFE_OPS` dari tipe node AST ke operasi aman (misal ast.Add -> operator.add).
# 2. Parse expr_str menggunakan ast.parse dengan mode="eval".
# 3. Buat fungsi rekursif `_eval(node)` yang mengevaluasi masing-masing ast.Expression, ast.Constant, dan ast.BinOp.
# 4. Jika ada ast.Name (variabel x/y), cari nilainya dari dictionary variables, error jika tidak ditemukan.

SAFE_OPS = {
    ast.Add: operator.add, ast.Sub: operator.sub,
    ast.Mult: operator.mul, ast.Div: operator.truediv,
    ast.Pow: operator.pow, ast.USub: operator.neg,
}

def safe_eval(expr_str, variables=None):
    """Evaluasi ekspresi matematika string dengan aman."""
    variables = variables or {}
    # tree = ast.parse(expr_str, mode="eval")
    
    # IMPLEMENTASIKAN:
    def _eval(node):
        # TODO: Cek dan return berdasarkan instance node 
        # (ast.Expression, ast.Constant, ast.Name, ast.BinOp, ast.UnaryOp)
        pass
    
    # return _eval(tree)
    pass

# TODO: Uji safe_eval() dengan expression "3*x**2 - 5*x + 2" atau "2*x + 3*y" dengan x=2, y=4.
pass

print("\n[Selesai Challenge 1.3]")
