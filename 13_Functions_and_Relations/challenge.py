"""
Challenge: Functions and Relations  |  Phase 1 — Topic 1.8
"""
import math
print("CHALLENGE 1.8 — FUNGSI DAN RELASI")

# Challenge 1: Function class
# KONSEP: Membuat kelas yang merepresentasikan fungsi matematika yang dapat dikomposisi dan dicari invers numeriknya.
# LANGKAH:
# 1. Definisikan metode __call__ agar instance bisa dipanggil seperti fungsi biasa
# 2. Definisikan compose() yang mengembalikan objek Function baru yang mengeksekusi f(g(x))
# 3. Implementasikan inverse_approx menggunakan metode Bisection untuk mencari x dimana f(x) = y
# IMPLEMENTASIKAN:
print("\n[Ch1] Kelas Function dengan komposisi dan invers")

class Function:
    def __init__(self, fn, name="f"):
        self.fn = fn
        self.name = name
    
    # TODO: Implementasikan __call__, compose, dan inverse_approx (Bisection)
    pass

# Challenge 2: Fixed Point Iteration
# KONSEP: Iterasi titik tetap (Fixed Point Iteration) mencari nilai x sedemikian rupa sehingga x = g(x).
# LANGKAH:
# 1. Mulai dengan tebakan awal x0
# 2. Hitung x_new = g(x)
# 3. Jika selisih |x_new - x| < toleransi, kembalikan x_new
# 4. Jika tidak, update x = x_new dan ulangi hingga max_iter
# IMPLEMENTASIKAN:
print("\n[Ch2] Fixed Point Iteration: x = g(x)")
def fixed_point(g, x0, tol=1e-8, max_iter=200):
    # TODO: Implementasikan algoritma fixed point iteration
    pass

print("\n[Selesai Challenge 1.8]")
