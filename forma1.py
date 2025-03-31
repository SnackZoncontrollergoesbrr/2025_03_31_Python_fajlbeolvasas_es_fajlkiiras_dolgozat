"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""


# print("A beolvasott fájlban összesen ____ versenyző szerepel.")
# print("A legtöbb futamot nyert versenyző: ____")
# print("A legtöbb futamot teljesített versenyző: ____")
# print("Az átlagos futamszám: ____")

# Név; Csapat; Győzelmek száma; Teljesített futamok száma
versenyzok = []
with open('beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nev = adatok[0]
        csapat = adatok[1]
        gyozelmek_szama = int(adatok[2])
        teljesitett_futamok_szama = int(adatok[3])
        versenyzok.append([nev, csapat, gyozelmek_szama, teljesitett_futamok_szama])

# print(f'{versenyzok=}')

print(f"A beolvasott fájlban összesen {len(versenyzok)} versenyző szerepel.")

legtobb_gyozelmi_versenyzo = None
legtobb_gyozelem = 0
for versenyzo in versenyzok:
    if versenyzo[2] > legtobb_gyozelem:
        legtobb_gyozelem = versenyzo[2]
        legtobb_gyozelmi_versenyzo = versenyzo

# print(legtobb_gyozelem)
# print(legtobb_gyozelmi_versenyzo)
print(f"A legtöbb futamot nyert versenyző: {legtobb_gyozelmi_versenyzo[0]}")

legtobb_futam_versenyzo = None
legtobb_futam = 0
for versenyzo in versenyzok:
    if versenyzo[3] > legtobb_futam:
        legtobb_futam = versenyzo[3]
        legtobb_futam_versenyzo = versenyzo

print(f"A legtöbb futamot teljesített versenyző: {legtobb_futam_versenyzo[0]}, a csapat neve: {legtobb_futam_versenyzo[1]}")