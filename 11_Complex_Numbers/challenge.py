"""
Challenge: Complex Numbers  |  Phase 1 — Topic 1.18
"""
import math, cmath
print("CHALLENGE 1.18 — BILANGAN KOMPLEKS")

# Challenge 1: Implement Complex class from scratch
# KONSEP: Membangun kelas bilangan kompleks dari nol membantu memahami cara kerja operasi bilangan kompleks secara mendalam.
# LANGKAH:
# 1. Implementasikan __init__, __add__, __mul__, __truediv__ untuk operasi dasar (hitung secara manual rumus a+bi)
# 2. Implementasikan conjugate, modulus, argument (gunakan math.atan2)
# 3. Implementasikan power dan nth_roots menggunakan Teorema De Moivre (gunakan bentuk polar)
# IMPLEMENTASIKAN:
print("\n[Ch1] Kelas Bilangan Kompleks dari Nol")

class MyComplex:
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    # TODO: Implementasikan operator-operator dan fungsi matematika
    pass

# Challenge 2: Fourier Series Preview
# KONSEP: Deret Fourier mendekati fungsi periodik dengan penjumlahan fungsi sinus dan kosinus. Bilangan kompleks sering digunakan untuk menyederhanakan perhitungan Fourier.
# LANGKAH:
# 1. Buat iterasi penjumlahan harmonik ganjil (2k-1)
# 2. Evaluasi deret Fourier untuk sebuah titik t pada gelombang kotak
# 3. Bandingkan hasil Fourier (aproksimasi) dengan nilai ideal (1 atau -1)
# IMPLEMENTASIKAN:
print("\n[Ch2] Preview Fourier Series dengan Bilangan Kompleks")
print("  Kita hitung beberapa koefisien untuk gelombang kotak")

def square_wave_fourier(t, T=1.0, n_terms=5):
    """
    Aproksimasi gelombang kotak dengan deret Fourier.
    f(t) = (4/π) Σ sin(2π(2k-1)t/T) / (2k-1)  untuk k=1,2,...
    """
    # TODO: Hitung hasil fungsi di titik t dengan n_terms
    pass

print("\n[Selesai Challenge 1.18]")
