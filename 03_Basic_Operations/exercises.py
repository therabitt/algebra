"""
=============================================================================
exercises.py — Latihan: Operasi Dasar / Exercises: Basic Operations
=============================================================================
Berisi 12 latihan dengan berbagai tingkat kesulitan.

Cara mengerjakan:
  1. Baca setiap soal
  2. Hitung secara MANUAL (di kertas atau di kepala)
  3. Isi nilai 'student_answer' dengan jawabanmu
  4. Jalankan file untuk cek jawaban!

Tingkat kesulitan:
  [★☆☆] = Mudah    [★★☆] = Sedang    [★★★] = Sulit
=============================================================================
"""

from fractions import Fraction
import math

# KONSEP: Operasi dasar matematika — penjumlahan, pengurangan, perkalian, pembagian,
#         beserta sifat-sifatnya (komutatif, asosiatif, distributif).
# LANGKAH: Untuk setiap soal, ISI student_answer dengan jawabanmu sendiri,
#          lalu jalankan file ini untuk melihat apakah jawabanmu benar.

# ===========================================================================
# HELPER FUNCTIONS (sudah jadi — jangan ubah)
# ===========================================================================

def check(problem_num: str, student_answer, correct_answer, tolerance=0):
    """Memeriksa jawaban student."""
    if student_answer is None:
        print(f"  [{problem_num}] ⏳ Belum dijawab — isi student_answer!")
        return False
    if tolerance > 0:
        try:
            correct = abs(float(student_answer) - float(correct_answer)) <= tolerance
        except:
            correct = student_answer == correct_answer
    else:
        correct = student_answer == correct_answer
    status = "✓ BENAR!" if correct else f"✗ SALAH. (Jawaban: {correct_answer})"
    print(f"  [{problem_num}] {status}")
    return correct

def section(title: str):
    print(f"\n{'='*65}")
    print(f"  {title}")
    print(f"{'='*65}")

def hint(text: str):
    print(f"  💡 PETUNJUK: {text}")


# ===========================================================================
# SOAL 1 [★☆☆]: Verifikasi Sifat Komutatif dan Asosiatif
# ===========================================================================
# KONSEP: Komutatif: a+b=b+a (penjumlahan). Pengurangan TIDAK komutatif!
#         Asosiatif: (a+b)+c = a+(b+c). Pengurangan TIDAK asosiatif!
# LANGKAH:
#   1. Untuk a=15, b=23, c=7:
#   (a) Hitung a+b dan b+a — apakah sama?
#   (b) Hitung (a+b)+c dan a+(b+c) — apakah sama?
#   (c) Hitung a-b dan b-a — apakah sama?
#   (d) Hitung (a-b)-c dan a-(b-c) — apakah sama?

section("SOAL 1 [★☆☆]: Verifikasi Sifat Komutatif dan Asosiatif")
a, b, c = 15, 23, 7
print(f"\n  a={a}, b={b}, c={c}")
hint("Sifat komutatif: a ○ b = b ○ a. Pengurangan TIDAK komutatif.")

# TODO: Hitung secara manual lalu isi True/False di bawah
student_answer_1a = None  # apakah a+b == b+a?  True atau False
student_answer_1b = None  # apakah (a+b)+c == a+(b+c)?  True atau False
student_answer_1c = None  # apakah a-b == b-a?  True atau False
student_answer_1d = None  # apakah (a-b)-c == a-(b-c)?  True atau False

check("1a", student_answer_1a, True)
check("1b", student_answer_1b, True)
check("1c", student_answer_1c, False)
check("1d", student_answer_1d, False)


# ===========================================================================
# SOAL 2 [★☆☆]: Urutan Operasi (PEMDAS)
# ===========================================================================
# KONSEP: PEMDAS = Parentheses, Exponent, Multiply/Divide, Add/Subtract
#         ** bersifat kanan-asosiatif: 2**2**3 = 2**(2**3) = 2**8 = 256
#         / bersifat kiri-asosiatif:  100/10/2 = (100/10)/2 = 5
# LANGKAH: Hitung MANUAL masing-masing ekspresi, jangan ketik langsung ke Python!

section("SOAL 2 [★☆☆]: Urutan Operasi / Order of Operations")
hint("Ingat PEMDAS. ** adalah kanan-asosiatif, / adalah kiri-asosiatif.")
print("""
  Hitung ekspresi berikut MANUAL (jangan langsung eval di Python):
  (a) 3 + 4 * 2          = ?
  (b) (3 + 4) * 2        = ?
  (c) 2 ** 3 + 1         = ?
  (d) 10 - 2 * 3 + 1     = ?
  (e) 2 ** 2 ** 3        = ?   ← hati-hati! kanan-asosiatif
  (f) 100 / 10 / 2       = ?
""")

