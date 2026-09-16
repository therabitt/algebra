# 1.13 Matriks Dasar — Teori Lengkap

## 1. Definisi Matriks
Matriks adalah susunan bilangan dalam baris dan kolom berbentuk persegi panjang.
Matriks m×n memiliki m baris dan n kolom.

    A = [a_ij]  di mana a_ij = elemen baris i, kolom j

## 2. Jenis-Jenis Matriks
| Nama | Definisi |
|------|----------|
| Matriks baris | Hanya satu baris (1×n) |
| Matriks kolom | Hanya satu kolom (m×1) |
| Matriks persegi | Baris = Kolom (n×n) |
| Matriks nol | Semua elemen = 0 |
| Matriks identitas (I) | Diagonal = 1, lainnya = 0 |
| Matriks diagonal | Non-diagonal = 0 |
| Matriks simetris | A = Aᵀ (aᵢⱼ = aⱼᵢ) |
| Matriks segitiga | Atas/bawah diagonal = 0 |

## 3. Kesamaan Matriks
A = B  ⟺  dimensi sama DAN aᵢⱼ = bᵢⱼ untuk semua i,j

## 4. Operasi Matriks

### Penjumlahan dan Pengurangan
(A ± B)ᵢⱼ = aᵢⱼ ± bᵢⱼ  (harus dimensi sama)
Sifat: komutatif, asosiatif

### Perkalian Skalar
(kA)ᵢⱼ = k · aᵢⱼ

### Perkalian Matriks
(AB)ᵢⱼ = Σₖ aᵢₖ · bₖⱼ
A(m×n) × B(n×p) = C(m×p)

Sifat perkalian matriks:
- TIDAK komutatif: AB ≠ BA (umumnya)
- Asosiatif: (AB)C = A(BC)
- Distributif: A(B+C) = AB + AC
- A·I = I·A = A

## 5. Transpose
(Aᵀ)ᵢⱼ = Aⱼᵢ  (baris jadi kolom, kolom jadi baris)
Sifat: (AB)ᵀ = BᵀAᵀ, (Aᵀ)ᵀ = A

## 6. Trace
tr(A) = Σᵢ aᵢᵢ  (jumlah diagonal utama)
Berlaku: tr(AB) = tr(BA)

## 7. Determinan

### 2×2:
|a b|
|c d|  = ad - bc

### 3×3 (Sarrus / Cofactor expansion):
|a b c|
|d e f| = a(ei-fh) - b(di-fg) + c(dh-eg)
|g h i|

Sifat determinan:
- det(AB) = det(A)·det(B)
- det(Aᵀ) = det(A)
- Jika baris/kolom sama: det = 0
- Tukar dua baris: det berubah tanda

## 8. Matriks Invers
A⁻¹ ada jika dan hanya jika det(A) ≠ 0 (matriks non-singular).
A · A⁻¹ = A⁻¹ · A = I

Untuk 2×2:
Jika A = |a b|, maka A⁻¹ = (1/det(A)) · | d -b|
         |c d|                             |-c  a|

## 9. Eliminasi Gauss
Metode untuk menyelesaikan Ax = b:
1. Buat matriks augmented [A|b]
2. Operasi baris elementer: tukar, kali skalar, tambah kelipatan
3. Bentuk row echelon form
4. Back substitution

## 10. Rank Matriks
Rank = jumlah baris tidak-nol setelah row reduction.
- Sistem Ax=b: solusi unik jika rank(A) = rank([A|b]) = n
- Tak hingga solusi jika rank(A) = rank([A|b]) < n
- Tidak ada solusi jika rank(A) < rank([A|b])

## 11. Aplikasi Matriks
- Grafis komputer (transformasi 2D/3D)
- Jaringan (adjacency matrix)
- Ekonomi (model input-output)
- Kriptografi
- Machine learning
