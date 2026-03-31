import random

""" def papier_stein_schere():
    while True:
        print("=== Papier-Stein-Schere ===")

        # Liste der möglichen Handzeichen
        handzeichen_in_worte = ["stein", "papier", "schere"]

        # Zufallseingabe des Gegners
        com_choice = random.choice(handzeichen_in_worte) 

        # Eingabe des Benutzers
        user_choice = input("Stein, Papier oder Schere?\n")

        # Zeige die Eingabe vom Gegner
        print(com_choice)

        # Wenn Gegner und Benutzer den selben Handzeichen haben unentschieden
        if user_choice == com_choice:
             print("Unentschieden")
             gewinner = "Keiner"
        
        elif user_choice != com_choice:
            if user_choice == "stein" and com_choice == "papier":
                gewinner = "Computer gewinnt!"
                
            elif user_choice == "stein" and com_choice == "schere":
                gewinner = "Spieler gewinnt"

            elif user_choice == "schere" and com_choice == "papier":
                gewinner = "Spieler gewinnt"

            elif user_choice == "schere" and com_choice == "stein":
                gewinner = "Computer gewinnt"
            
            elif user_choice == "papier" and com_choice == "schere":
                gewinner = "Computer gewinnt"

            elif user_choice == "papier" and com_choice == "stein":
                gewinner = "Spieler gewinnt"

            else:
                print("Ungültige Eingabe!")

        print(f"{gewinner} gewinnt diese Runde!")

        play_again = input("Möchtest du noch eine Runde spielen? y/n:\n")

        if play_again != "y":
            break
        else:
            continue 
    
papier_stein_schere() """


""" 
def zahlenraten():
    while True:
        print("=== Zahlenraten ===")
        print()
        # Zufällige Zahl zwischen 1 und 100 in einer Variable
        random_number = random.randint(1, 100)
        guess = 0
        trys = 0

        while guess != random_number:
            trys += 1
            guess = int(input("Errate die zufällige Zahl indem du eine Zahl zwischen 1 und 100 eingibst:\n"))
            print()
            if guess < random_number:
                print("Zu niedrig!")
            elif guess > random_number:
                print("Zu hoch!")        
        
        if guess == random_number:
            print(f"Richtig. Du hast die Zahl erraten: {guess}")
            print(f"Du hast {trys} Versuche gebraucht.")

        play_again = input("Möchtest du noch eine Runde Spielen? y/n: \n")

        if play_again.lower() != "y":
            break
        else:
            continue
zahlenraten() """

""" def zufallsnamen():
    print("=== Zufallsnamen ===")
    while True:
        print()
        silben_liste = [
        # Vokal-dominant (weich/flüssig)
        "a", "e", "i", "o", "u", "ae", "io", "ia", "oa", "ya",
        "ma", "me", "mi", "mo", "mu", "la", "le", "li", "lo", "lu",
        "na", "ne", "ni", "no", "nu", "ra", "re", "ri", "ro", "ru",
        "sa", "se", "si", "so", "su", "va", "ve", "vi", "vo", "vu",
        
        # Konsonant-Endungen (kräftig/strukturiert)
        "al", "el", "il", "ol", "ul", "an", "en", "in", "on", "un",
        "ar", "er", "ir", "or", "ur", "as", "es", "is", "os", "us",
        "at", "et", "it", "ot", "ut", "am", "em", "im", "om", "um",
        
        # Komplexe & Mystische Klänge (Fantasy/Sci-Fi)
        "dra", "dro", "stri", "stra", "phy", "phi", "thra", "thro", "chron", "aeth",
        "vax", "vox", "vix", "trix", "trax", "zax", "zor", "zun", "flux", "syn",
        "bel", "dal", "gan", "kor", "mor", "pel", "quas", "sur", "tor", "ver",
        "bra", "cre", "dlo", "fra", "gle", "kri", "pla", "pre", "stu", "tra",
        
        # Kurze Akzente
        "ba", "be", "bi", "bo", "bu", "ca", "ce", "ci", "co", "cu",
        "da", "de", "di", "do", "du", "fa", "fe", "fi", "fo", "fu",
        "ga", "ge", "gi", "go", "gu", "ha", "he", "hi", "ho", "hu",
        "ka", "ke", "ki", "ko", "ku", "pa", "pe", "pi", "po", "pu"
        ]

        anzahl_wörter = int(input("Wie viele Wörter möchtest du generieren?\n"))
        anzahl_silben = int(input("Wie viele Silben möchtest du haben?\n"))

        fantasie_wort = ""

        liste_mit_wörtern = []

        for j in range(anzahl_wörter):
            for i in range(anzahl_silben):
                # Silben werden zum Fantasiewort hinzugefügt bis gewünschte silbenanzahl erreicht ist
                fantasie_wort += random.choice(silben_liste)

            print(fantasie_wort)
            liste_mit_wörtern.append(fantasie_wort)
            fantasie_wort = ""
        print()
        print(liste_mit_wörtern)

        # Abfrage ob noch mehr generiert werden soll
        create_more = input("Willst du noch mehr generieren lassen? y/n\n")
        if create_more.lower() != "y":
            break
        else:
            continue

zufallsnamen() """

