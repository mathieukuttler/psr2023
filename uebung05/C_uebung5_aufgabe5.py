user_in = input('Gib Dezimalzahl ein: ')
bin_zahl = ''

# Validitätsprüfung des Inputs:
val = 0
for x in user_in:
    if not x.isdigit():
        val += 1 # non-digit-character erhöht 'val'

if val > 0:
    print('Invalid Input')
else:
    dec_zahl = int(user_in)
    # Konvertierung in Binärzahl
    if dec_zahl == 0:
        bin_zahl = '0'
    else:
        while dec_zahl > 0:
            bin_zahl = str(dec_zahl % 2) + bin_zahl
            dec_zahl = dec_zahl // 2
    print(bin_zahl)
