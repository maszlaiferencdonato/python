import random

szamok = [random.randint(1, 12) for _ in range(20)]

harommaloszthato = [szam for szam in szamok if szam % 3 == 0]

print("A 3-mal osztható számok:")
for szam in harommaloszthato:
    print(szam)

# Az osztható számok számának kiírása
print(f"Összesen {len(harommaloszthato)} darab szám osztható 3-mal.")
