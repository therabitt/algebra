"""
Challenge: Linear Inequalities  |  Phase 1 — Topic 1.5
"""
print("CHALLENGE 1.5 — PERTIDAKSAMAAN LINEAR")

# Challenge 1: Linear Programming (intro)
print("\n[Ch1] Linear Programming Sederhana")
print("  Maksimalkan: P = 3x + 5y")
print("  Subject to: x+y<=4, x>=0, y>=0")
print("  Titik-titik ekstrem (corner points):")

# KONSEP:
# Dalam Pemrograman Linear, titik maksimum atau minimum dari suatu fungsi objektif linear 
# di dalam domain terbatas polihedral selalu terjadi pada titik-titik sudut (corner points).
# ALGORITMA:
# 1. Hitung titik persilangan pertidaksamaan (corners: (0,0), (4,0), (0,4)).
# 2. Evaluasi fungsi P di semua corner tersebut.
# 3. Cari dan ambil titik dengan P yang maksimal.

# IMPLEMENTASIKAN:
# corners = [(0,0), (4,0), (0,4)]
# TODO: Uji setiap titik di atas, temukan kombinasi yang memaksimalkan P, dan print.
pass

# Challenge 2: Interval Intersection
print("\n[Ch2] Operasi Interval")

# KONSEP:
# Operasi himpunan interval di bilangan real (contoh: [-2, 5) irisan (1, 8] menjadi (1, 5)).
# ALGORITMA:
# 1. Suatu Interval memiliki batas bawah (a) dan atas (b), serta status penutup kurung siku (inclusive) atau bulat (exclusive).
# 2. Fungsi contains: Mengecek jika titik berada dalam interval tersebut (x >= a/x > a).
# 3. Fungsi intersect: Mempertemukan 2 interval. Batas bawah adalah max(self.a, other.a), 
#    batas atas adalah min(self.b, other.b).
# 4. Jika batas bawah > batas atas, irisannya kosong (return None).
# 5. Penentuan jenis kurung siku pada titik persilangan dilakukan dengan mengecek interval pemilik titik (jika self.a > other.a, ambil jenis kurung self).

class Interval:
    def __init__(self, a, b, left_closed=True, right_closed=True):
        self.a, self.b = a, b
        self.lc, self.rc = left_closed, right_closed

    def __contains__(self, x):
        # TODO: Implementasi logika pengecekan himpunan untuk menentukan apakah x ada di dalamnya.
        pass

    def intersect(self, other):
        # IMPLEMENTASIKAN:
        # TODO: Cari batas irisan (intersection), beserta resolusi logika kurung tertutup.
        pass

    def __repr__(self):
        # TODO: Kembalikan representasi string, contoh "(-2, 5]".
        pass

# TODO: Uji logika dengan mengiris interval I1 = [-2, 5] dan I2 = [1, 8]. Periksa eksistensi titik x=3 dan x=6.
pass

print("\n[Selesai Challenge 1.5]")
