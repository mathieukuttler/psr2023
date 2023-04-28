import math

a = int(input('Bitte a eingeben:'))
b = int(input('Bitte b eingeben:'))
c = int(input('Bitte c eingeben:'))

term = b ** b - 4 * a * c

if term > 0:
    sq = math.sqrt(term)
    quot = 2 * a
    x1 = round(((-b - sq) / quot), 4)
    x2 = round(((-b + sq) / quot), 4)
else:
    print('Term unter der Wurzel ist 0 oder kleiner') 

