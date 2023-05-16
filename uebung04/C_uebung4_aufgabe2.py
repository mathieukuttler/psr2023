# ein "verunreinigten Token" ist laut Aurora 
# ein Token mit überflüssigen Zeichen
# es ist beim Tokenisieren (splitten) 
# eines Textes entstanden 

input_token = "    '!?A'.z'bde,'peter's,!?  "

input_token = input('gib was ein' + '\n')

# 1. Satzzeichen löschen
satzzeichen = [',','.','!','?']
for x in satzzeichen:
    input_token = input_token.replace(x,'') 

# 2. Leerzeichen an den Ränden löschen
input_token = input_token.strip()

# 3.a. "doppelte" Anführungszeichen
input_token = input_token.replace('"','')

# 3.b einfache Anführungszeichen löschen 
# außer folgender Ausnahme:
'''
um solche Fälle zu berücksichtigen, sollen 
einfache Anführungszeichen am Anfang eines Wortes 
ohne entsprechendes Anführungszeichen am Ende des Wortes 
nicht entfernt werden
'''
if input_token.startswith('\''):
    input_token = input_token[1:].replace('\'','')
else:
    input_token = input_token.replace('\'','')

out_message = input_token
if len(out_message) == 0:
    out_message = 'Kein Token gefunden'
    
print(f'> original: {input_token}')
print(f'> output: {out_message}')