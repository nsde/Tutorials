# local singleplayer ttt

from random import randint as rdi
import sys

l = ['-','-','-','-','-','-','-','-','-']

end = False

def run():
    for row in range(3):
        for col in range(3):
            print(end=l[col])
        print(end='\n')

    inp = input('\n>')

    try:
        inp = int(inp)
        if inp > -1 and inp < 9:
            pass
        else:
            print(Error)

    except:
        if inp == 'end':
            end = True
            return end
        else:
            print('ERROR')

# print tictactoe

while 1:
    if end:
        sys.exit(0)
    else:
        run()
