"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""

adatok = []

nevek_szama = 0

with open('beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        nev, csapat, gyozelmek_szama, telj_futamok_szama = sor.strip().split(';')
        adatok.append([nev, csapat, int(gyozelmek_szama), int(telj_futamok_szama)])

for sor in adatok:
    nevek_szama += 1

legtobb_gyozelem_versenyzo = None

legtobb_gyozelem = 0
for versenyzo in adatok:
    if legtobb_gyozelem < versenyzo[2]:
        legtobb_gyozelem = versenyzo[2]
        legtobb_gyozelem_versenyzo = versenyzo[0]

legtobb_futam_versenyzo = None

legtobb_futam = 0
for versenyzo in adatok:
    if legtobb_futam < versenyzo[3]:
        legtobb_futam = versenyzo[3]
        legtobb_futam_versenyzo = versenyzo[0]




print(f"A beolvasott fájlban összesen ", nevek_szama, "versenyző szerepel.")
print(f'A legtöbb futamot nyert versenyző: {legtobb_gyozelem_versenyzo}')
print(f"A legtöbb futamot teljesített versenyző: {legtobb_futam_versenyzo}")
print("Az átlagos futamszám: ____")