with open('beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

competitors = []
for line in lines[1:]:
    name, team, wins, races = line.strip().split(';')
    competitors.append({
        'name': name,
        'team': team,
        'wins': int(wins),
        'races': int(races)
    })


num_competitors = len(competitors)

most_wins = max(competitors, key=lambda x: x['wins'])

most_races = max(competitors, key=lambda x: x['races'])

average_races = sum(comp['races'] for comp in competitors) / num_competitors

results = f"""1. A versenyzők száma: {num_competitors}
2. A legtöbb futamot nyerő versenyző: {most_wins['name']} ({most_wins['wins']} győzelem)
3. A legtöbb futamot teljesítő versenyző: {most_races['name']} ({most_races['races']} futam)
4. Átlagosan a versenyzők által teljesített futamok száma: {average_races:.2f}
"""

with open('kiirt_adatok/statisztika.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(results)
