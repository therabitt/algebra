"""
Challenge: Quadratic & Rational Inequalities  |  Phase 1 — Topic 1.17
"""
import math
print("CHALLENGE 1.17 — PERTIDAKSAMAAN KUADRAT & RASIONAL")

# Challenge 1: General Sign Chart Engine
# KONSEP: Sign chart engine mengotomatisasi pengujian tanda untuk interval yang dibatasi oleh titik-titik kritis.
# LANGKAH:
# 1. Gabungkan dan urutkan semua akar pembilang dan penyebut
# 2. Buat interval dari -∞ hingga +∞ berdasarkan titik kritis
# 3. Pilih titik uji di setiap interval
# 4. Evaluasi tanda fungsi pada titik uji
# 5. Kumpulkan interval yang memenuhi syarat > 0
# KOMPLEKSITAS: O(N log N) untuk sorting, O(N*M) untuk evaluasi dimana M adalah jumlah interval
# IMPLEMENTASIKAN:
print("\n[Ch1] Sign Chart Engine Universal")
def solve_inequality_by_sign_chart(numerator_roots, denominator_roots, strict_denom=True):
    """
    Selesaikan f(x) > 0 menggunakan sign chart.
    Asumsi: setiap faktor (x - r) muncul sekali.
    """
    # TODO: Implementasikan algoritma sign chart
    pass

# Challenge 2: AM-GM Inequality
# KONSEP: Ketidaksamaan AM-GM menyatakan Rata-rata Aritmatika ≥ Rata-rata Geometris.
# LANGKAH:
# 1. Hitung AM = (x₁+...+xₙ)/n
# 2. Hitung GM = (x₁*...*xₙ)^(1/n)
# 3. Verifikasi AM ≥ GM (dengan toleransi error floating point)
# IMPLEMENTASIKAN:
print("\n[Ch2] Ketidaksamaan AM-GM")
def verify_am_gm(pairs):
    # TODO: Implementasikan verifikasi AM-GM untuk array of pairs
    pass

# Challenge 3: Cauchy-Schwarz
# KONSEP: Ketidaksamaan Cauchy-Schwarz membatasi hasil kali titik (dot product) dua vektor.
# LANGKAH:
# 1. Hitung sisi kiri: (Σ aᵢbᵢ)²
# 2. Hitung sisi kanan: (Σ aᵢ²)(Σ bᵢ²)
# 3. Bandingkan LHS ≤ RHS
# IMPLEMENTASIKAN:
print("\n[Ch3] Ketidaksamaan Cauchy-Schwarz")
# TODO: Tulis kode untuk memverifikasi Cauchy-Schwarz pada dua vektor

print("\n[Selesai Challenge 1.17]")
