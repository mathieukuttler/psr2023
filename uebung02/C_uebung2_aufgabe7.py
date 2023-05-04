# gruppe C
# 817928, 787490, 821198
# Übung 2: Aufgabe 7

string = input('Bitte geben Sie etwas ein.')

'''
wir bauen den output der Beispiele  
aus der Aufgabe nach:
'''

string = 'hallo, welt'

a = string.count('a')
print(a)
b = string[::-1]
print(b)
c = string[::2]
print(c)
d = string[-3:]
print(d)

words = string.split(' ')
e = words[0] + '***' + words[1]
print(e)
