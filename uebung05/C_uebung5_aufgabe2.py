
word_in = input('gib string ein:')
separator = input('gib Trennzeichen ein:')

new_word_list = [] # die Wortliste anlegen
teilwort = '' # das leere Teilwort anlegen

for x in word_in:
    if x != separator:  # falls der Buchstabe ok ist:  
        teilwort += x # schreibe ihn ins neue Wort
    else: # Ausnahme: der Buchstabe splittet
        new_word_list.append(teilwort) # Teilwort in die Liste schreiben
        teilwort = '' # Teilwort wieder auf Null setzen

# Am Ende müssen wird den "sauberen" Rest 
# vom inputstring in die Liste eintragen:
# (weil wir nur bei Separatoren die Liste 
# beschrieben haben, fehlt dieser Schritt bislang) 

if teilwort not in new_word_list:
    new_word_list.append(teilwort)

print(new_word_list)