# TODO: Isi jawaban di bawah
student_answer_2a = None   # 3 + 4 * 2
student_answer_2b = None   # (3 + 4) * 2
student_answer_2c = None   # 2 ** 3 + 1
student_answer_2d = None   # 10 - 2 * 3 + 1
student_answer_2e = None   # 2 ** 2 ** 3
student_answer_2f = None   # 100 / 10 / 2

check("2a", student_answer_2a, 11)
check("2b", student_answer_2b, 14)
check("2c", student_answer_2c, 9)
check("2d", student_answer_2d, 5)
check("2e", student_answer_2e, 256)
check("2f", student_answer_2f, 5.0)


# ===========================================================================
# SOAL 3 [★★☆]: FPB / GCD dengan Algoritma Euclidean
# ===========================================================================
# KONSEP: GCD(a,b) = GCD(b, a mod b). Terus sampai b=0.
#         Sisa terakhir sebelum b=0 adalah GCD.
# LANGKAH: Jalankan Euclidean Algorithm secara manual:
#   GCD(56, 98): 98=56×1+42 → GCD(56,42) → 56=42×1+14 → GCD(42,14) → 42=14×3+0 → GCD=14

section("SOAL 3 [★★☆]: FPB / GCD dengan Algoritma Euclidean")
hint("GCD(a,b) = GCD(b, a mod b). Terus sampai sisa = 0.")
print("""
  Hitung GCD secara manual menggunakan Algoritma Euclidean:
  (a) GCD(56, 98)
  (b) GCD(144, 89)   ← bilangan Fibonacci! (kasus tersulit)
  (c) GCD(1071, 462)
  (d) GCD(100, 75)
""")

# TODO: Implementasikan fungsi gcd_euclidean(a, b) dan hitung jawabannya
def gcd_euclidean(a, b):
    """Algoritma Euclidean untuk GCD. TODO: implementasikan!"""
    # TODO: while b != 0: a, b = b, a % b; return a
    pass

student_answer_3a = gcd_euclidean(56, 98)    # atau isi langsung dengan angka
student_answer_3b = gcd_euclidean(144, 89)
student_answer_3c = gcd_euclidean(1071, 462)
student_answer_3d = gcd_euclidean(100, 75)

check("3a", student_answer_3a, 14)
check("3b", student_answer_3b, 1)
check("3c", student_answer_3c, 21)
check("3d", student_answer_3d, 25)


# ===========================================================================
# SOAL 4 [★★☆]: Aritmatika Modular
# ===========================================================================
# KONSEP: a mod n adalah sisa pembagian a dengan n.
#         Hari dalam seminggu: mod 7. Jam: mod 24.
# LANGKAH untuk (a): (index_hari_awal + jumlah_hari) mod 7
#   Senin=0, Selasa=1, ..., Minggu=6

section("SOAL 4 [★★☆]: Aritmatika Modular")
hint("Hari mod 7 (Senin=0,...,Minggu=6). Jam mod 24.")
days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
print(f"""
  (a) Hari ini Senin. Hari apa 100 hari lagi?
  (b) Pukul 09:00 sekarang. Pukul berapa 250 jam lagi?
  (c) (2024 × 365 + 100) mod 7 = ?
  (d) Apakah 1234567 habis dibagi 9? (Gunakan aturan digit sum)
""")

# TODO: Hitung dan isi jawaban
student_answer_4a = None  # index hari (0=Senin,...,6=Minggu)
student_answer_4b = None  # jam (0-23)
student_answer_4c = None  # nilai mod 7
student_answer_4d = None  # True atau False (habis dibagi 9?)

check("4a", student_answer_4a, (0+100)%7)       # 1 = Selasa
check("4b", student_answer_4b, (9+250)%24)      # 19
check("4c", student_answer_4c, (2024*365+100)%7)
check("4d", student_answer_4d, 1234567 % 9 == 0)


# ===========================================================================
# SOAL 5 [★★☆]: Hukum Perpangkatan
# ===========================================================================
# KONSEP: a^m × a^n = a^(m+n),  a^m / a^n = a^(m-n),
#         (a^m)^n = a^(m×n),    a^0 = 1 (a≠0),  a^(-n) = 1/a^n
# LANGKAH: Sederhanakan setiap ekspresi menggunakan aturan perpangkatan

