dec_in = input('Gib Dezimalzahl ein: ')

dec_zahl = int(dec_in)
bin_zahl = ''

# Konvertierung in Binärzahl
if dec_zahl == 0:
    bin_zahl = '0'
else:
    while dec_zahl > 0:
        print('////////')
        print(f'dec: {dec_zahl}')
        print('decModulo:' + str(dec_zahl % 2))
        bin_zahl = str(dec_zahl % 2) + bin_zahl
        print(f'bin: {bin_zahl}')
        dec_zahl = dec_zahl // 2


print('final:')
print(bin_zahl)
