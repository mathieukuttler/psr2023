'''
Ein Schaltjahr ist ohne Rest durch 4 teilbar 
und nicht durch 100 teilbar
ODER es ist ohne Rest durch 400 teilbar 
'''
for jahr in range(1971,2024):
    testergbnis = ''
    if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
        ergebnis = " = Schaltjahr"
    else:
        ergebnis = " = KEIN Schaltjahr"
    print(f'{jahr}{ergebnis}')
