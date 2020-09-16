elemente = ["apfel", "birne", "wassermelone", "straßenverkehrskontrollierungsbescheinigungsverantwortlicher"]
sortiert = []
punkte = []

anfrage = input(">")
anfrage = anfrage.lower()

# Punkte berechnen
letterno = 0
for letter in anfrage:

    elementno = 0
    for element in elemente:
        elemente[elementno] = element.lower()
        punkte.append(element.count(letter))
        elementno += 1
    

# Erstellen und ausgeben
sortiert = list(zip(*sorted(list(zip(punkte,elemente)),reverse=True))) # Danke an DELTA und LoC (TheMorpheusTutorials' Discord) für Hilfe <3
print(sortiert)