"""
Module  : Bukti √2 Irasional (Proof that √2 is Irrational)
Phase   : 1 - Algebra
Topic   : 1.1 Number Systems (Sistem Bilangan)
File    : proof_sqrt2_irrational.py
Metode  : Proof by Contradiction (Reductio ad Absurdum)

Deskripsi:
    File khusus untuk membuktikan secara matematis dan komputasional bahwa
    √2 adalah bilangan irasional (tidak dapat dinyatakan sebagai p/q).
    
    Mengimplementasikan:
    1. Rekonstruksi formal langkah demi langkah bukti kontradiksi klasik (Pithagoras/Euklides).
    2. Verifikasi empiris / exhaustive check pada pasangan bilangan bulat (p, q).
    3. Pembuktian kontradiksi via Teorema Dasar Aritmetika (Paritas Eksponen Faktor Prima 2).
    4. Pembuktian Penurunan Tak Hingga (Method of Infinite Descent).

Jalankan:
    python3 proof_sqrt2_irrational.py
"""

import math
from fractions import Fraction
from typing import List, Tuple


def print_separator(title: str = "", char: str = "=", length: int = 70):
    """Mencetak garis pemisah dengan judul opsional."""
    if title:
        print(f"\n{char * 5} {title.upper()} {char * max(0, length - len(title) - 7)}")
    else:
        print(char * length)


# ─────────────────────────────────────────────────────────────────────────────
# 1. BUKTI FORMAL KLASIK: LANGKAH DEMI LANGKAH (STEP-BY-STEP PROOF)
# ─────────────────────────────────────────────────────────────────────────────

def lemma_even_square_implies_even_root(n_max: int = 10) -> bool:
    """
    Membuktikan Lemma: "Jika n² genap, maka n genap".
    
    Bukti Kontrapositif:
    Jika n ganjil, maka n dapat ditulis sebagai n = 2k + 1 (k ∈ Z).
    Maka n² = (2k + 1)² = 4k² + 4k + 1 = 2(2k² + 2k) + 1.
    Karena (2k² + 2k) adalah bilangan bulat, maka n² berbentuk 2m + 1 (ganjil).
    
    Karena "n ganjil => n² ganjil" benar,
    maka kontrapositifnya: "n² genap => n genap" juga PASTI BENAR.
    """
    print("\n--- Pembuktian Lemma: Jika n² genap, maka n genap ---")
    all_valid = True
    for n in range(1, n_max + 1):
        n_squared = n ** 2
        is_n_even = (n % 2 == 0)
        is_sq_even = (n_squared % 2 == 0)
        
        # Lemma menyatakan: is_sq_even -> is_n_even (ekivalen dengan: not is_sq_even or is_n_even)
        implication = (not is_sq_even) or is_n_even
        if not implication:
            all_valid = False
            
        paritas_n = "Genap" if is_n_even else "Ganjil"
        paritas_sq = "Genap" if is_sq_even else "Ganjil"
        print(f"n = {n:2d} ({paritas_n:6s}) -> n² = {n_squared:3d} ({paritas_sq:6s}) | Lemma valid: {implication}")
        
    return all_valid


