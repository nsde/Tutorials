# simple word generation using syllables
# silben-generation

from random import randint as rdi

s = 'dfgklmprtw' # "easy" words

def word():
    for _  in range(rdi(4,8)):
        print(end=s)

for _ in range(10):
    word()
    print(end='\n')