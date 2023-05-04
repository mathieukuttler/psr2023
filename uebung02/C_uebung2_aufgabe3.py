# gruppe C
# 817928, 787490, 821198
# Übung 2: Aufgabe 3


fellowship = ['gandalf', 'aragorn', 'frodo', 'sam', 'merry', 'pippin', 'gimli', 'legolas', 'boromir']
hobbits = ['frodo', 'sam', 'pippin', 'merry']

a = 'saruman' in fellowship
b = 'gandalf' in fellowship[0]
c = fellowship[2] and fellowship[3] \
    and fellowship[4]  and fellowship[5] \
    and fellowship[6] and fellowship[7] \
    and fellowship[8] \
    in hobbits
d = 'sam' in hobbits and 'sam' in fellowship
e = 'gimli' == fellowship[-3] or 'gimli' in hobbits

# print für die Überprüfung:
print(a,b,c,d,e)
