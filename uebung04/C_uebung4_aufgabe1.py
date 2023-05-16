import random

#create needed variables
options = ["scissors", "paper", "rock"]

print("let's play rock, paper, scissors!")

# an eleemnt from the lists 'options' is seclected randomly
player_a = random.choice(options)

player_b = input("Please input one of the following:" + str(options) + "\n")
# validate user input

#if player_b not in options: 
#print("Please choose one of the given options")
'''
Fehler 2: nach der If-Deklaration fehlt die Intendation
diese Anweisung müsste eingerückt sein
so wird es korrigiert (durch Einrücken):
'''
if player_b not in options: 
    print("Please choose one of the given options")
'''
An dieser Stelle hat das Program ein Desingfehler:
es übernimmt die falsche Antwort und läuft 
in Zeile 14 mit dem Else weiter.
Besser wäre es, den User zu einer neuen Eingabe aufzufordern.
Das geht z.B. mit einer For-Schleife, mit der man die Anzahl
der Eingaben begrenzen kan (for i in range(3)),
oder mit einer While-Schleife, die solange fragt, 
bis der User eine richhtige Eingabe tätigt.
So würde das mit While aussehen, also ab Zeile 15 neu::

while True:
    if player_b not in options:
        print("INPUT ERROR. PLEASE RETRY.")
        player_b = input("Please input one of the following:" + str(options) + "\n")
    else:
        break
'''
print("vs.\n" + player_a)
print("-"*65)

# calculate the score:  
# if player_a = player_b:
'''
Fehler 3: syntax error
Lösung:
'''
if player_a == player_b:
    print("There is no winner!")
    '''
    Warum diese Lösung?            
    Die Gleichheit von Variablen vergleicht 
    man in python mit "==". 
    Das im Code verwendete "=" benutzt man 
    für die Deklaration von Variablen.
    '''
    #elif player_b == "scissors" ^ player_a == "paper":
    '''
    Fehler 4: formaler Logikoprator "^" für Konjunktion 
    ist in python "and"
    so ist es korrekt:
    '''
elif (player_b == "scissors" and player_a == "paper") or\
     (player_b =="paper" and player_a == "rock") or\
     (player_b =="rock" and player_a == "scissors"):
    print("You won!")
    # die multiplen elifs gehen eleganter mit "or",
    # denn formallogisch sind sie ja reine Wiederholungen von ifs,
    # von denen eines TRUE sein muss.
else:
    print("You lost!")
        

