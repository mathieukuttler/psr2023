# ein "verunreinigten Token" ist laut Aurora 
# ein Token mit überflüssigen Zeichen
# es ist beim Tokenisieren (splitten) 
# eines Textes entstanden 

verunreinigter_token = "    '!?A'.z'bde,'peter's,!?  "

x = verunreinigter_token
#x = "'s"
print(f'Input: {x}')
# 1. Satzzeichen löschen

satzzeichen = [',','.','!','?']
for sz in satzzeichen:
    x = x.replace(sz,'') 
#print(x)    

# 2. Leerzeichen an den Ränden löschen
x = x.strip() 
# umständlicher möglich mit .lstrip() und .rstrip()
#print(x)

# 3.a. "doppelte" Anführungszeichen
x = x.replace('"','')
#print(x)

# 3.b Aufgabe: einfache Anführungszeichen löschen 
# außer folgender Ausnahme:
# "um solche Fälle zu berücksichtigen, sollen 
# einfache Anführungszeichen am Anfang eines Wortes 
# ohne entsprechendes Anführungszeichen am Ende des Wortes 
# nicht entfernt werden"

# als Beispiel wird uns gegeben: x = "let's" => "let" und "'s" 
# wir sollen beide Fälle berücksichtigen
if x.startswith('\''): # falls "'" am Anfang des Wortes
    # Rest des Wortes bereinigen und Wort wieder zusammenfügen
    x = '\'' + x[1:].replace('\'','') 
#print(x)

# jetzt die Ausgabe:
if len(x) == 0:
    print('Kein Token gefunden')
else:
    print(f'output: {x}')