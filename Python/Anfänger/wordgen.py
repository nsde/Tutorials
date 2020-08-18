# simple word generation using syllables
# silben-generation

from random import randint as rdi
from random import choice as c

l = 'dfklmprtw' # letters (prefixes of the syllables)
v = 'aeiou'# vocals (suffixes of the syllables)

min_gen = 2 # minimum syllables per word
max_gen = 4 # maximal syllables per word

word_count = 10 # no. of words to generate

def word():
    for _  in range(rdi(min_gen,max_gen)):
        print(end=c(l) + c(v)) # choose random and generate

for _ in range(word_count):
    word()
    print(end='\n')