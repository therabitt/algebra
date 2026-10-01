"""
Challenge: Absolute Value  |  Phase 1 — Topic 1.15
"""
import math
print("CHALLENGE 1.15 — NILAI MUTLAK")

# ─── Ch1: Norma L1, L2, L-inf ────────────────────────────────
print("\n[Ch1] Berbagai Norma (Generalisasi Nilai Mutlak)")

# KONSEP:
# Norma P (Lp-norm) adalah generalisasi dari jarak/nilai mutlak ke vektor banyak dimensi.
# Rumus: Lp = (Σ|x_i|^p)^(1/p)
# - L1 (Manhattan norm) adalah jumlah absolut (p=1).
# - L2 (Euclidean norm) adalah jarak garis lurus biasa (p=2).
# - L-infinity (Chebyshev norm) adalah nilai absolut maksimum elemen saat p mendekati tak terhingga.
# Sifat penting: L-inf <= L2 <= L1 untuk sembarang vektor konstan.

# LANGKAH:
# 1. Definisikan fungsi lp_norm(v, p)
# 2. Jika p == float("inf"), return nilai mutlak terbesar dari seluruh elemen vektor.
# 3. Jika bukan, kalkulasikan rumus p-norm menggunakan sum().
# IMPLEMENTASIKAN:
def lp_norm(v, p):
    # TODO: Hitung p-norm dari vektor v
    pass

# TODO: Uji lp_norm untuk [3,4], hitung L1, L2, Linf. Buktikan Linf <= L2 <= L1
pass

# ─── Ch2: Taxicab / Manhattan Distance ───────────────────────
print("\n[Ch2] Jarak Taksi (Taxicab / Manhattan Geometry)")
print("  d_taxi(P,Q) = |x1-x2| + |y1-y2|")
print("  Ini adalah L1 norm dari selisih koordinat")

# KONSEP:
# Manhattan Distance memodelkan jarak di kota grid (seperti taksi di Manhattan) 
# yang hanya boleh berjalan secara ortogonal. 
# Secara definisi, jarak Euclidean akan selalu LEBIH KECIL atau sama dengan jarak Manhattan.

# LANGKAH:
# 1. Definisikan fungsi taxi_dist() sebagai jumlahan selisih absolut koordinat.
# 2. Definisikan fungsi eucl_dist() sebagai akar dari jumlahan selisih kuadrat koordinat.
# IMPLEMENTASIKAN:
def taxi_dist(P, Q):
    # TODO: Return jarak Manhattan antara titik koordinat P dan Q
    pass

def eucl_dist(P, Q):
    # TODO: Return jarak Euclidean antara titik P dan Q
    pass

# TODO: Bandingkan taxi_dist dan eucl_dist untuk pasangan titik, e.g., P=(0,0) Q=(3,4).
pass


# ─── Ch3: L1 Minimization (Median is L1-optimal) ─────────────
print("\n[Ch3] L1 Minimization — Mengapa Median Meminimalkan Σ|x-m|?")

# KONSEP:
# Dalam statistik:
# - Nilai yang meminimalkan "L1 loss" (jumlah total error mutlak Σ|x - m|) adalah MEDIAN.
# - Nilai yang meminimalkan "L2 loss" (jumlah total error kuadrat Σ(x - m)^2) adalah MEAN (rata-rata).

# LANGKAH:
# 1. Siapkan sebuah data, contoh: [1, 3, 7, 8, 10, 15, 20]. Cari Mean dan Median-nya.
# 2. Buat fungsi l1_cost(data, m) yang menjumlahkan error abs.
# 3. Buat fungsi l2_cost(data, m) yang menjumlahkan error kuadrat.
# 4. Cetak cost untuk Median dan Mean di fungsi L1 dan fungsi L2, bandingkan hasilnya.
# 5. Opsional: Lakukan Grid Search untuk cost L1 terkecil dan buktikan titik optimum adalah saat m = median.

data = [1, 3, 7, 8, 10, 15, 20]

# IMPLEMENTASIKAN:
def l1_cost(data, m):
    pass

def l2_cost(data, m):
    pass

# TODO: Hitung Mean dan Median dari data, lalu cetak nilai l1_cost dan l2_cost-nya.
# Buktikan bahwa L1(median) < L1(mean) dan L2(mean) < L2(median).
pass

print("\n[Selesai Challenge 1.15]")