def step_by_step_contradiction_proof():
    """
    Menampilkan dan memverifikasi langkah demi langkah pembuktian kontradiksi
    sesuai dengan formulasi matematika standar.
    """
    print_separator("1. Rekonstruksi Bukti Kontradiksi (Proof by Contradiction)")
    
    steps = [
        (
            "Langkah 1: Asumsi Dasar (Reductio ad Absurdum)",
            "Andaikan √2 adalah bilangan RASIONAL.\n"
            "Maka √2 dapat dinyatakan sebagai perbandingan dua bilangan bulat positif:\n"
            "    √2 = p / q\n"
            "di mana p, q ∈ Z⁺, q ≠ 0, dan p/q berada dalam BENTUK PALING SEDERHANA.\n"
            "Artinya, p dan q adalah relatif prima (koprima): gcd(p, q) = 1."
        ),
        (
            "Langkah 2: Kuadratkan Kedua Sisi",
            "(√2)² = (p / q)²\n"
            "2 = p² / q²\n"
            "Kalikan kedua sisi dengan q²:\n"
            "p² = 2q²"
        ),
        (
            "Langkah 3: Deduksi Paritas p",
            "Karena p² = 2q², maka p² adalah kelipatan 2 (p² bernilai GENAP).\n"
            "Berdasarkan lemma (jika kuadrat bilangan bulat genap, maka bilangannya genap):\n"
            "    p² genap  ==>  p genap.\n"
            "Karena p genap, maka p dapat ditulis sebagai kelipatan 2:\n"
            "    p = 2k  (untuk suatu bilangan bulat k ∈ Z⁺)"
        ),
        (
            "Langkah 4: Substitusi Nilai p Kembali ke Persamaan",
            "Substitusikan p = 2k ke persamaan p² = 2q²:\n"
            "    (2k)² = 2q²\n"
            "    4k² = 2q²\n"
            "Bagi kedua ruas dengan 2:\n"
            "    2k² = q²   atau   q² = 2k²"
        ),
        (
            "Langkah 5: Deduksi Paritas q",
            "Dari q² = 2k², jelas bahwa q² adalah kelipatan 2 (q² bernilai GENAP).\n"
            "Dengan lemma yang sama:\n"
            "    q² genap  ==>  q genap."
        ),
        (
            "Langkah 6: Terjadinya KONTRADIKSI!",
            "Dari Langkah 3: p adalah bilangan GENAP (dapat dibagi 2).\n"
            "Dari Langkah 5: q adalah bilangan GENAP (dapat dibagi 2).\n"
            "Maka 2 adalah faktor persekutuan dari p dan q:\n"
            "    gcd(p, q) ≥ 2\n"
            "\n"
            "⚠️  KONTRADIKSI FATAL!\n"
            "Ini bertentangan secara langsung dengan asumsi di Langkah 1 bahwa:\n"
            "    gcd(p, q) = 1 (p dan q tidak memiliki faktor persekutuan selain 1)."
        ),
        (
            "Langkah 7: Kesimpulan Akhir",
            "Karena kontradiksi tidak dapat dihindari, maka asumsi awal salah:\n"
            "    '√2 adalah bilangan rasional' ==> SALAH (FALSE)\n"
            "Oleh karena itu, kebalikannya harus benar:\n"
            "    √2 ADALAH BILANGAN IRASIONAL. ∎"
        )
    ]
    
    for title, content in steps:
        print(f"\n📌 {title}")
        print(f"   {content.replace(chr(10), chr(10) + '   ')}")
        
    # Verifikasi lemma pembantu
    lemma_even_square_implies_even_root(5)


# ─────────────────────────────────────────────────────────────────────────────
# 2. VERIFIKASI KOMPUTASIONAL / PENCARIAN EMPIRIS (FINITE SEARCH)
# ─────────────────────────────────────────────────────────────────────────────

def search_rational_approximation(max_q: int = 1000) -> List[Tuple[int, int, int, float]]:
    """
    Secara komputasional mencari pasangan (p, q) dengan gcd(p, q) = 1
    dan menunjukkan bahwa nilai p² - 2q² TIDAK PERNAH sama dengan 0.
    
    Mengembalikan daftar aproksimasi konvergen terbaik (di mana |p² - 2q²| = 1).
    """
    print_separator("2. Pencarian Komputasional Solusi p² = 2q²")
    print(f"Menguji semua pecahan p/q yang disederhanakan hingga q = {max_q}...")
    
    best_approximations = []
    exact_solution_found = False
    
    for q in range(1, max_q + 1):
        # Nilai p terbaik yang mendekati q * √2
        p = round(q * math.sqrt(2))
        
        # Periksa apakah gcd(p, q) == 1 (bentuk paling sederhana)
        if math.gcd(p, q) == 1:
            diff = p**2 - 2 * (q**2)
            ratio = p / q
            error = abs(ratio - math.sqrt(2))
            
            if diff == 0:
                print(f"Ditemukan solusi eksak: p = {p}, q = {q}!")
                exact_solution_found = True
                break
            
            # Catat aproksimasi terbaik di mana selisih kuadrat bernilai minimum (|diff| == 1)
            if abs(diff) == 1:
                best_approximations.append((p, q, diff, error))
                
    if not exact_solution_found:
        print("\n✅ Hasil: Tidak ada satupun pasangan (p, q) bulat yang memenuhi p² = 2q²!")
        print("   Selisih p² - 2q² selalu bernilai minimal ±1, tidak pernah 0.")
        
    print("\nTabel Aproksimasi Rasional Terbaik untuk √2 (Pecahan Konvergen):")
    print("-" * 75)
    print(f"{'p':>10} | {'q':>10} | {'p/q':>18} | {'p² - 2q²':>10} | {'Error ke √2':>15}")
    print("-" * 75)
    for p, q, diff, err in best_approximations[:8]:
        frac_val = f"{p/q:.10f}"
        print(f"{p:>10d} | {q:>10d} | {frac_val:>18} | {diff:>10d} | {err:>15.2e}")
    print("-" * 75)
    print("Perhatikan kolom p² - 2q²: nilainya selalu bergantian antara +1 dan -1,")
    print("menegaskan bahwa p² tidak pernah bisa tepat menyamai 2q².")
    
    return best_approximations


