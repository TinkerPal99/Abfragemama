# Abfragemama
Lernen ist eine grausame Tätigkeit für die meisten Schüler- Daher greifen sie gerne zu Hilfsmitteln.
Dieses Repository zeigt ein einfaches Programm, das mittels JSON-Bibliothek Fragen an den Nutzer stellt und dabei 
unerbittlich wie eine Mutter selbst ist.

Für den AE Unterricht findet sich anbei die Aufgabenstellung, wie man dieses Programm simpel nachbauen kann. Für mich 
selbst plane ich aber noch einige Erweiterungen, wie eine mobile Anwendung daraus zu machen.

Im Folgenden habe ich Aufgaben formuliert, die einem dabei helfen, das Programm selber zu formulieren. Empfohlen ist es 
für einen **Python-Anfänger** mit Wissen über Schleifen, Listen&Dictionaries, Arbeit mit Dateien und grundlegenen Libraries 
(json, random)
##Nachbauen

Für das Lernen werden gerne Lernkarteien benutzt, diese sollen hier 'modernisiert' werden.

### 1. Kartein einlesen

Die Fragen hart einzucoden ist zwar machbar, aber nicht schön. Stattdessen werden sie in einer json mitgeliefert. 
Man kann diese nach Fächern oder Lehrjahren trennen.
EIne Beispieldatei findet sich hier Abfragemama\Fragenbibliothek\Versuch.json

a)  Diese Datei muss nun eingelessen werden, mittels python-Methode "open()" und dann der Inhalt mittels der JSON-library in ein 
    Python-lesbares Format verwandelt werden. 
    Alle Fragen finden sich in einer Liste wieder, die Fragen selbst sind jeweils ein Dictionary.

b)  Der Userfreundlichkeit halber, sollte der Pfad, wo die json gefunden werden kann, via input() angegeben werden.

Zusatz **Errorhandling**)  Was passiert nun, wenn der USer eine nicht-json angibt ? Dies müssen wir sauber abfangen. Gibt der User eine 
    nicht-Json an, soll der FIleNotFoundError geworfen werden 
    
Zum Test können wir uns die komplette Fragenliste nun ausgeben lassen. Sieht der Output gut aus ? Perfekt, dann weiter !
### 2. Fragen stellen
Die Fragen müssen nun aus der Fragenliste ausgelesen werden und gestellt werden.

a)  Zuerst müssen wir eine Frage aus der Frageliste auswählen, dabei am besten eine zufällige, sodass die Reihenfolge 
    sich immer unterscheidet. 

b)  Als nächstes soll für jede Frage die Thematik genannt werden, gefolgt von der Frage an sich.
    Das heißt wir lesen diese Daten jeweil aus dem Dictionary aus, das wir zuvor zufällig aus der Frageliste gewählt 
    haben.

c)  In der Json sehen wir, eine Frage kann auf 2 Antworten warten, also müssen wir zählen, wieviele Antworten erwartet 
    werden. Dabei sind die erwarteten Antworten jeweils eine Liste, in welcher sich auch mögliche Synonyme finden.
        
         "Antwort": [
                  ["programmablaufplan", "pap"],
                  ["pseudocode"]
                ]
                        
   Das Dict-Attribut "Antwort" ist eine Liste, diese Liste enthält 2 erwartete Antworten, wobei die Erste ein 
   Synonym erwartet.

### 3. Antwort erhalten
Was sind Fragen ohne Antworten ? Aufjedenfall keine gute Abfragemama!

a)  Für jede erwartete Antwort im Attribut "Antwort" muss einmal der Input genommen werden.
    Ist dieser Input nun richtig, muss entsprechend reagiert werden, ist diese falsch muss eine Strafe 
    (bspw. das doppelte Abfragen dieses 'Schwachpunktes') vorgenommen werden. Ist bereits die erste Antwort in einer Frage 
    mit mehreren Antworten falsch, kann die Frage abgebrochen werden.

b)  Sind alle Fragen der Frageliste beantwortet, kann der Spaß mit einem freundlichen Kommentar beendet werden. 
    Sind noch Fragen vorhanden, soll jedoch dies dargestellt werden.

### 4. Ausprobieren

Die JSON kann nun um diverse Fragen erweitert werden, und dann ausprobieren, ob das Programm funktioniert.  
Wenn es Fragen gibt, stehe ich gerne Antwort und unterstütze.