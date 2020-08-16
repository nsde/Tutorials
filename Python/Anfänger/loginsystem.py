from random import randint as rdi

users = []
pws = []
global id
id = 99999
inp = ''
notes = []

def login():
    user = inp.split()
    user = user[1]
    if user in users:
        id = users.index(user)
        print('Type in password')
        pw = input('>')
        if pws[id] == pw:
            print(f'Logged in as id {id}. Welcome, "{user}"!')
        else:
            print('Wrong password.')
    else:
        print(f'[ERROR] User "{user}" not found.')

def create():
    user = inp.split()
    user = user[1]
    print(user)
    if not user in users:
        print('Type in password')
        pw = input('>')
        if pw in pws or len(pw) < 5:
            print('Password is not strong enough.')
        else:
            users.append(user)
            pws.append(pw)
            print('User created. Please log in.')

    else:
        print(f'[ERROR] Name "{user}" already exists. What about "{user}{rdi(0,999)}"?')

def logout():
    user = ''
    pw = ''
    id = 9999
    return user, pw

def editnote():
    note = inp.split()
    note = note[1]
    try:
        id = int(id)
        notes[id] = note
    except:
        print('[ERROR] Sorry, you don\'t have the permissons to edit your note.')

def readnote():
    try:
        id = int(id)
        note = notes[id]
        print(f'Your note:\n"{note}".')
    except:
        print('[ERROR] Sorry, you don\'t have access to your notes.')


while 1:
    print('===[HELP]===\nCommands:\nlogin <user>\tlogin to an existing account\
        \ncreate <user>\tcreate a new user\nlogout\t\tlog out from your account\
        \neditnote\tedit your note\
        \nreadnote\tread your note\n=========')
    inp = input('>')
    if inp.startswith('login'):
        login()
    elif inp.startswith('create'):
        create()
    elif inp.startswith('logout'):
        logout()
    elif inp.startswith('editnote'):
        editnote()
    elif inp.startswith('readnote'):
        readnote()
    else:
        print(f'[ERROR] Command "{inp}" not found.')
