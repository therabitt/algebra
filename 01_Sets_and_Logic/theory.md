# 1.14 Himpunan dan Logika — Teori Lengkap

## BAGIAN A: HIMPUNAN (SETS)

### 1. Definisi Himpunan
Himpunan adalah kumpulan objek yang terdefinisi dengan jelas, disebut elemen/anggota.
- Notasi: A = {1, 2, 3}  atau  B = {x | x > 0}  (set-builder)
- Keanggotaan: 2 ∈ A,  5 ∉ A

### 2. Himpunan Khusus
| Simbol | Nama | Contoh |
|--------|------|--------|
| ∅ atau {} | Himpunan kosong | {} |
| U | Himpunan universal | semua obyek yang relevan |
| A ⊆ B | Subset | {1,2} ⊆ {1,2,3} |
| A ⊂ B | Proper subset | {1,2} ⊂ {1,2,3} |

### 3. Kardinalitas
|A| = jumlah elemen unik dalam A
|∅| = 0,  |{1,2,3}| = 3

### 4. Operasi Himpunan
| Operasi | Simbol | Definisi |
|---------|--------|----------|
| Union | A ∪ B | {x | x∈A atau x∈B} |
| Intersection | A ∩ B | {x | x∈A dan x∈B} |
| Difference | A − B | {x | x∈A dan x∉B} |
| Complement | Aᶜ atau A' | {x∈U | x∉A} |
| Symmetric diff | A △ B | (A−B) ∪ (B−A) |

### 5. Hukum-Hukum Himpunan
- Komutatif: A∪B=B∪A,  A∩B=B∩A
- Asosiatif: (A∪B)∪C=A∪(B∪C)
- Distributif: A∩(B∪C)=(A∩B)∪(A∩C)
- **De Morgan:** (A∪B)ᶜ = Aᶜ∩Bᶜ,  (A∩B)ᶜ = Aᶜ∪Bᶜ
- Identitas: A∪∅=A,  A∩U=A
- Komplemen: A∪Aᶜ=U,  A∩Aᶜ=∅

### 6. Produk Kartesian
A × B = {(a,b) | a∈A, b∈B}
|A×B| = |A| × |B|

### 7. Himpunan Kuasa (Power Set)
P(A) = semua himpunan bagian dari A
|P(A)| = 2^|A|

### 8. Prinsip Inklusi-Eksklusi
|A∪B| = |A| + |B| − |A∩B|
|A∪B∪C| = |A|+|B|+|C|−|A∩B|−|A∩C|−|B∩C|+|A∩B∩C|

---

## BAGIAN B: LOGIKA PROPOSISIONAL

### 9. Proposisi dan Nilai Kebenaran
Proposisi adalah pernyataan yang bernilai BENAR (T) atau SALAH (F).

### 10. Konektor Logika
| Konektor | Simbol | Nama |
|----------|--------|------|
| NOT | ¬p | Negasi |
| AND | p ∧ q | Konjungsi |
| OR | p ∨ q | Disjungsi |
| XOR | p ⊕ q | Eksklusif OR |
| IMPLIKASI | p → q | Jika p maka q |
| BIKONDITIONAL | p ↔ q | p jika dan hanya jika q |

### 11. Tabel Kebenaran — Implikasi
| p | q | p→q |
|---|---|-----|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

p→q HANYA salah ketika p benar dan q salah.
Setara dengan: ¬p ∨ q

### 12. Konvers, Invers, Kontrapositif
Dari p→q:
- Konvers: q→p
- Invers: ¬p→¬q
- Kontrapositif: ¬q→¬p  ← SETARA dengan p→q!

### 13. Hukum De Morgan (Logika)
¬(p ∧ q) = ¬p ∨ ¬q
¬(p ∨ q) = ¬p ∧ ¬q

### 14. Tautologi dan Kontradiksi
- Tautologi: selalu BENAR (contoh: p ∨ ¬p)
- Kontradiksi: selalu SALAH (contoh: p ∧ ¬p)

### 15. Kuantifikasi
- ∀x P(x) — untuk SEMUA x, P(x) benar
- ∃x P(x) — ADA (setidaknya satu) x, P(x) benar
- Negasi: ¬(∀x P(x)) = ∃x ¬P(x)
- Negasi: ¬(∃x P(x)) = ∀x ¬P(x)

### 16. Teknik Pembuktian
1. Langsung (Direct): asumsikan p, buktikan q
2. Kontrapositif: buktikan ¬q→¬p
3. Kontradiksi: asumsikan p dan ¬q, dapatkan kontradiksi
4. Induksi matematika: P(1) benar, P(k)→P(k+1)
