satz_in = input("Geben Sie einen Satz ein: ")

# Satzzeichen entfernen und Satz in Wörter aufteilen
# von letzter Woche - extended
satzzeichen = [',','.','!','?',';','"','\'',':','+','-','=','*','/']
for sz in satzzeichen:
    satz_clean = satz_in.replace(sz,'') 

# Satz splitten (in Wörter aufteilen)
woerter = satz_clean.split()

# Wörter zählen
anzahl_woerter = len(woerter)

# Wortlängen berechnen:
# länge aller Wörter / Anzahl der Wörter
len_woerter = 0

for x in woerter:
    len_woerter += len(x) 

wortlaenge_durchschnitt = round(len_woerter / anzahl_woerter, 2)

# tuple anlegen
result = (anzahl_woerter, wortlaenge_durchschnitt)
