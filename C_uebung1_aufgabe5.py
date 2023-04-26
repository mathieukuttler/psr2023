# gruppe C
# 817928, 787490, 821198
# Übung 1: Aufgabe 5

# 1. Lest vom User/von der Userin zwei Strings ein.
print('gib bitte etwas sein')
string1 = input()

print('und bitte noch mehr')
string2 = input()

# 2. Gebt den zweiten String zwei Mal mit sich selbst konkateniert zuru ̈ck (also word2word2word2).
word2word2word2 = string2 + string2 + string2
print(word2word2word2)

# 3. Konkateniert anschließend die beiden eingelesen Strings (also word1word2) und gebt das Ergebnis aus.
aufgabe_5_3 = string1 + string2
print(aufgabe_5_3)

# 4. Gebt anschließend noch beide Strings mit *** eingefasst aus (also ***word1***word2***).
strings_stars = '***' + string1 + '***' + string2 + '***'
print(strings_stars)