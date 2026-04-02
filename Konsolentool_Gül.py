import random

def taschenrechner():
    print("=== Taschenrechner ===")
    
    while True:  # Endlosschleife damit das programm bei Falscheingaben hier wieder starten kann
    
        print()
        # Liste mit erlaubten Operatoren
        erlaubte_operatoren = ["+", "-", "*", "/", "%"]

        # Error abfangen:

        operator = input("Mit welchen operator möchtest du rechnen?\n")
        if operator not in erlaubte_operatoren:
            print("Ungültiger Operator!")
            continue

        try:    # wenn eingaben keine zahlen sind startet Taschenrechner neu
            operand1 = float(input("Erste Zahl: "))
        except ValueError:
            print("Ungültige Eingabe!\n")
            continue

        try:
            operand2 = float(input("Zweite Zahl: "))
        except ValueError:
            print("Ungültige Eingabe!\n")
            continue
            
        if operator is "+":                                 # berechnung mit +
            ergebnis = round(operand1 + operand2, 12)
        elif operator is "-":                               # berechnung mit -
            ergebnis = round(operand1 - operand2, 12)
        elif operator is "*":                               # berechnung mit *
            ergebnis = round(operand1 * operand2, 12)
        elif operator is "/":                               # berechnung mit /
            if operand2 == 0:
                try:
                    operand2 = float(input("Division durch 0 nicht möglich. Nimm eine Zahl außer 0:\n"))
                except (ValueError, ZeroDivisionError, TypeError):
                    print("Ungültige Eingabe oder wieder 0 eingegeben!\nFang nochmal von vorne an!\n")
                    print()
                continue
            ergebnis = round(operand1 / operand2, 12)
        elif operator is "%":                               # berechnung mit %
            ergebnis = round(operand1 % operand2, 12)
        else:
            print("Ungültige Eingabe!")

        print(f"{operand1} {operator} {operand2} = {ergebnis}") # Ausgabe der Berechnung und des Ergebnis

        # Abfrage ob weiter gerechnet werden soll
        calc_again = input("Möchtest du eine weitere berechnung durchführen? y/n: ")
        if calc_again.lower() != "y": # alles andere bringt uns zurück zum Hauptmenü
            break

        else:  # startet wieder den Taschenrechner
            print()
            continue

########################################################################################################################################

def bmi_rechner():
    print("=== BMI-Rechner ===")
    while True:        
        print()

        try:
            # Eingabe der jeweiligen Daten
            gewicht = float(input("Gib dein gewicht ein (KG):\n"))  
            print(f"{gewicht} Kilogramm")
        except ValueError:
            print("Gib eun gültigen positiven Wert an!")

        try:
            groesse = float(input("Gib deine Körpergröße in CM ein:\n"))
            print(f"{groesse} CM")
        except ValueError:
            print("Gib ein gültigen positiven Wert an!")

        if groesse == 0:
            print("Division durch 0 nicht möglich!")
            continue

        bmi = gewicht / ((groesse / 100) * (groesse / 100))     # Formel für BMI: gewicht / körpergröße * körpergewicht

        # Verzweigung zur jeweilgen Diagnose
        if bmi < 18.5:
            diagnose = "Untergewicht"
        elif bmi >= 18.5 and bmi < 25:
            diagnose = "Normalgewicht"
        elif bmi >= 25 and bmi < 30:
            diagnose = "Übergewicht"
        elif bmi >= 30 and bmi < 35:
            diagnose = "Adipositas Grad 1"
        elif bmi >= 35:
            diagnose = "Adipositas Grad 2"
        print(f"Sie haben ein BMI von {bmi:.1f} und haben {diagnose}.")

        # Abfrage ob weiter gerechnet werden soll
        calc_again = input("Möchtest du eine weitere berechnung durchführen? y/n: ")
        if calc_again.lower() != "y": # bringt uns zurück zum Hauptmenü 
            break

        else: # startet wieder den BMI-Rechner
            print()
            continue

########################################################################################################################################

