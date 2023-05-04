# gruppe C
# 817928, 787490, 821198
# Übung 2: Aufgabe 6

user_input = input().split()
length = len(user_input)
input_as_tuple = tuple(user_input)
contains_python = 'python' in user_input or 'Python' in user_input
copy_input = user_input[::-1]
same_element = user_input[0] == input_as_tuple[0]

# prints zur Überprüfung:
print(user_input)
print(length)
print(input_as_tuple)
print(contains_python)
print(copy_input)
print(same_element)