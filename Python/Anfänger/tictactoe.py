# local singleplayer ttt

from random import randint as rdi
import sys

# standard ttt list
l = ['-','-','-','-','-','-','-','-','-']

end = False
player = 0

def run():
# player settings
    global player
    if player == 1:
        player = 2
        playersymbol = 'X'
    else:
        player = 1
        playersymbol = 'O'

# print
    item = 0
    for _ in range(3):
        for _ in range(3):
            print(end=l[item])
            item += 1
        print(end='\n')
    print(end='\n')

# input
    inp = input(f'\n[P{player}] ')
    try:
        if l[int(inp)-1] == '-':
            l[int(inp)-1] = playersymbol
        else:
            print('REPLACE ERROR - Replacing is against the rules of TicTacToe!')
    except:
        print('INPUT ERROR - Input is a invalid number!')

# loop
while 1:
    if end:
        sys.exit(0)
    else:
        run()
