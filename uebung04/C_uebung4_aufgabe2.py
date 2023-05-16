# wir nehmen an, dass unter "Token" ein 
# einziges String gemeint ist, 
# das allenfalls ein Apostroph auf index = -2 beinhaltet.
# wir gehen davon aus, dass es sich bei dem String
# um ein einziges "Wort" handelt.
# Es wäre gut gewesen, ein Beispiel 
# eines "verunreinigten Tokens" zu bekommen 

input_token = input('gib was ein' + '\n')
#print(f'> original: {input_token}')

# 1. satzzeichen löschen
satzzeichen = [',','.','!','?']
for x in satzzeichen:
    input_token = input_token.replace(x,'') 

# 2. leerzeichen an den Ränden löschen
input_token = input_token.strip()

# 3. Apostrophes & Anführungszeichen
#unsere Anweisung lautet wie folgt:
'''
um solche Fälle zu
berücksichtigen, sollen einfache Anführungszeichen
am Anfang eines Wortes ohne entsprechendes 
Anführungszeichen am Ende des Wortes nicht entfernt werden
'''
output_list = []
# hier Umsetzung der Anweisung Schritt für Schritt:
# 1. "einfache Anführungszeichen am Anfang eines Wortes":
if input_token.startswith("'"):
    # 2. "ohne entsprechendes Anführungszeichen am Ende des Wortes":
    if not input_token.endswith("'"):
        # 3. "sollen ... nicht entfernt werden"
        output_list.append(input_token[0])
        # jetzt bauen wir uns das Wort für den output:
        for char in input_token[1:]:
            # wir prüfen jedes Zeichen im input ob es ein Buchstabe ist:
            if char.isalpha():
                # und schreiben es ggf. in den output 
                output_list.append(char)
else: 
    # für allen tokens, die nicht mit "'" beginnen:
    for char in input_token:
        # ziehen wir erst alle Buchsgaben als Ouput raus
        # damit umgehen wir alle Punkte und Striche.
        # wir gehen davon aus, dass der Input englisch ist
        # und nur peter's und don't hat.
        # es funktioniert aber auch für Französisch,
        # z.B l'opéra
        if char.isalpha() or "'" in char: 
            output_list.append(char)


'''
da das briefing uns nicht sagt, 
was wir mit Zahlen machen sollen,
gehen wir hypothetisch von 
Input ohne Zahlen aus.
'''

#outpuliste umwandlen in string für den output:
out_string = ""
if len(output_list) > 0:
    out_string = ''.join(output_list)
else:
    out_string = "Kein Token gefunden"

print(output_list)
print(out_string)

