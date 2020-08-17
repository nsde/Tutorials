# local singleplayer ttt

from random import randint as rdi
import sys

l = ['-','-','-','-','-','-','-','-','-']

end = False
player = 0

def run():
    global player

    if player == 1:
        player = 2
        playersymbol = 'X'
    else:
        player = 1
        playersymbol = 'O'

    for i in range(9):
        print(end=l[i])
    print(end='\n')

    inp = input(f'\n[P{player}] ')
    l[int(inp)+1] = playersymbol

# print tictactoe

while 1:
    if end:
        sys.exit(0)
    else:
        run()
