#regel = input('bitte gib eine Regel ein!' + '\n')
regel = " B A --> b c d"

N = ["NP", "Det", "N"] 
N_mit_S = ["NP", "Det", "N", "S"]
T = ["the", "cat"]

testlist = ["NP --> Det NP","S --> the cat VP","NP --> ","N --> cat","NP --> the N"]

for regel in testlist:
    # wir gehen von True aus 
    # und prüfen in jedem if
    # ob die Fehlerbedinungen erfüllt sind:
    # (haben wir in MulG oder EinfCompLing so gelernt)
    correct_rule = True

    
    # 1. Regeln sollten genau nur einen Pfeil ("-->") enthalten
    pfeil = '-->'
    res = regel.count(pfeil)
    if res == 0:
        correct_rule = False
    elif res > 1:
        correct_rule = False
    else: #es gibt genau 1 Pfeil
        # also zuerst linke Seite und rechte Seite trennen: 
        links_rechts = regel.split('-->')
        links = links_rechts[0].strip()
        rechts = links_rechts[1].strip()
        # .strip() hier zur Sicherheit
        
        # linke Seite: wir prüfen sie in einem Rutsch:
        # "die linke Seite sollte genau ein Symbol lang sein" 
        len_links = len(links.split())
        '''     
        print('Links split:' + str(links.split()))
        print(type(links.split()))
        print(len_links)
        '''
        if len_links != 1:
            correct_rule = False
        # "das eine Symbol auf der linken Pfeilseite sollte
        # in der Menge der Nichtterminale enthalten sein"
        else: 
            # weil len_links nur noch == 1 sein kann:
            if links not in N_mit_S:
                correct_rule = False
        
        # jetzt prüfen wir die rechte Seite in einem Rutsch:
        # "und die rechte Seite ein oder zwei Symbole"  
        len_rechts = len(rechts.split())
        '''
        print('Rechts split:' + str(rechts.split()))
        print(type(rechts.split()))
        print(len_rechts)
        '''
        if len_rechts == 0 or len_rechts > 2: 
            correct_rule = False
        #3.b. "ist die rechte Seite 1 lang, 
        # dann sollte das eine Symbol in der Menge der
        # Terminale enthalten sein"
        if len_rechts == 1 and rechts not in T:
            correct_rule = False
        if len_rechts == 2:
            # rechts ist hier noch unverändert ein String,
            # das wir in eine Liste umwandeln, um auf die
            # einzelnen Wörter zugreifen zu können
            rechts_liste = rechts.split()
            # Prüfung Symbol 1:
            if rechts_liste[0] not in T:
                correct_rule = False
            # Prüfung Symbol 2: 
            if rechts_liste[1] not in N:
                correct_rule = False
 
 
    print(f'Regel: {regel}; Resultat: {correct_rule}')