def papier_stein_schere():
    while True:
        print("=== Papier-Stein-Schere ===")
        print()
        # Liste der möglichen Handzeichen
        handzeichen_in_worte = ["stein", "papier", "schere"]

        # Zufallseingabe des Gegners
        com_choice = random.choice(handzeichen_in_worte) 

        # Eingabe des Benutzers
        user_choice = input("Stein, Papier oder Schere?\n\n")
        user_choice = user_choice.lower()
        print()
        
        # springt zurück zum anfang des moduls wenn was anderes eingegeben wird als das was in der liste steht
        if user_choice not in handzeichen_in_worte:
            print("Du hast 'Stein', 'Papier' oder 'Schere' zur Auswahl!\n")
            continue
        else:
            # Zeige die Eingabe vom Gegner
            print(f"{user_choice} gegen {com_choice}")
            print()

        # Wenn Gegner und Benutzer den selben Handzeichen haben : Unentschieden
        if user_choice == com_choice:
             print("Unentschieden")
             gewinner = "Keiner"
        
        # Verzweigung wer wann gewinnt
        elif user_choice != com_choice:
            if user_choice == "stein" and com_choice == "papier":
                gewinner = "Computer"
                
            elif user_choice == "stein" and com_choice == "schere":
                gewinner = "Spieler"

            elif user_choice == "schere" and com_choice == "papier":
                gewinner = "Spieler"

            elif user_choice == "schere" and com_choice == "stein":
                gewinner = "Computer"
            
            elif user_choice == "papier" and com_choice == "schere":
                gewinner = "Computer"

            elif user_choice == "papier" and com_choice == "stein":
                gewinner = "Spieler"

            else:
                print("Ungültige Eingabe!")

        print(f"{gewinner} gewinnt diese Runde!")
        print()

        # Abfrage ob man noch weiter spielen möchte
        play_again = input("Möchtest du noch eine Runde spielen? y/n:\n")
        if play_again != "y":
            break
        else:
            print()
            continue 

########################################################################################################################################

def zufallsnamen():
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

        try:
            anzahl_wörter = int(input("Wie viele Wörter möchtest du generieren?\n\n"))
            print()
            anzahl_silben = int(input("Wie viele Silben möchtest du haben?\n\n"))
        except ValueError:
            print()
            print("gib hier einfach nur ganze Zahle ein. Bitte!\n\n")
            continue

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
            print()
            continue

########################################################################################################################################