# ─────────────────────────────────────────────────────────────────────────────
# 3. BUKTI ALTERNATIF: FAKTORISASI PRIMA (PRIME FACTORIZATION PARITY)
# ─────────────────────────────────────────────────────────────────────────────

def count_prime_factors_of_2(n: int) -> int:
    """Menghitung banyaknya faktor prima 2 dalam bilangan bulat n (2-adic valuation)."""
    if n == 0:
        return 0
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    return count


def proof_via_prime_factorization():
    """
    Membuktikan kontradiksi menggunakan Teorema Dasar Aritmetika:
    Setiap bilangan bulat > 1 memiliki faktorisasi prima yang UNIK.
    
    Pada persamaan:
        p² = 2 · q²
        
    Jika p memiliki k faktor prima 2 (yaitu p = 2^k · m, m ganjil),
    maka p² memiliki 2k faktor prima 2 (selalu GENAP).
    
    Jika q memiliki j faktor prima 2 (yaitu q = 2^j · r, r ganjil),
    maka q² memiliki 2j faktor prima 2.
    Akibatnya, ruas kanan 2 · q² memiliki 1 + 2j faktor prima 2 (selalu GANJIL).
    
    Ruas Kiri:  banyaknya faktor 2 = 2k     (GENAP)
    Ruas Kanan: banyaknya faktor 2 = 2j + 1 (GANJIL)
    
    Karena bilangan genap tidak pernah sama dengan bilangan ganjil (2k ≠ 2j + 1),
    maka p² = 2q² TIDAK MEMILIKI SOLUSI bilangan bulat positif non-nol.
    """
    print_separator("3. Bukti Kontradiksi via Paritas Faktor Prima (Teorema Dasar Aritmetika)")
    print("Analisis Eksponen Bilangan Prima 2 pada Persamaan: p² = 2q²\n")
    
    sample_values = [(3, 2), (7, 5), (17, 12), (41, 29), (99, 70)]
    
    print(f"{'p':>5} | {'q':>5} | {'Faktor 2 di p²':>16} (Genap?) | {'Faktor 2 di 2q²':>17} (Ganjil?) | Sama?")
    print("-" * 75)
    for p, q in sample_values:
        left_val = p ** 2
        right_val = 2 * (q ** 2)
        
        pow2_left = count_prime_factors_of_2(left_val)
        pow2_right = count_prime_factors_of_2(right_val)
        
        is_left_even = (pow2_left % 2 == 0)
        is_right_odd = (pow2_right % 2 != 0)
        is_equal = (pow2_left == pow2_right)
        
        print(f"{p:5d} | {q:5d} | {pow2_left:10d} ({'Genap':^5}) | {pow2_right:10d} ({'Ganjil':^6}) | {str(is_equal):^5}")
        
    print("-" * 75)
    print("Kesimpulan Teoretis:")
    print("  • Eksponen 2 pada p² adalah 2 · v₂(p)     ==> Pasti GENAP")
    print("  • Eksponen 2 pada 2q² adalah 2 · v₂(q) + 1 ==> Pasti GANJIL")
    print("  • Karena GENAP ≠ GANJIL, maka p² = 2q² MUSTAHIL secara aritmetika!")


