import math

a = int(input('Bitte a eingeben:'))
b = int(input('Bitte b eingeben:'))
c = int(input('Bitte c eingeben:'))

term = b ** b - 4 * a * c

sq = math.sqrt(term)
quot = 2 * a
x1 = round(((-b - sq) / quot), 4)
x2 = round(((-b + sq) / quot), 4)

'''
um ein Error bei z.B. der Eingabe von 1,5,10 zu vermeiden, 
könnten wir einfach vor der Ausführung prüfen, 
ob sq > 0 ist. Ich glaube aber die Aufgabe so zu verstehen,
dass wir bewusst so tun sollen, als 
würden solche Eingaben in der Realität nicht vorkommen.
Was wollen wir liefern?

Hier der Code, der für alle möglichen Zahlenkombis läuft:

if term > 0:
    sq = math.sqrt(term)
    quot = 2 * a
    x1 = round(((-b - sq) / quot), 4)
    x2 = round(((-b + sq) / quot), 4)
else:
    print('Term unter der Wurzel ist 0 oder kleiner') 
'''
