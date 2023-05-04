import math
a,b,c =  9,9,1

term = b ** 2 - 4 * a * c
sq = math.sqrt(term)
quot = 2 * a

x1 = round(((-b - sq) / quot), 4)
x2 = round(((-b + sq) / quot), 4)

print('Berechnung der Lösungen für bis zu -10,10:')
n_max = 10
loesungen = []
for a in range(-n_max, n_max + 1):
    for b in range(-n_max, n_max + 1):
        for c in range(-n_max, n_max + 1):
            term = b ** 2 - 4 * a * c
            if term >= 0:
                loesungen.append((a,b,c))
anzahl_loesungen = len(loesungen)

for loesung in loesungen:
      print(f"a: {loesung[0]}, b: {loesung[1]}, c: {loesung[2]}")

print(f'fuer +/- n_max = {n_max} gibt es {anzahl_loesungen} loesungen')
