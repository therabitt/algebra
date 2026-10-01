"""
Exercises: Linear Equations  |  Phase 1 — Topic 1.4
"""
print("LATIHAN 1.4 — PERSAMAAN LINEAR")
print("=" * 50)

# KONSEP:
# Persamaan linear ax + b = c. 
# Jika a != 0, solusi x = (c - b) / a.
# Jika a == 0, maka ada tak terhingga solusi (Infinite) jika b == c, atau tidak ada (None) jika b != c.
# LANGKAH:
# 1. Buat fungsi solve(a, b, c).
# 2. Periksa a. Jika 0, evaluasi b dan c untuk menentukan apakah solusinya tak terhingga atau None.
# 3. Jika bukan 0, kembalikan hasil (c - b) / a.
# IMPLEMENTASIKAN:
def solve(a, b, c):
    # TODO: Tulis algoritma solver dasar
    if a != 0:
        x = (c - b)/a
        return x
    else:
        if b == c:
            return "Infinite"
        else:
            return "None"

## Input nilai variabel
a = float(input("masukkan nilai variabel a: "))
b = float(input("masukkan nilai variabel b: "))
c = float(input("masukkan nilai variabel c: "))

hasil = solve(a, b, c)

print(f"solusi dari {a}x + {b} = {c} adalah: {hasil}")

# Ex 1
print("\n[Ex 1] Selesaikan:")
for a,b,c,label in [(3,7,22,"3x+7=22"),(2,-5,13,"2x-5=13"),
                    (-4,8,-12,"-4x+8=-12"),(1,0,0,"x=0")]:
    # TODO: Panggil fungsi solve() untuk set persamaan di atas dan tampilkan
    pass

# Ex 2
print("\n[Ex 2] Identifikasi jenis (satu solusi/tidak/tak hingga):")
# KONSEP:
# Kasus "a=0" mewakili garis horizontal atau anomali, mengakibatkan 0, 1, atau tak terbatas solusi (degeneracy).
# LANGKAH:
# TODO: Uji dengan parameter berikut dan lihat perilaku solver:
# (5,3,18), (0,7,7), (0,3,9), (2,4,4)
pass

# Ex 3
print("\n[Ex 3] Soal kecepatan-waktu-jarak (d=vt):")
print("  Mobil A kecepatan 60 km/h, mobil B 80 km/h.")
print("  Keduanya start dari tempat sama ke arah sama.")
print("  Kapan B mendahului A sejauh 40 km?")
# KONSEP:
# Jarak = Kecepatan x Waktu (d = v*t).
# Mobil B bergerak lebih cepat dari A sejauh 40 km, maka d_B - d_A = 40.
# 80t - 60t = 40  ->  20t = 40.
# LANGKAH:
# 1. Definisikan kecepatan dan jarak.
# 2. Hitung t berdasarkan perbandingan jarak terhadap selisih kecepatan.
# IMPLEMENTASIKAN:
# TODO: Hitung t, dan tampilkan hasilnya.
pass

# Ex 4 - literal equations
print("\n[Ex 4] Selesaikan persamaan literal:")
print("  F = (9/5)C + 32  untuk C  ->  C = 5(F-32)/9")
# KONSEP:
# Isolasi variabel yang dicari dari persamaan umum dengan aturan aljabar.
# LANGKAH:
# 1. Definisikan array/list dari derajat F yang akan diuji.
# 2. Loop dan aplikasikan formula invers.
# IMPLEMENTASIKAN:
# TODO: Hitung suhu celcius (C) untuk array F = [32, 100, 212, -40] dan cetak hasil
pass

print("\n[Selesai]")