section("SOAL 5 [★★☆]: Hukum Perpangkatan")
hint("a^m × a^n = a^(m+n), (a^m)^n = a^(mn), a^(-n) = 1/a^n")
print("""
  Sederhanakan (hitung nilai numeriknya):
  (a) 2^5 × 2^3       = 2^? = ?
  (b) 3^7 / 3^4       = 3^? = ?
  (c) (2^3)^4         = 2^? = ?
  (d) 5^0             = ?
  (e) 2^(-3)          = 1/? = ?
  (f) (2×3)^4         = ?
""")

# TODO: Isi jawaban
student_answer_5a = None  # nilai dari 2^5 × 2^3
student_answer_5b = None  # nilai dari 3^7 / 3^4
student_answer_5c = None  # nilai dari (2^3)^4
student_answer_5d = None  # nilai dari 5^0
student_answer_5e = None  # nilai dari 2^(-3) sebagai float
student_answer_5f = None  # nilai dari (2×3)^4

check("5a", student_answer_5a, 2**8)     # 256
check("5b", student_answer_5b, 3**3)     # 27
check("5c", student_answer_5c, 2**12)    # 4096
check("5d", student_answer_5d, 1)
check("5e", student_answer_5e, 1/8, tolerance=1e-9)
check("5f", student_answer_5f, 6**4)     # 1296


# ===========================================================================
# SOAL 6 [★★☆]: Faktorisasi Prima
# ===========================================================================
# KONSEP: Setiap bilangan bulat > 1 dapat difaktorkan unik menjadi bilangan prima.
#         Trial division: coba semua prima p ≤ √n.
# LANGKAH untuk prime_factors(n):
#   1. Mulai dengan d=2
#   2. Selama d*d <= n: jika n%d==0: tambahkan d, n/=d; else: d+=1
#   3. Jika n>1: tambahkan n (prima terakhir)

section("SOAL 6 [★★☆]: Faktorisasi Prima")
hint("Trial division: coba dibagi p=2,3,5,... sampai p^2 > n.")

def prime_factors(n):
    """
    Faktorisasi prima dari n.
    Return list faktor prima (boleh duplikat, misal 12 → [2,2,3]).
    """
    # TODO: implementasikan trial division
    # Pseudocode:
    #   factors = []
    #   d = 2
    #   while d*d <= n: ...
    #   return factors
    pass

print("""
  Faktorkan bilangan berikut:
  (a) 84      = ? × ? × ? × ?
  (b) 360     = ?
  (c) 1001    = ?
  (d) 1024    = ?
  (e) 9999    = ?
""")
# TODO: implementasikan prime_factors di atas, lalu cek dengan check()
check("6a", prime_factors(84),   [2, 2, 3, 7])
check("6b", prime_factors(360),  [2, 2, 2, 3, 3, 5])
check("6c", prime_factors(1001), [7, 11, 13])
check("6d", prime_factors(1024), [2]*10)
check("6e", prime_factors(9999), [3, 3, 11, 101])


# ===========================================================================
# SOAL 7 [★★☆]: Masalah Kata (Word Problems)
# ===========================================================================
# KONSEP: Terjemahkan masalah nyata ke ekspresi matematika, lalu hitung.
# LANGKAH: Identifikasi apa yang diketahui, apa yang dicari, lalu susun persamaan.

section("SOAL 7 [★★☆]: Masalah Kata")
print("""
  (a) Toko diskon: harga asli Rp 150.000, diskon 30%. Harga akhir?
  (b) Keuntungan: beli 80, jual 100. Persentase keuntungan?
  (c) Campuran: 2L larutan 30% + 3L larutan 50%. Konsentrasi akhir?
  (d) Kecepatan: 360 km dalam 4.5 jam. Kecepatan rata-rata?
  (e) Bunga: Rp 1.000.000, bunga 5%/tahun, 3 tahun (bunga majemuk). Nilai akhir?
""")
hint("Bunga majemuk: P × (1 + r)^t. Campuran: (V1×c1 + V2×c2) / (V1+V2).")

# TODO: Hitung dan isi jawaban
student_answer_7a = None  # harga akhir dalam Rupiah
student_answer_7b = None  # persentase keuntungan (contoh: 25.0 untuk 25%)
student_answer_7c = None  # konsentrasi akhir dalam persen (contoh: 42.0)
student_answer_7d = None  # kecepatan dalam km/jam
student_answer_7e = None  # nilai akhir dalam Rupiah (bulatkan 2 desimal)

