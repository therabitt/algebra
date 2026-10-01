"""
Exercises: Sets and Logic  |  Phase 1 — Topic 1.14
"""
print("LATIHAN 1.14 — HIMPUNAN DAN LOGIKA")
print("=" * 50)

A = {1,2,3,4,5}; B = {3,4,5,6,7}; C = {5,6,7,8}; U = set(range(1,11))

# Ex 1: Set operations
print("\n[Ex 1] Hitung operasi himpunan A={1..5}, B={3..7}:")
# KONSEP:
# Operasi himpunan meliputi gabungan (∪), irisan (∩), selisih (-), selisih simetris (△), dan komplemen (ᶜ).
# LANGKAH:
# 1. Gunakan operator bawaan Python untuk set: | (gabungan), & (irisan), - (selisih), ^ (selisih simetris).
# 2. Untuk komplemen Aᶜ, kurangi semesta U dengan A (U - A).
# 3. Urutkan hasil menggunakan sorted() sebelum dicetak.
# IMPLEMENTASIKAN:
# TODO: Buat daftar operasi himpunan dan cetak hasilnya.
pass

# Ex 2: Venn problems
print("\n[Ex 2] Dari 40 siswa: 25 suka Matematika (M), 18 suka Fisika (F)")
print("  10 suka keduanya. Berapa yang suka keduanya? Hanya M? Hanya F? Tidak keduanya?")
# KONSEP:
# Prinsip Inklusi-Eksklusi: |M ∪ F| = |M| + |F| - |M ∩ F|. 
# LANGKAH:
# 1. Tentukan jumlah siswa yang hanya suka M dengan mengurangi total M dengan yang suka keduanya.
# 2. Lakukan hal yang sama untuk F.
# 3. Hitung siswa yang tidak suka keduanya dengan mengurangi total siswa dengan gabungan M dan F.
# IMPLEMENTASIKAN:
# TODO: Hitung only_M, only_F, dan neither, lalu cetak nilainya.
pass
# Jawaban: Hanya M: 15, Hanya F: 8, Keduanya: 10, Tidak keduanya: 7

# Ex 3: Power set
print("\n[Ex 3] Himpunan kuasa dari S = {a, b, c}")
# KONSEP:
# Himpunan kuasa (Power set) adalah himpunan yang berisi semua subset dari himpunan S.
# Jumlah elemen dalam himpunan kuasa adalah 2^n, di mana n adalah jumlah elemen S.
# LANGKAH:
# 1. Ubah S menjadi list untuk bisa diindeks.
# 2. Lakukan iterasi dari 0 hingga 2^n - 1.
# 3. Gunakan bitwise AND untuk menentukan elemen mana yang masuk ke dalam subset.
# IMPLEMENTASIKAN:
def power_set(s):
    # TODO: Kembalikan daftar semua subset dari s
    pass

S = {"a","b","c"}
# ps = power_set(S)
# print hasilnya

# Ex 4: Truth tables
print("\n[Ex 4] Tentukan nilai kebenaran:")
# KONSEP:
# Operasi logika: Implikasi (p→q) ekuivalen dengan (¬p ∨ q), Biimplikasi (p↔q) ekuivalen dengan p == q.
# LANGKAH:
# 1. Definisikan fungsi lambda untuk masing-masing proposisi logika.
# 2. Evaluasi fungsi dengan argumen kebenaran (True/False) yang diberikan.
# IMPLEMENTASIKAN:
# TODO: Buat list test cases yang menguji implikasi, biimplikasi, dan operasi logika gabungan, lalu cetak hasilnya.
pass

# Ex 5: De Morgan
print("\n[Ex 5] Verifikasi Hukum De Morgan dengan contoh konkret")
A5 = {1,2,3,4}; B5 = {3,4,5,6}; U5 = set(range(1,8))
# KONSEP:
# Hukum De Morgan: (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ dan (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
# LANGKAH:
# 1. Hitung sisi kiri (LHS): U5 - (A5 | B5).
# 2. Hitung sisi kanan (RHS): (U5 - A5) & (U5 - B5).
# 3. Bandingkan LHS dan RHS, lalu lakukan hal yang sama untuk varian irisan.
# IMPLEMENTASIKAN:
# TODO: Hitung dan bandingkan kedua sisi untuk membuktikan Hukum De Morgan.
pass

# Ex 6: Proof by induction
print("\n[Ex 6] Induksi Matematika: buktikan Σk = n(n+1)/2")
# KONSEP:
# Menjumlahkan deret aritmetika k dari 1 hingga n sama dengan n(n+1)/2.
# LANGKAH:
# 1. Buat fungsi verify_sum_formula(n) yang menghitung jumlah manual dari 1 ke n.
# 2. Hitung juga menggunakan rumus n*(n+1)//2.
# 3. Kembalikan kedua nilai tersebut beserta boolean apakah mereka sama.
# IMPLEMENTASIKAN:
def verify_sum_formula(n):
    # TODO: Hitung cara langsung dan formula, bandingkan, dan return (langsung, formula, sama_kah)
    pass

# TODO: Iterasi dari n=1 hingga 10 dan panggil fungsi verifikasi.
pass

print("\n[Selesai]")
