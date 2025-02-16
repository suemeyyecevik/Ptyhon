import math

 #DEF : In Python wird das Schlüsselwort def zum Definieren einer Funktion verwendet.
 #Funktionen sind Codeblöcke, die eine bestimmte Operation ausführen und bei Bedarf wiederverwendet werden können.
 #def gibt den Anfang der Funktion an und der Funktionsname und die Parameter (falls vorhanden) werden geschrieben.

def kalkulator():
    print("Fortgeschrittener Kalkulator.")
    print("Optionen:")
    print("1: Addition")
    print("2: Subtraktion")
    print("3: Multiplikation")
    print("4: Division")
    print("5: Potenzzahlen (a^b)")
    print("6: Quadratwurzel")
    print("7: Prozent")
    print("0: Abmelden ")

    while True:     #WHİLE: Startet eine Schleife. Der Zyklus läuft weiter, solange eine bestimmte Bedingung erfüllt ist.
        try:
            wahl = int(input("\nWählen Sie eine Aktion aus. (0-7): "))
            if wahl == 0:     #
                print("Kalkulator wird ausgeschaltet....")
                break      #BREAK: Wird verwendet, um Schleifen vorzeitig zu beenden. Stoppt sofort eine for- oder while-Schleife.

    # zwei nummerierte Operationen.
            if wahl in [1, 2, 3, 4, 5]:
                num1 = float(input("Geben Sie die erste Zahl ein.: "))
                num2 = float(input("Geben Sie die zweite Zahl ein.: "))

                if wahl == 1:    #İF: Legt eine Bedingung fest und stellt sicher, dass ein Codeblock nur ausgeführt wird, wenn eine bestimmte Bedingung wahr ist.
                    print(f"Ergebnis: {num1} + {num2} = {num1 + num2}")
                elif wahl == 2:
                    print(f"Ergebnis: {num1} - {num2} = {num1 - num2}")
                elif wahl == 3:
                    print(f"Ergebnis: {num1} * {num2} = {num1 * num2}")
                elif wahl == 4:   #ELİF: Wird für zusätzliche alternative Bedingungen der if-Bedingung verwendet. Wenn die if-Bedingung falsch ist, wird die elif-Bedingung überprüft.
                    if num2 == 0:
                        print("Fehler: Eine Zahl kann nicht durch Null geteilt werden.!")
                    else:           # ELSE: Gibt den Codeblock an, der ausgeführt werden soll, wenn die if- oder elif-Bedingung nicht erfüllt ist.
                        print(f"Ergebnis: {num1} / {num2} = {num1 / num2}")
                elif wahl == 5:
                    print(f"Ergebnis: {num1}^{num2} = {math.pow(num1, num2)}")

            elif wahl == 6:  # Ziehe die Quadratwurzel.
                nummer = float(input("Geben Sie die Zahl ein, aus der Sie die Quadratwurzel ziehen möchten.: "))
                if nummer < 0:
                    print("Fehler: Sie können nicht die Quadratwurzel einer negativen Zahl ziehen!")
                else:
                    print(f"Ergebnis: √{nummer} = {math.sqrt(nummer)}")

            elif wahl == 7:  # PROZENT
                nummer = float(input("Nummer eingeben: "))
                prozent = float(input("Welchen Prozentsatz möchten Sie berechnen? "))
                print(f"Ergebnis: {nummer}'nin %{prozent}'si = {nummer * (prozent / 100)}")

            else:
                print("Falsche Auswahl, bitte geben Sie eine Zahl zwischen 0 und 7 ein.")

        except ValueError: #EXCEPT : Fängt Fehler innerhalb des Try-Blocks ab und ermöglicht die Durchführung alternativer Aktionen, wenn ein Fehler auftritt.
            print("Fehler: Bitte geben Sie eine gültige Nummer ein!")

# Kalkulator wird gestartet.
kalkulator()
