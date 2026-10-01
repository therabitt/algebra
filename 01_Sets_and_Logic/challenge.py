"""
Challenge: Sets and Logic  |  Phase 1 — Topic 1.14
"""
print("CHALLENGE 1.14 — HIMPUNAN DAN LOGIKA")

# ─── Ch1: Propositional Logic Evaluator ───────────────────────
print("\n[Ch1] Evaluator Logika Proposisional")

# KONSEP:
# Membangun sistem logika (Propositional Logic) menggunakan Object-Oriented Programming (OOP).
# Kelas ini merepresentasikan proposisi (variabel logika) yang dapat digabungkan dengan
# operator logika (AND, OR, NOT, IMPLIES) untuk membentuk proposisi majemuk.

# ALGORITMA:
# 1. Setiap objek `Prop` memiliki nama dan nilai (jika sudah didefinisikan).
# 2. Metode `eval(env)` akan mengembalikan nilainya dari dictionary `env` (environment) jika proposisi itu variabel dasar,
#    atau mengevaluasi closure (fungsi tersimpan) jika proposisi itu majemuk.
# 3. Override operator `__and__` (&), `__or__` (|), dan `__invert__` (~) di Python untuk mengembalikan objek `Prop` baru.
#    Objek baru ini menyimpan `orig_eval` yang mengeksekusi operasi tersebut secara rekursif terhadap `self` dan `other`.

class Prop:
    """Kelas proposisi yang bisa dikombinasikan."""
    def __init__(self, name, value=None):
        self.name = name
        self._value = value

    def eval(self, env=None):
        # TODO: Return nilai jika ada, jika tidak, cari di dictionary env (default False).
        pass

    def __and__(self, other):
        # TODO: Buat objek Prop baru untuk AND (∧), dan isi fungsi eval-nya agar meng-AND-kan hasil dari eval(self) dan eval(other).
        pass

    def __or__(self, other):
        # TODO: Buat objek Prop baru untuk OR (∨), dan isi fungsi eval-nya.
        pass

    def __invert__(self):
        # TODO: Buat objek Prop baru untuk NOT (¬).
        pass

    def implies(self, other):
        # TODO: Buat objek Prop baru untuk Implikasi (→). (Ingat: p→q sama dengan ¬p ∨ q).
        pass

    def __repr__(self): return self.name

# IMPLEMENTASIKAN:
# TODO: Uji kelas di atas dengan membuat proposisi p dan q.
# Buat tabel kebenaran untuk p→q dan kontrapositifnya ¬q→¬p.
pass


# ─── Ch2: SAT Solver (brute force) ────────────────────────────
print("\n[Ch2] SAT Solver — Apakah formula dapat dipenuhi?")

# KONSEP:
# SAT (Satisfiability) Solver bertugas mencari apakah ada setidaknya satu kombinasi nilai variabel
# (Truth Assignment) yang membuat keseluruhan formula logika menjadi True.

# KOMPLEKSITAS:
# Brute-force solver ini mengevaluasi semua 2^n kombinasi nilai kebenaran. Time complexity = O(2^n).
# SAT problem adalah NP-Complete problem.

def sat_solve(formula_fn, variables):
    """
    Brute-force SAT solver: coba semua kombinasi nilai kebenaran.
    formula_fn: fungsi yang menerima dict {var: bool} dan return bool
    variables: list nama variabel
    """
    # LANGKAH:
    # 1. Cari jumlah variabel n.
    # 2. Iterasi i dari 0 hingga 2^n - 1.
    # 3. Dalam setiap iterasi, buat dictionary `env` yang memetakan nama variabel ke True/False berdasarkan bit ke-j dari i.
    # 4. Panggil formula_fn(env). Jika True, tambahkan env ke list `solutions`.
    # 5. Return semua solusi.
    
    # IMPLEMENTASIKAN:
    pass

# TODO: Uji sat_solve() dengan formula: (p ∨ q) ∧ (¬p ∨ r) ∧ (¬q ∨ ¬r)
pass


# ─── Ch3: Cantor's Diagonal Argument (demo) ───────────────────
print("\n[Ch3] Argumen Diagonal Cantor")
print("  Buktikan bahwa bilangan real (0,1) tidak bisa didaftar!")

# KONSEP:
# Argumen Diagonal Georg Cantor membuktikan bahwa himpunan bilangan riil tidak terhitung (uncountable).
# Ini dilakukan dengan asumsi kita bisa mendaftar semua bilangan riil antara (0, 1), 
# lalu membuat satu bilangan baru yang pasti TIDAK ada di daftar tersebut.

# LANGKAH:
# 1. Buat "daftar palsu" yang berisi 10 bilangan acak dengan 20 digit di belakang koma.
# 2. Cetak daftar tersebut.
# 3. Bangun `new_number`: untuk setiap baris i, ambil digit ke-i dari bilangan di baris ke-i.
# 4. Ubah digit tersebut (misalnya tambah 1, lalu mod 10 agar jadi 0-9).
# 5. Karena bilangan baru ini berbeda di digit ke-1 dari bilangan ke-1, berbeda di digit ke-2 dari bilangan ke-2,
#    bilangan ini PASTI belum ada di daftar!
# 6. Cetak `new_number` dan penjelasan singkat.

import random
random.seed(42)

# IMPLEMENTASIKAN:
# TODO: Tulis argumen diagonal sesuai langkah-langkah di atas.
pass

print("\n[Selesai Challenge 1.14]")
