# gruppe C
# 817928, 787490, 821198
# Übung 2: Aufgabe 1

import math

a = int(input('Bitte Zahl a eingeben:'))
b = int(input('Bitte Zahl b eingeben:'))
c = int(input('Bitte Zahl c eingeben:'))

term = b ** 2 - 4 * a * c
sq = math.sqrt(term)
quot = 2 * a

x1 = round(((-b - sq) / quot), 4)
x2 = round(((-b + sq) / quot), 4)

# printouts für die Überprüfung:
print(f'x1: {x1}')
print(f'x2: {x2}')

