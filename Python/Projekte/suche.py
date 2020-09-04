elemente = ["In", "botany,", "a", "tree", "is", "a", "perennial", "plant", "with", "an", "elongated", "stem,", "or", "trunk,", "supporting", "branches", "and", "leaves", "in", "most", "species.", "In", "some", "usages,", "the", "definition", "of", "a", "tree", "may", "be", "narrower,", "including", "only", "woody", "plants", "with", "secondary", "growth,", "plants", "that", "are", "usable", "as", "lumber", "or", "plants", "above", "a", "specified", "height.", "In", "wider", "definitions,", "the", "taller", "palms,", "tree", "ferns,", "bananas,", "and", "bamboos", "are", "also", "trees.", "Trees", "are", "not", "a", "taxonomic", "group", "but", "include", "a", "variety", "of", "plant", "species", "that", "have", "independently", "evolved", "a", "trunk", "and", "branches", "as", "a", "way", "to", "tower", "above", "other", "plants", "to", "compete", "for", "sunlight.", "Trees", "tend", "to", "be", "long-lived,", "some", "reaching", "several", "thousand", "years", "old.", "Trees", "have", "been", "in", "existence", "for", "370", "million", "years.", "It", "is", "estimated", "that", "there", "are", "some", "three", "trillion", "mature", "trees", "in", "the", "world.", "A", "tree", "typically", "has", "many", "secondary", "branches", "supported", "clear", "of", "the", "ground", "by", "the", "trunk.", "This", "trunk", "typically", "contains", "woody", "tissue", "for", "strength,", "and", "vascular", "tissue", "to", "carry", "materials", "from", "one", "part", "of", "the", "tree", "to", "another.", "For", "most", "trees", "it", "is", "surrounded", "by", "a", "layer", "of", "bark", "which", "serves", "as", "a", "protective", "barrier.", "Below", "the", "ground,", "the", "roots", "branch", "and", "spread", "out", "widely;", "they", "serve", "to", "anchor", "the", "tree", "and", "extract", "moisture", "and", "nutrients", "from", "the", "soil.", "Above", "ground,", "the", "branches", "divide", "into", "smaller", "branches", "and", "shoots.", "The", "shoots", "typically", "bear", "leaves,", "which", "capture", "light", "energy", "and", "convert", "it", "into", "sugars", "by", "photosynthesis,", "providing", "the", "food", "for", "the", "trees", "growth", "and", "development.", "Trees", "usually", "reproduce", "using", "seeds.", "Flowers", "and", "fruit", "may", "be", "present,", "but", "some", "trees,", "such", "as", "conifers,", "instead", "have", "pollen", "cones", "and", "seed", "cones.", "Palms,", "bananas,", "and", "bamboos", "also", "produce", "seeds,", "but", "tree", "ferns", "produce", "spores", "instead.", "Trees", "play", "a", "significant", "role", "in", "reducing", "erosion", "and", "moderating", "the", "climate.", "They", "remove", "carbon", "dioxide", "from", "the", "atmosphere", "and", "store", "large", "quantities", "of", "carbon", "in", "their", "tissues.", "Trees", "and", "forests", "provide", "a", "habitat", "for", "many", "species", "of", "animals", "and", "plants.", "Tropical", "rainforests", "are", "among", "the", "most", "biodiverse", "habitats", "in", "the", "world.", "Trees", "provide", "shade", "and", "shelter,", "timber", "for", "construction,", "fuel", "for", "cooking", "and", "heating,", "and", "fruit", "for", "food", "as", "well", "as", "having", "many", "other", "uses.", "In", "parts", "of", "the", "world,", "forests", "are", "shrinking", "as", "trees", "are", "cleared", "to", "increase", "the", "amount", "of", "land", "available", "for", "agriculture.", "Because", "of", "their", "longevity", "and", "usefulness,", "trees", "have", "always", "been", "revered,", "with", "sacred", "groves", "in", "various", "cultures,", "and", "they", "play", "a", "role", "in", "many", "of", "the", "worlds", "mythologies."]

punkte = []

for element in elemente:
    punkte.append(0)


anfrage = input(">")
anfrage = anfrage.lower()

letterno = 0
for letter in anfrage:

    elementno = 0
    for element in elemente:
        punkte[elementno] += element.count(letter)
        elementno += 1

    letterno += 1

def fnc(e):
    try:
        return punkte[elemente.index(e)]
    except:
        pass

elemente.sort(key=fnc)

print(elemente)

# elementno = 0
# for element in punkte:
#     print(f"\"{elemente[elementno]}\": {element}")
#     elementno += 1