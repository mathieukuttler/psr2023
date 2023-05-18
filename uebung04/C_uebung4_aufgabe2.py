verunreinigter_token = "    '!?A'.z'bde,'peter's,!?  "
x = verunreinigter_token
print(f'Input: {x}')

# 1. Satzzeichen löschen
satzzeichen = [',','.','!','?']
for sz in satzzeichen:
    x = x.replace(sz,'') 

# 2. Leerzeichen an den Ränden löschen
x = x.strip() 
# umständlicher möglich mit .lstrip() und .rstrip()

# 3.a. "doppelte" Anführungszeichen
x = x.replace('"','')

# 3.b Aufgabe: einfache Anführungszeichen löschen 
# außer folgender Ausnahme:
# "um solche Fälle zu berücksichtigen, sollen 
# einfache Anführungszeichen am Anfang eines Wortes 
# ohne entsprechendes Anführungszeichen am Ende des Wortes 
# nicht entfernt werden"
# als Beispiel wird uns gegeben: x = "let's" => "let" und "'s" 

# falls "'" am Anfang des Wortes
if x.startswith('\''):
    # Rest des Wortes bereinigen und Wort wieder zusammenfügen:
    x = '\'' + x[1:].replace('\'','')
else:
    x = x.replace('\'','')
# ich habe hier die Anweisung befolgt,
# die sagt, wir bekommen ein "'s" als token

# jetzt die Ausgabe:
if len(x) == 0:
    print('Kein Token gefunden')
else:
    print(f'output: {x}')