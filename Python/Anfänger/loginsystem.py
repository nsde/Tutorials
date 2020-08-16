from random import randint as rdi

users = []
pws = []
inp = ''
notes = []

def login():
    print(users)
    print(pws)
    user = inp.split()
    user = user[1]
    if user in users:
        id = users.index(user)
        print('Type in password')
        pw = input('>')
        if pws[id] == pw:
            print(f'Logged in. Welcome, "{user}"!')
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
    return user, pw

def note():
    pass

def readnote():
    try:
        print('')
    except:
        print('[ERROR] Sorry, you don\'t have access to your notes.')


while 1:
    print('login <user> or create <user>')
    inp = input('>')
    if inp.startswith('login'):
        login()
    elif inp.startswith('create'):
        create()
    elif inp.startswith('logout'):
        logout()
    elif inp.startswith('createnote'):
        note()
    elif inp.startswith('readnote'):
        readnote()
    else:
        print('[ERROR] Command not found.')
