from json import loads
from random import randint

if __name__ == "__main__":
    # Wo liegen die Fragen ?
    print("Dann lass uns mal die Abfrage starten, ich muss die Küche noch aufräumen.")
    fragenpfad = input("Wo liegen den die Thematiken ? ")

    # Korrketes Eingabeformat ?
    if fragenpfad.split(".")[1] != "json":
        raise FileNotFoundError
    # TODO ordentlichen Fehler schreiben
    else:

        # Einlesen der Fragen
        with open(file=fragenpfad, mode="r") as fragen:
            fragenliste = loads(fragen.read())

        while len(fragenliste):
            # Frage stellen
            frage = fragenliste.pop(randint(0, len(fragenliste) - 1))

            print(" ", "Okay, diese Frage ist über: " + frage["Thematik"],
                  frage["Frage"], sep="\n")

            # Antwort validieren
            print("Ich brauche {x} Antworten!".format(x=len(frage["Antwort"])))
            # TODO Reihenfolge der Antworten egalisieren
            for antwort in frage["Antwort"]:
                x = 0
                x += 1
                if input(str(x) + " :").lower() in antwort:
                    print("Korrekt!")
                else:
                    print("Das musst du nochmal üben!")
                    fragenliste.append(frage)
                    fragenliste.append(frage)
                    # TODO Dual append
                    break
            print("Okay, noch {x} Fragen, dann muss ich aber weiter!".format(x=len(fragenliste)))
