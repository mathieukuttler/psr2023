fellowship = ['gandalf', 'aragorn', 'frodo', 'sam', 'merry', 'pippin', 'gimli', 'legolas', 'boromir']
hobbits = ['frodo', 'sam', 'pippin', 'merry']

a = 'saruman' in fellowship
b = 'gandalf' == fellowship[0]
#fellows_selection = fellowship[2:8] # = ['frodo', 'sam', 'merry', 'pippin', 'gimli', 'legolas']
c = fellowship[2] and fellowship[3] \
    and fellowship[4]  and fellowship[5] \
    and fellowship[6] and fellowship[7] \
    and fellowship[8] \
    in hobbits
# auch hier ließe sich c anders viel eleganter schreiben, 
# aber hier gehts wohl um das Einüben der logischen Operatoren durch Wiederholung
d = 'sam' in hobbits and 'sam' in fellowship
e = 'gimli' == fellowship[-3] or 'gimli' in hobbits

# print vor Abgabe löschen
print(a,b,c,d,e)