def hangman():
    while True:
        print("=== Hangman ===")
        print()
        print("[1] Tiere")
        print("[2] deutsche Städte")
        print("[3] Länder")
        print("[4] Flüsse")
        print("[5] Sportarten")
        print("[6] Videospiele")
        print("[7] Automarken")
        print("[8] Informatik")
        # print("[9] Zufällig")
        print()

        # Status des Galgenmänchens
        hangman_status = [
        # 0 Leben (Tod)
        """
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        |
        """,
        # 1 Leben
        """
        ------
        |    |
        |    O
        |   /|\\
        |   / 
        |
        """,
        # 2 Leben
        """
        ------
        |    |
        |    O
        |   /|\\
        |    
        |
        """,
        # 3 Leben
        """
        ------
        |    |
        |    O
        |   /|
        |    
        |
        """,
        # 4 Leben
        """
        ------
        |    |
        |    O
        |    |
        |    
        |
        """,
        # 5 Leben
        """
        ------
        |    |
        |    O
        |    
        |    
        |
        """,
        # 6 Leben (Startzustand)
        """
        ------
        |    |
        |    
        |    
        |    
        |
        """
    ]
        try:
            category = int(input("mit welcher Kategorie möchtest du spielen?\n\n"))

            if category == 1:   # Tiere
                woerter_liste = ["Elefant", "Känguru", "Pinguin", "Schimpanse", "Krokodil", "Eichhörnchen", "Nashorn", "Libelle", "Schildkröte", "Hamster"]
            elif category == 2: # deutsche Städte
                woerter_liste = ["Berlin", "Hamburg", "München", "Frankfurt", "Stuttgart", "Dortmund", "Dresden", "Bremen", "Hannover", "Nürnberg"]
            elif category == 3: # Länder
                woerter_liste = ["Brasilien", "Frankreich", "Italien", "Kanada", "Japan", "Australien", "Ägypten", "Norwegen", "Mexiko", "Thailand"]
            elif category == 4: # Flüsse
                woerter_liste = ["Rhein", "Donau", "Elbe", "Main", "Neckar", "Mosel", "Weser", "Isar", "Spree", "Ems"]
            elif category == 5: # Sportarten
                woerter_liste = ["Fussball", "Basketball", "Tennis", "Volleyball", "Schwimmen", "Leichtathletik", "Handball", "Badminton", "Fechten", "Rudern"]
            elif category == 6: # Videospiele
                woerter_liste = ["Minecraft", "Tetris", "Pacman", "Fortnite", "Valorant", "Overwatch", "Eldenring", "Bloodborne", "Zelda", "Mario"]
            elif category == 7: # Automarken
                woerter_liste = ["Mercedes", "Porsche", "Volkswagen", "Ferrari", "Lamborghini", "Toyota", "Hyundai", "Renault", "Peugeot", "Mazda"]
            elif category == 8: # Informatik
                woerter_liste = ["Algorithmus", "Prozessor", "Datenbank", "Schnittstelle", "Programmierung", "Netzwerk", "Hardware", "Software", "Bit", "Byte"]
            else:
                print("Ungültige Auswahl. Wähle von 1 bis 8!\n")
                continue
        except ValueError:
            print("Ungültige Eingabe! Es werden nur Zahlen akzeptiert!\n")
            continue

        # elif category == 9: # Zufällig
        #     woerter_liste = random.randint(range(1, 8))

        # speichert zufälliges wort aus woerter_liste
        secret_word = random.choice(woerter_liste)
        secret_word = secret_word.lower()
        #print(secret_word)

        # Ersetze die wörter durch "_"
        display_word = len(secret_word) * ["_"]
        
        print(" ".join(display_word))
        print()
        guessed_letters = []
        
        # anzahl von Leben
        lives = 6

        while "_" in display_word and lives > 0:
            
            # einen Buchstaben raten
            guess = input("Rate einen Buchstaben\n oder das ganze Wort\n wenn du dich traust:\n")

            # Wenn Eingabe ein Buchstabe und Länge von eins ist
            if guess.isalpha() and len(guess) == 1:
                # Wenn Eingabe schonmal eingegeben wurde
                if guess in guessed_letters:
                    print("Dieser Buchstabe wurde schon erraten")
                    continue # Überspringt restlichen Code und springt zum Schleifenanfang zurück 
                else:
                    guessed_letters.append(guess) # Wenn die Eingabe zum erstenmal vorkommt füge die eingabe zur liste hizu
                    
                    # Wenn eingabe in secret_word existiert...
                    if guess.lower() in secret_word.lower():
                        print("Dieser Buchstabe ist korrekt!")

                        # durch secret_word iterieren
                        for i in range(len(secret_word)):
                            # wenn an stelle i Buchstabe von secret_word gleich eingabe ist, setze in display an der Stelle diesen Buchstaben
                            if secret_word[i] == guess:
                                display_word[i] = guess
                        print(f"Leben: {lives}") # Anzeigen von übrigen Leben
                        print(hangman_status[lives])
                            
                    else:
                        print("Leider falsch geraten!")
                        lives -= 1 # Bei falsch raten wird leben um eins reduziert
                        print(f"Leben: {lives}\n") # Anzeigen von übrigen Leben
                        print(hangman_status[lives])                        

                print(" ".join(display_word)) # Ausgabe des secret_word wie es aktuell aussieht
            
            elif len(guess) > 1 and guess.isalpha(): # wenn guess/eingabe aus mehreren Buchstaben besteht
                if guess.lower() == secret_word.lower():
                    display_word = guess
                    print(f"Leben: {lives}") # Anzeigen von übrigen Leben
                    print(hangman_status[lives])
                else:
                    print("Leider falsch geraten!")
                    lives -= 1 # Bei falsch raten wird leben um eins reduziert
                    print(f"Leben: {lives}\n") # Anzeigen von übrigen Leben
                    print(hangman_status[lives])

            else:
                print("Ich kann so nicht arbeiten!") 

        if "".join(display_word) == secret_word.lower():
            print("Glückwunsch, du hast das Wort rausgefunden\n")
        else:
            print(f"Schade. Du hast keine Leben mehr. Das gesuchte Wort war {secret_word}.\n")

        play_again = input("Möchtest du noch eine Runde Spielen? (y/n): \n")

        if play_again.lower() != "y":
            print("--- Spiel beendet. ---")
            break
        else:
            play_again.lower() == "y"
            print()
            continue

########################################################################################################################################

def zahlenraten():
    while True:
        print("=== Zahlenraten ===")
        print()

        try:
            # Zufällige Zahl zwischen zwei Usereingaben in einer Variable
            random_number = random.randint(int(input("Niedrigste Zahl: ")), int(input("Höchste Zahl: ")))
        except ValueError:
            print("Ungültiger Wert. Bitte nur Zahlen eingeben!\n")
            continue
        
        # prüft ob die zufällige Zahl ein Integer ist
        if not isinstance(random_number, int):
            print("Bitte nur Ganzzahlen eingeben. Danke!\n")
            continue

        guessed_numbers = []

        guess = 0

        trys = 0

        while guess != random_number:
            
            # trys zählt die Versuche
            trys += 1
            try:
                # guess speichert den wert der eingabe
                guess = int(input("Errate die zufällige Zahl in der von dir angegeben Range:\n"))
                print()
            except ValueError:
                print("Du musst schon eine Zahl eingeben.")
                continue

            if guess not in guessed_numbers:
                
                guessed_numbers.append(guess)

                if guess < random_number:
                    print("Zu niedrig!\n")
                elif guess > random_number:
                    print("Zu hoch!\n")        
        
            else:
                print("Diese Zahl hast du schon versucht.\n")

        # Wenn geratene Zahl gleich zufällige Zahl ist hat mann gewonnen
        if guess == random_number:
            print(f"Richtig. Du hast die Zahl erraten: {guess}")
            print()
            print(f"Du hast {trys} Versuche gebraucht.")

        # Abfrage ob man noch weiter spielen möchte
        play_again = input("Möchtest du noch eine Runde Spielen? y/n: \n")
        if play_again.lower() != "y":
            break
        else:
            print()
            continue

