import random

#create needed variables
options = ["scissors", "paper", "rack"]

print("let's play rock, paper, scissors!")
# an elemnt from the lists 'options' is seclected randomly
player_a = random.choice(options)
# Fehler 1:
#player_b = input("Please input one of the following:" + options + "\n" )
# options ist hier eine Liste. Es wird versucht, diese in ein String zu concatenate.
# Das ist in python nicht möglich. Denn in solchen Operationen müssen 
# concatenierte Variablen wie Listen oder auch Zahlen in strings konvertiert werden.
# Z.B. so:
player_b = input("Please input one of the following:" + str(options) + "\n" )

# validate user input:
# falls die Eingabe nicht in "options" enthalten is:
if player_b not in options: 
# Fehler 2: nach der If-Deklaration fehlt die Intendation
#print("Please choose one of the given options")
# diese Anweisung müsste eingerückt sein
# so wird es korrigiert (durch Einrücken):
    print("Please choose one of the given options")

# das Program wiederholt die Aufforderung so lange,
# wie die Bedingung "not in options" erfüllt ist.
# Das Spiel geht erst dann weiter, 
# wenn diese Bedingung erfüllt ist:
else: 
    # d.h. bei einer richtigen Eingabe passiert folgendes
    # Anzeige der Spieleingaben
    print("vs.\n" + player_a)
    print("-"*65)
#die erste Bedingung ist erfüllt, 
#es geht weiter.

# In den nachfolgenden Zeilen prüft 
# das Programm ausschließllich die Fälle,
# in denen player_b nicht verliert.
# Die Bedingungsüberprüfung "sind die 
# EIngaben korrekt?" ist erfüllt.

# Jetzt beginnt das eigentliche Spiel 
# mit der Bedingungsüberprüfung 
# "Spieler b hat nicht verloren"
# Daher würde ich hier statt "else" (sonstige Fälle)
# mit einem neuen "if" fortführen
# am Einfachsten wäre es hierbei
# in den Zeilen 17 - 24 des Originalcodes
# den intend (die Einrückung) auf 0 zu setzen:

 # Fehler 3: syntax error
 # player_a = player_b:
 if player_a == player_b:
    # Lösung: die `(Un)gleichheit von Variablen vergleicht 
    # man in python mit "==". Das im Code verwendete "="
    # benutzt man für die Deklaration von Variablen
    # Korrektur für diese und die nachfolgenden Zeilen:
    print("There is now winner!")
#Fehler 4: formaler Logikoprator "^" für Konjunkiton 
# ist in python "AND"
#elif player_b == "scissors" ^ player_a == "paper":
# so ist es korrekt:
elif player_b == "scissors" AND player_a == "paper":    
    print("You won!")
elif player_b =="paper" AND player_a = "rock":
    print("You won!")
elif player_b =="rock" AND player_a = "scissors":
    print("You won!")
else:
    print("You lost!")

