"""
Challenge: Linear Equations  |  Phase 1 — Topic 1.4
"""
print("CHALLENGE 1.4 — PERSAMAAN LINEAR")

# Challenge: Step-by-step solver dengan output rinci
# KONSEP:
# Memecahkan persamaan string menggunakan modul SymPy secara terprogram (Computer Algebra System).
# Ini membutuhkan parsing dari String ke Expression AST Sympy, dan mengaplikasikan sp.solve.
# ALGORITMA:
# 1. Pisahkan string string berdasarkan "=" menjadi LHS (Left Hand Side) dan RHS (Right Hand Side).
# 2. Gunakan sp.sympify() untuk mengubah teks menjadi ekspresi Sympy.
# 3. Buat persamaan menggunakan sp.Eq(lhs, rhs).
# 4. Cari solusi menggunakan sp.solve(eq, variabel).
# 5. Verifikasi solusi tersebut dengan cara subtitusi (subs) solusi kembali ke dalam LHS dan RHS.

def solve_with_steps(equation_str, var="x"):
    """Solver persamaan linear dengan langkah-langkah ditampilkan."""
    # IMPLEMENTASIKAN:
    # import sympy as sp
    # TODO: Lengkapi fungsi solver
    pass

equations = [
    "3*x + 7 = 22",
    "2*(x - 3) + 5 = x + 8",
    "x/3 + x/4 = 7",
    "0.5*x - 1.5 = 2.5",
]
# TODO: Panggil solver untuk persamaan di atas.
pass

# Mixture problem solver
print("\n[Ch2] Mixture Problem Solver")
# KONSEP:
# Dalam soal Mixture (Campuran), kuantitas bahan yang dilarutkan adalah konsisten:
# Jumlah Larutan_Murni 1 + Jumlah Larutan_Murni 2 = Jumlah Murni Campuran Akhir
# c1*v1 + c2*x = c_target*(v1 + x)
# Tujuan: cari x (volume larutan 2 yang harus dicampur).
# ALGORITMA:
# 1. Isolasi variabel x: x = v1*(c_target - c1) / (c2 - c_target).
# 2. Apabila pembagi (c2 - c_target) bernilai ~0, tidak ada solusi unik (konsentrasi akhir sama dengan salah satu larutan).

def mixture(c1, v1, c2, v2, c_target):
    """
    Berapa banyak larutan 1 (konsentrasi c1) dan larutan 2 (c2)
    yang dicampur untuk mendapatkan c_target?
    """
    # IMPLEMENTASIKAN:
    # TODO: implementasikan pengecekan pembagian dengan nol, dan kembalikan nilai x.
    pass

# TODO: Uji dengan mencampur 100ml konsentrasi 20% dengan suatu larutan konsentrasi 50% 
# untuk membuat campuran konsentrasi akhir 30%.
pass

print("\n[Selesai Challenge 1.4]")