########################################################################################################################################

def wuerfelsimulator():
    while True:
        print("=== Würfelsimulator ===")

        try:
            anzahl_wuerfel = int(input("Wie viele würfel möchtest du werfen? \n"))
            anzahl_seiten = int(input("Wie viele Seiten haben die Würfel?\n"))
        except (ValueError, TypeError):
            print("Hier funktionieren nur ganze Zahlen.\nAlso nochmal von vorn.\n")
            continue

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
            print()
            continue

########################################################################################################################################

def glueckskeks():
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
            print()
            continue # Springt zum Anfang der Schleife

########################################################################################################################################

def palindrom():
    while True:
        print("=== Palindrom ===")
        print()

        # Eingabe des Wortes das geprüft werden soll
        check_palindrom = str(input("Gib ein Wort ein, dass du prüfen möchtest.\n"))
        print()

        # Wenn die Eingabe Zahlen enthält startet die Schleife neu   
        if not check_palindrom.isalpha():
            print("Das ist keine gültige Eingabe.")
            print()
            continue

        # check_palindrom wird hier direkt umgedreht und ausgegeben
        check_reversed = check_palindrom[::-1]
        print(f"{check_reversed} ist dein Wort rückwärts geschrieben.")
        print()

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
            print()
            continue # y bring uns zum Anfang der Schleife

########################################################################################################################################

def anagramm():
    while True:
        print("=== Anagramm ===")
        print()

        # User Eingabe welches auf Anagramme geprüft werden soll
        check_anagram = input("Gib ein Wort ein, dass du prüfen möchtest.\n")
        check_anagram = check_anagram.lower()

        # Wenn die Eingabe Zahlen enthält startet die Schleife neu   
        if not check_anagram.isalpha():
            print("Das ist keine gültige Eingabe.")
            print()
            continue

        try:
            # Anzahl der Anagramme
            anzahl_anagramm = int(input("Gib an wie viele Anagramme ausgegeben werden sollen.\n"))
        except ValueError:
            print("Hier ist nach Anzahl gefragt. Nochmal von vorn.\n")
            print()
            continue

        # deklariert leere liste in der die Anagramme hinzugefügt werden 
        anagramm_list = []

        # Schleife für die geewünschte Anzahl an Anagrammen
        for i in range(anzahl_anagramm):

            # Leere Liste für die Buchstaben des eingegebenen Wortes
            char_list = []

            # Hier werden die Buchstaben in die Liste hinzugefügt und gemischt
            for j in check_anagram:
                char_list.append(j)
            random.shuffle(char_list) 
            
            # deklariert neue Variable in der die Buchstaben aus char_list zusammengefügt werden
            anagramm_wort = "".join(char_list)
            
            # fügt das neugemischte wort der anagramm_list hinzu
            anagramm_list.append(anagramm_wort)
        
        # Ausgabe der Liste
        print(anagramm_list)


        # Abfrage ob man ein weiteres Wort prüfen möchte
        check_again = input("Möchtest du ein weiteres Wort prüfen? Y/N\n")
        if check_again.lower() != "y": # Alles was kein "Y" oder "y" ist beendet die schleife
            break # zum beenden der Schleife
        else:
            print()
            continue # y bringt uns zum Anfang der Schleife

########################################################################################################################################

def hauptmenu():
    print()
    print("=== Konsolentool von Recai Gül ===")
    # Menüpunkte
    while True:
        print()
        print("=== Hauptmenü ====================")
        print()
        print("[x] Beenden")
        print("[0] Taschenrechner")
        print("[1] BMI Rechner")
        print("[2] Papier-Stein-Schere")
        print("[3] Zufallsnamen")
        print("[4] Hangman")
        print("[5] Zahlenraten")
        print("[6] Würfelsimulator")
        print("[7] Glückskeks")
        print("[8] Palindrom")
        print("[9] Anagramm")
        print("==================================")
        print()

        # Benutzer Eingaben
        eingabe = input("Wähle eine Aktion aus: \n")
        print()
        if eingabe == "x":
            break
        elif eingabe == "0":
            taschenrechner()
        elif eingabe == "1":
            bmi_rechner()
        elif eingabe == "2":
            papier_stein_schere()
        elif eingabe == "3":
            zufallsnamen()
        elif eingabe == "4":
            hangman()
        elif eingabe == "5":
            zahlenraten()
        elif eingabe == "6":
            wuerfelsimulator()
        elif eingabe == "7":
            glueckskeks()
        elif eingabe == "8":
            palindrom()
        elif eingabe == "9":
            anagramm()
        else:
            print("Ungültige Eingabe")
hauptmenu()