""" def wuerfelsimulator():
    while True:
        print("=== Würfelsimulator ===")

        anzahl_wuerfel = int(input("Wie viele würfel möchtest du werfen? \n"))
        anzahl_seiten = int(input("Wie viele Seiten haben die Würfel?\n"))

        ergebnisse = []

        for i in range(anzahl_wuerfel):
            wurf = random.randint(1, anzahl_seiten)
            ergebnisse.append(wurf)
        
        print(ergebnisse)

        # Abfrage ob man noch weiter spielen möchte
        play_again = input("Möchtest du noch eine Runde Spielen? y/n: \n")
        if play_again.lower() != "y":
            break
        else:
            continue

wuerfelsimulator() """

""" def glueckskeks():
    while True:
        print("=== Glückskeks ===")

        sprueche = [
        "Vorsicht vor Tratsch am Arbeitsplatz!",
        "Kleine Gewichtsschwankungen kündigen sich an.",
        "Mal verliert man, mal gewinnen die anderen.",
        "Früh aufstehen ist der erste Schritt in die falsche Richtung!",
        "Hüte dich davor, dass deine Empfindlichkeit zu einer wehleidigen Haltung führt.",
        "Lächeln ist die charmanteste Art, dem Gegner die Zähne zu zeigen.",
        "Wenn jeder an sich denkt, ist an alle gedacht.",
        "Das Glück, das du suchst, befindet sich in einem anderen Keks!",
        "Liebe ist, die Schokolade ganz alleine zu essen.",
        "Was du heute kannst entkorken, das verschiebe nicht auf morgen.",
        "Zuhause ist da, wo du doof sein darfst!",
        "Du hast alles in dir, was du zu deinem Unglück brauchst.",
        "Wenn das Leben dir einen Korb gibt, geh einkaufen.",
        "Deine Pflanzen sind nicht tot, sie wachsen nur knusprig.",
        "Komm auf die dunkle Seite."
    ]
        
        # Ausgabe eines zufälligen Spruchs aus sprueche Liste
        print(random.choice(sprueche))
        print() # Zeilenumbruch

        # Abfrage ob man noch weiter spielen möchte
        play_again = input("Möchtest du dein Glück erneut versuchen? Y/N\n")
        if play_again.lower() != "y":
            break # beendet die Schleife
        else:
            continue # Springt zum Anfang der Schleife 

glueckskeks() """

""" def palindrom():
    while True:
        print("=== Palindrom ===")

        check_palindrom = input("Gib ein Wort ein, dass du prüfen möchtest.\n")
        
        # check_palindrom wird hier direkt umgedreht
        check_reversed = check_palindrom[::-1]
        print(check_reversed)

        # wandelt das wort in Kleinbuchstaben um und prüft ob es ein Palindrom ist 
        if check_palindrom.lower() == check_reversed.lower():
            print("Das eingegeben Wort ist ein Palindrom!\n")
        else:
            print("Das ist kein Palindrom!\n")

        # Abfrage ob man ein weiteres Wort prüfen möchte
        check_again = input("Möchtest du ein weiteres Wort prüfen? Y/N\n")
        if check_again.lower() != "y": # Alles was kein "Y" oder "y" ist beendet die schleife
            break # zum beenden der Schleife
        else:
            continue # y bring uns zum Anfang der Schleife

palindrom() """




def anagram():
    while 1:
        print("=== Anagram ===")

        check_word = input("Gib ein Wort ein, dass du prüfen möchtest.\n")
        # woerterbuch = open( "r")

        # erstellt eine Liste
        char_list = []
        # fügt jede einzelne Buchstabe der Liste hinzu
        for i in check_word:
            char_list += i
        print(char_list)

        """for line in woerterbuch:
            if check_word.upper() == line.upper():
                print(line) """

        # Abfrage ob man ein weiteres Wort prüfen möchte
        check_again = input("Möchtest du ein weiteres Wort prüfen? Y/N\n")
        if check_again.lower() != "y": # Alles was kein "Y" oder "y" ist beendet die schleife
            break # zum beenden der Schleife
        else:
            continue # y bring uns zum Anfang der Schleife

anagram()