# ─────────────────────────────────────────────────────────────────────────────
# 4. BUKTI METODE PENURUNAN TAK HINGGA (INFINITE DESCENT)
# ─────────────────────────────────────────────────────────────────────────────

def infinite_descent_demonstration(p0: int = 1414, q0: int = 1000):
    """
    Menunjukkan metode 'Infinite Descent' (Descente Infinie):
    Jika diasumsikan ada pecahan p/q terkecil yang sama dengan √2,
    kita dapat selalu menemukan pasangan baru yang LEBIH KECIL:
        p' = 2q - p
        q' = p - q
    
    Karena 1 < √2 < 2, maka q < p < 2q:
    - p' = 2q - p > 0 dan p' < p
    - q' = p - q > 0 dan q' < q
    
    Dan rasionya tetap sama:
        (p')² - 2(q')² = (2q - p)² - 2(p - q)²
                       = 4q² - 4pq + p² - 2(p² - 2pq + q²)
                       = 2q² - p² = -(p² - 2q²)
    
    Jika p² = 2q², maka (p')² = 2(q')².
    Proses ini menghasilkan barisan bilangan bulat positif menurun tanpa batas
    (p > p' > p'' > ... > 0), yang MUSTAHIL dalam himpunan bilangan asli (Well-Ordering Principle).
    """
    print_separator("4. Bukti via Penurunan Tak Hingga (Infinite Descent)")
    print("Jika ada pasangan bilangan asli terkecil (p, q), kita selalu dapat mengonstruksi")
    print("pasangan yang lebih kecil lagi: p' = 2q - p dan q' = p - q.\n")
    
    p, q = p0, q0
    print(f"Mulai dari pasangan aproksimasi awal: p = {p}, q = {q} (p/q = {p/q:.6f})")
    print(f"{'Iterasi':>7} | {'p':>8} | {'q':>8} | {'p/q':>12} | {'Catatan':>20}")
    print("-" * 65)
    
    for iteration in range(1, 6):
        new_p = 2 * q - p
        new_q = p - q
        
        if new_q <= 0 or new_p <= 0:
            print(f"{iteration:7d} | {abs(new_p):8d} | {abs(new_q):8d} | {'--':>12} | Nilai mencapai ≤ 0")
            break
            
        ratio = new_p / new_q
        print(f"{iteration:7d} | {new_p:8d} | {new_q:8d} | {ratio:12.6f} | Nilai p dan q mengecil!")
        p, q = new_p, new_q
        
    print("-" * 65)
    print("Aksioma Well-Ordering: Tidak ada barisan bilangan bulat positif menurun tak hingga.")
    print("Oleh karena itu, pasangan bilangan bulat terkecil tersebut TIDAK PERNAH ADA. ∎")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN EXECUTION
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("=" * 70)
    print("    PEMBUKTIAN MATEMATIKA & KOMPUTASIONAL: √2 ADALAH IRASIONAL    ")
    print("               (PROOF BY CONTRADICTION / EUCLID)                  ")
    print("=" * 70)
    
    # 1. Langkah demi langkah bukti kontradiksi klasik
    step_by_step_contradiction_proof()
    
    # 2. Verifikasi pencarian empiris pada bilangan bulat
    search_rational_approximation(max_q=1000)
    
    # 3. Bukti berbasis Teorema Dasar Aritmetika (Faktorisasi Prima)
    proof_via_prime_factorization()
    
    # 4. Bukti Penurunan Tak Hingga
    infinite_descent_demonstration()
    
    print_separator("Ringkasan Akhir")
    print("Semua jalur pembuktian (Aljabar Paritas, Teorema Dasar Aritmetika,")
    print("maupun Penurunan Tak Hingga) menghasilkan KONTRADIKSI yang tak terbantahkan.")
    print("=> Terbukti secara mutlak bahwa √2 adalah BILANGAN IRASIONAL (√2 ∉ Q, √2 ∈ R). ■\n")


if __name__ == "__main__":
    main()