check("7a", student_answer_7a, 105000)
check("7b", student_answer_7b, 25.0, tolerance=0.01)
check("7c", student_answer_7c, 42.0, tolerance=0.01)
check("7d", student_answer_7d, 80.0, tolerance=0.01)
check("7e", student_answer_7e, round(1000000 * (1.05)**3, 2), tolerance=1)


# ===========================================================================
# SOAL 8 [★☆☆]: Sifat Bilangan Negatif
# ===========================================================================
# KONSEP: (-a)(-b) = ab (min×min=plus), (-a)(b) = -ab (min×plus=min)
# LANGKAH: Hitung setiap ekspresi manual

section("SOAL 8 [★☆☆]: Sifat Bilangan Negatif")
print("""
  Hitung:
  (a) -5 + (-3)      = ?
  (b) -8 - (-3)      = ?
  (c) (-4) × (-7)    = ?
  (d) (-36) ÷ 6      = ?
  (e) -2^4            = ?     ← hati-hati! bukan (-2)^4
  (f) (-2)^4          = ?
""")
hint("−2^4 = −(2^4) = −16. Tapi (−2)^4 = +16.")

student_answer_8a = None
student_answer_8b = None
student_answer_8c = None
student_answer_8d = None
student_answer_8e = None
student_answer_8f = None

check("8a", student_answer_8a, -8)
check("8b", student_answer_8b, -5)
check("8c", student_answer_8c, 28)
check("8d", student_answer_8d, -6)
check("8e", student_answer_8e, -16)
check("8f", student_answer_8f, 16)


# ===========================================================================
# SOAL 9 [★★☆]: Sifat Distributif
# ===========================================================================
# KONSEP: a(b+c) = ab + ac. Berguna untuk menyederhanakan ekspresi.
# LANGKAH: Terapkan distribusi ke luar kurung, lalu sederhanakan

section("SOAL 9 [★★☆]: Sifat Distributif")
hint("a(b+c) = ab + ac  dan  (a+b)(c+d) = ac + ad + bc + bd")
print("""
  Sederhanakan (hitung nilai akhirnya):
  (a) 7 × (100 + 3)       = ?   ← gunakan distribusi
  (b) 15 × (20 - 2)       = ?
  (c) (a+b)^2 untuk a=3, b=4  = ?   ← a^2+2ab+b^2
  (d) (a+b)(a-b) untuk a=7, b=3 = ?  ← a^2-b^2
  (e) 3×(2+5) - 2×(4-1)   = ?
""")

student_answer_9a = None
student_answer_9b = None
student_answer_9c = None
student_answer_9d = None
student_answer_9e = None

check("9a", student_answer_9a, 7*(103))    # 721
check("9b", student_answer_9b, 15*(18))    # 270
a, b = 3, 4
check("9c", student_answer_9c, (a+b)**2)   # 49
a, b = 7, 3
check("9d", student_answer_9d, a**2-b**2)  # 40
check("9e", student_answer_9e, 3*7 - 2*3)  # 15


# ===========================================================================
# SOAL 10 [★★☆]: Properti Kesamaan dan Ketidaksamaan
# ===========================================================================
# KONSEP: Ketidaksamaan berbalik arah saat dikali/dibagi bilangan NEGATIF!
# LANGKAH: Jika mengalikan/membagi dengan negatif, balik tanda < menjadi >

section("SOAL 10 [★★☆]: Kesamaan & Ketidaksamaan")
hint("Hati-hati: mengalikan dua sisi dengan NEGATIF → tanda < menjadi >!")
print("""
  Untuk setiap pernyataan, jawab True atau False:
  (a) Jika a = b, apakah a + 5 = b + 5?
  (b) Jika a > b, apakah a + 5 > b + 5?
  (c) Jika a > b, apakah -a > -b?    ← HATI-HATI!
  (d) Jika a > b dan a,b > 0, apakah a^2 > b^2?
  (e) Jika a > b > 0, apakah 1/a < 1/b?
""")

student_answer_10a = None  # True atau False
student_answer_10b = None
student_answer_10c = None  # ← ini jebakan!
student_answer_10d = None
student_answer_10e = None

check("10a", student_answer_10a, True)
check("10b", student_answer_10b, True)
check("10c", student_answer_10c, False)  # -a < -b (tanda berbalik!)
check("10d", student_answer_10d, True)
check("10e", student_answer_10e, True)


