import random

def taschenrechner():
    print("=== Taschenrechner ===")
    
    while True:  # Endlosschleife damit das programm bei Falscheingaben hier wieder starten kann
    
        print()
        # Liste mit erlaubten Operatoren
        erlaubte_operatoren = ["+", "-", "*", "/", "%"]

        operator = input("Mit welchen operator möchtest du rechnen?\n")
        if operator not in erlaubte_operatoren:
            print("Ungültiger Operator!")
            continue

        try:                                                # wenn eingaben keine zahlen sind startet Taschenrechner neu
            operand1 = float(input("Erste Zahl: "))
        except ValueError:
            print("Ungültige Eingabe! ")
            continue
        try:
            operand2 = float(input("Zweite Zahl: "))
        except ValueError:
            print("Ungültige Eingabe! ")
            continue
            
        if operator is "+":                                 # berechnung mit +
            ergebnis = round(operand1 + operand2, 12)
        elif operator is "-":                               # berechnung mit -
            ergebnis = round(operand1 - operand2, 12)
        elif operator is "*":                               # berechnung mit *
            ergebnis = round(operand1 * operand2, 12)
        elif operator is "/":                               # berechnung mit /
            if operand2 == 0:
                print("Division durch 0 nicht möglich!")
                continue
            ergebnis = round(operand1 / operand2, 12)
        elif operator is "%":                               # berechnung mit %
            ergebnis = round(operand1 % operand2, 12)
        else:
            print("Ungültige Eingabe!")

        print(f"{operand1} {operator} {operand2} = {ergebnis}") # Ausgabe der Berechnung und des Ergebnis

        # Abfrage ob weiter gerechnet werden soll
        calc_again = input("Möchtest du eine weitere berechnung durchführen? y/n: ")
        if calc_again.lower() == "y": # startet wieder den Taschenrechner
            taschenrechner()

        else: # bringt uns zurück zum Hauptmenü
            hauptmenu()
########################################################################################################################################

def bmi_rechner():
    print("=== BMI-Rechner ===")
    while True:        
        print()

        # Eingabe der jeweiligen Daten
        gewicht = float(input("Gib dein gewicht ein (KG):\n"))  
        print(f"{gewicht} Kilogramm")

        groesse = float(input("Gib deine Körpergröße in CM ein:\n"))
        print(f"{groesse} CM")
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
        if calc_again.lower() == "y": # startet wieder den BMI-Rechner
            bmi_rechner()

        else: # bringt uns zurück zum Hauptmenü
            hauptmenu()
########################################################################################################################################

def papier_stein_schere():
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

        # Abfrage ob man noch weiter spielen möchte
        play_again = input("Möchtest du noch eine Runde spielen? y/n:\n")
        if play_again != "y":
            break
        else:
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

zufallsnamen()

########################################################################################################################################

def hangman():
    print("=== Hangman ===")

########################################################################################################################################

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
        
        # Wenn geratene Zahl gleich zufällige Zahl ist hat mann gewonnen
        if guess == random_number:
            print(f"Richtig. Du hast die Zahl erraten: {guess}")
            print(f"Du hast {trys} Versuche gebraucht.")

        # Abfrage ob man noch weiter spielen möchte
        play_again = input("Möchtest du noch eine Runde Spielen? y/n: \n")
        if play_again.lower() != "y":
            break
        else:
            continue
########################################################################################################################################

def wuerfelsimulator():
    print("=== Würfelsimulator ===")

########################################################################################################################################

def glueckskeks():
    print("=== Glückskeks ===")

########################################################################################################################################

def palindrom():
    print("=== Palindrom ===")

########################################################################################################################################

def anagram():
    print("=== Anagram ===")

########################################################################################################################################

def hauptmenu():
    print("=== Konsolentool von Recai Gül ===")
    
    # Menüpunkte
    while True:
        print("=== Hauptmenü ===")
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
        print("[9] Anagram")
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
            anagram()
        else:
            print("Ungültige Eingabe")
hauptmenu()

