"""
Exercises: Linear Equations  |  Phase 1 — Topic 1.4
"""
print("LATIHAN 1.4 — PERSAMAAN LINEAR")
print("=" * 50)

def solve(a, b, c):
    if a == 0: return ("Infinite" if b==c else "None")
    return (c - b) / a

# Ex 1
print("\n[Ex 1] Selesaikan:")
for a,b,c,label in [(3,7,22,"3x+7=22"),(2,-5,13,"2x-5=13"),
                    (-4,8,-12,"-4x+8=-12"),(1,0,0,"x=0")]:
    print(f"  {label}  ->  x = {solve(a,b,c)}")

# Ex 2
print("\n[Ex 2] Identifikasi jenis (satu solusi/tidak/tak hingga):")
for a,b,c in [(5,3,18),(0,7,7),(0,3,9),(2,4,4)]:
    r = solve(a,b,c)
    print(f"  {a}x + {b} = {c}  ->  {r}")

# Ex 3
print("\n[Ex 3] Soal kecepatan-waktu-jarak (d=vt):")
print("  Mobil A kecepatan 60 km/h, mobil B 80 km/h.")
print("  Keduanya start dari tempat sama ke arah sama.")
print("  Kapan B mendahului A sejauh 40 km?")
# 80t - 60t = 40  ->  20t = 40  ->  t = 2 jam
t = 40 / (80 - 60)
print(f"  Jawaban: t = {t} jam (setelah {t} jam)")

# Ex 4 - literal equations
print("\n[Ex 4] Selesaikan persamaan literal:")
print("  F = (9/5)C + 32  untuk C  ->  C = 5(F-32)/9")
for F in [32, 100, 212, -40]:
    C = 5*(F-32)/9
    print(f"  F={F}°F  ->  C={C:.2f}°C")

print("\n[Selesai]")
