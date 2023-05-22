max_sterne = int(input('max Sterne eingeben:'))

# mehr werden: von 1 bis max
for i in range(1, max_sterne + 1):
    print(i, "*" * i)

# weniger werden: von max zurück zu 0 in 1er Schritten
for i in range(max_sterne - 1, 0, -1):
    print(i, "*" * i)
