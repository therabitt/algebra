"""
Exercises: Algebraic Expressions  |  Phase 1 — Topic 1.3
"""
print("LATIHAN 1.3 — EKSPRESI ALJABAR")
print("=" * 50)

print("""
[Ex 1] Evaluasi f(x) = 2x^2 + 3x - 5 untuk x = -1, 0, 2, 4
""")
# KONSEP:
# Evaluasi ekspresi polinomial dilakukan dengan mensubstitusi nilai x ke dalam ekspresi.
# LANGKAH:
# 1. Definisikan fungsi f(x) yang mengembalikan 2x^2 + 3x - 5.
# 2. Lakukan perulangan untuk setiap x di dalam [-1, 0, 2, 4].
# 3. Cetak hasil f(x) dari masing-masing x.
# IMPLEMENTASIKAN:
# TODO: Buat fungsi f(x) dan evaluasi nilainya
pass

print("""
[Ex 2] Sederhanakan: 4x^2 - 3x + 7 + 2x^2 + 5x - 9
  Suku x^2: 4+2=6  ->  6x^2
  Suku x  : -3+5=2 ->  2x
  Konst   : 7-9=-2 -> -2
  Hasil: 6x^2 + 2x - 2
""")
# KONSEP:
# Menyederhanakan polinomial berarti menjumlahkan koefisien dari suku-suku yang memiliki pangkat yang sama (like terms).
# LANGKAH:
# 1. Representasikan polinomial sebagai daftar pasangan (derajat, koefisien).
# 2. Gunakan struktur data seperti kamus (dictionary/defaultdict) untuk menyimpan total koefisien tiap derajat.
# 3. Iterasi setiap suku dan tambahkan koefisiennya ke dalam dictionary.
# IMPLEMENTASIKAN:
# TODO: Buat list terms dan gabungkan suku yang sejenis.
pass

print("""
[Ex 3] Kalikan (2x + 5)(x - 3) menggunakan FOIL
  F: 2x*x  = 2x^2
  O: 2x*-3 = -6x
  I: 5*x   = 5x
  L: 5*-3  = -15
  Hasil: 2x^2 - x - 15
""")
# KONSEP:
# FOIL (First, Outer, Inner, Last) digunakan untuk mengalikan dua binomial (ax + b)(cx + d).
# Hasil akhirnya memiliki pola: ac*x^2 + (ad + bc)*x + bd.
# LANGKAH:
# 1. Tetapkan a=2, b=5, c=1, d=-3.
# 2. Hitung koefisien untuk pangkat 2, pangkat 1, dan konstanta menggunakan rumus di atas.
# 3. Opsional: verifikasi dengan modul symPy jika ada (sympy.expand).
# IMPLEMENTASIKAN:
# TODO: Hitung hasil perkalian binomial menggunakan aturan FOIL.
pass

print("""
[Ex 4] Buktikan (a+b)^2 = a^2 + 2ab + b^2 untuk a=7, b=3
""")
# KONSEP:
# Identitas kuadrat binomial: (a+b)^2 identik dengan a^2 + 2ab + b^2 untuk nilai a dan b manapun.
# LANGKAH:
# 1. Tentukan a=7 dan b=3.
# 2. Hitung sisi kiri (LHS) dengan menjumlahkan a dan b lalu mengkuadratkannya.
# 3. Hitung sisi kanan (RHS) menggunakan a^2 + 2ab + b^2.
# 4. Buktikan LHS sama dengan RHS.
# IMPLEMENTASIKAN:
# TODO: Hitung dan bandingkan kedua sisi persamaan (LHS dan RHS).
pass

print("""
[Ex 5] Tentukan domain dari f(x) = (x+1)/(x^2-4)
  Penyebut = 0 jika x^2-4=0 -> x=2 atau x=-2
  Domain: semua real kecuali x=2 dan x=-2
  Notasi: (-inf,-2) U (-2,2) U (2,+inf)
""")
# KONSEP:
# Domain fungsi pecahan adalah semua nilai x yang membuat penyebut TIDAK SAMA DENGAN 0.
# Division by zero akan menghasilkan error.
# LANGKAH:
# 1. Definisikan fungsi safe_f(x) yang memeriksa apakah penyebut (x^2 - 4) hampir mendekati 0.
# 2. Jika penyebut nol, kembalikan 'NaN' (Not a Number).
# 3. Jika tidak, kembalikan hasil (x+1)/(x^2-4).
# 4. Tes fungsi dengan beberapa nilai x termasuk -2 dan 2.
# IMPLEMENTASIKAN:
def safe_f(x):
    # TODO: Cek pembagi, kembalikan hasil pembagian atau float("nan") jika pembagi 0
    pass

# TODO: Uji dengan beberapa nilai x dan cetak.
pass

print("\n[Selesai]")
