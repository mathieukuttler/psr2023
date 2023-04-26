# gruppe C
# 817928, #todo die Matrikelunmmer von Orkan hier eintragen
# Übung 1: Aufgabe 6

'''
Mit input() werden die Variablen als strings erfasst. 
Um mit ihnen rechen zu könen, brauchen wir sie als integer. 
Wir müssen unsere Variablen also in integer umwandeln.
Das tun wir schon bei ihrer Erfassung, um unseren Code kurz zu halten.
'''

print('bitte geben Sie eine ganze Zahl ein ')
zahl1 = int(input())

print('bitte geben Sie noch eine ganze Zahl ein')
zahl2 = int(input())

# True ausgibt, wenn die eingele- senen Zahlen gleich sind, ansonsten False.
check = zahl1 == zahl2
print(check)

# 2. Gebt anschließend das Ergebnis 
# der Addition und 
 
addition = zahl1 + zahl2

# der Multiplikation der beiden Zahlen 
multiplication = zahl1 * zahl2
#sowie die Subtraktion zahl1 - zahl2 an.
substraction = zahl1 - zahl2

# Es soll jeweils ein Ergebnis in einer Zeile ausgegeben werden.
print(addition)
print(multiplication)
print(substraction)