# ===========================================================================
# SOAL 11 [★★☆]: Nilai Mutlak
# ===========================================================================
# KONSEP: |x| = x jika x ≥ 0, -x jika x < 0.
#         |a + b| ≤ |a| + |b|  (triangle inequality)
# LANGKAH: Hitung |x| dengan mengingat: hasilnya selalu ≥ 0

section("SOAL 11 [★★☆]: Nilai Mutlak")
hint("|x| = jarak dari 0 di garis bilangan. Selalu ≥ 0.")
print("""
  Hitung:
  (a) |-7|              = ?
  (b) |3 - 8|           = ?
  (c) |(-4) × 5|        = ?
  (d) |-3| + |4|        = ?
  (e) |3 + 4| vs |3| + |4|  → apakah |a+b| ≤ |a|+|b| berlaku?
  (f) |-3 + 4| vs |-3| + |4| → cek lagi triangle inequality
""")

student_answer_11a = None
student_answer_11b = None
student_answer_11c = None
student_answer_11d = None
student_answer_11e = None  # True jika |3+4| ≤ |3|+|4|
student_answer_11f = None  # True jika |-3+4| ≤ |-3|+|4|

check("11a", student_answer_11a, 7)
check("11b", student_answer_11b, 5)
check("11c", student_answer_11c, 20)
check("11d", student_answer_11d, 7)
check("11e", student_answer_11e, True)
check("11f", student_answer_11f, True)


# ===========================================================================
# SOAL 12 [★★★]: Tantangan Integrasi
# ===========================================================================
# KONSEP: Gabungan GCD, modular arithmetic, dan pola bilangan prima.
# LANGKAH: Implementasikan setiap fungsi dari nol menggunakan konsep yang sudah dipelajari.

section("SOAL 12 [★★★]: Tantangan Integrasi")
print("""
  Tantangan: Implementasikan SEMUA fungsi di bawah dari nol!
""")

def is_prime(n):
    """Cek apakah n bilangan prima. TODO: implementasikan!"""
    # LANGKAH:
    #   1. Jika n < 2: return False
    #   2. Jika n == 2: return True
    #   3. Jika n % 2 == 0: return False
    #   4. Cek semua ganjil d dari 3 sampai sqrt(n): jika n%d==0: return False
    #   5. return True
    pass

def count_primes_up_to(limit):
    """Hitung banyaknya prima ≤ limit. TODO: implementasikan!"""
    # LANGKAH: gunakan is_prime untuk setiap angka dari 2 sampai limit
    pass

def sum_of_prime_factors(n):
    """Jumlah faktor prima unik dari n. TODO: implementasikan!"""
    # LANGKAH: cari faktor prima unik (gunakan prime_factors dari soal 6),
    #          lalu jumlahkan
    pass

def lcm(a, b):
    """LCM(a,b) = a*b / GCD(a,b). TODO: implementasikan!"""
    # LANGKAH: gunakan gcd_euclidean dari soal 3
    pass

# TODO: implementasikan semua fungsi di atas, lalu check akan otomatis berjalan
print("  (a) is_prime untuk 97, 100, 1, 2, 17")
check("12a1", is_prime(97),  True)
check("12a2", is_prime(100), False)
check("12a3", is_prime(1),   False)
check("12a4", is_prime(2),   True)
check("12a5", is_prime(17),  True)

print("  (b) Banyak prima ≤ 100")
check("12b", count_primes_up_to(100), 25)

print("  (c) Jumlah faktor prima unik dari 60")
check("12c", sum_of_prime_factors(60), 2+3+5)   # faktor prima 60: 2,3,5

print("  (d) LCM(12, 18)")
check("12d", lcm(12, 18), 36)

print("  (e) LCM(a,b) × GCD(a,b) = a × b  → cek untuk (24, 36)")
g = gcd_euclidean(24, 36) if gcd_euclidean(24, 36) is not None else None
l = lcm(24, 36) if lcm(24, 36) is not None else None
if g is not None and l is not None:
    check("12e", g * l, 24 * 36)
else:
    print("  [12e] ⏳ Implementasikan gcd_euclidean dan lcm terlebih dahulu!")


print("\n" + "="*65)
print("  SELESAI! Implementasikan semua fungsi yang masih 'pass'")
print("  lalu jalankan ulang file ini untuk cek semua jawabanmu.")
print("="*65)
