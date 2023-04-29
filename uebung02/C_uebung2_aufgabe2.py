satz1 = "Golm ist ein schoenes Fleckchen Erde."

a = satz1[1]
b = satz1[:3]
c = satz1[0] + satz1[5]  + satz1[10] \
    + satz1[15] + satz1[20] + satz1[25] \
    + satz1[30]  + satz1[35]
'''
die Backslashs sind um die Zeilen kurz zu halten.
irgendwo in den guideliens zum Kurs 
stand was von max 80 Zeichen Länge pro Zeile
das lässt sich auch im Editor einstellen,
je nachdem welchem man verwendet.
Ist good practice in teams so was einzuhalten,
wir könnten das gerne gleich von Beginn an einüben,
wenn Ihr möchtet. 
(ich muss auch für meine Editor nachschauen)
'''

'''
c ist nicht elegant, 
(weil es den selben Befehl 8 Mal wiederholt,
aber mir fällt aktuell 
mit den Befehlen aus den Folien 
nix besseres ein.
wir werden das später eleganter lösen
mit einer Schleife.
'''

d = satz1[:4][::-1]
e = satz1[::-1]

# prints vor Abgabe löschen
print(a)
print(b)
print(c)
print(d)
print(e)
