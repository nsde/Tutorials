users = []
pws = []
inp = ''

def login():
    print(users)
    print(pws)
    user = inp.split()
    if user in users:
        id = users.index(user)
        print('Type in password')
        pw = input('>')
        if pws[id] == pw:
            print('Logged in. Welcome,',user)
        else:
            print('Wrong password.')
    else:
        print('Error.')

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
        print(f'[ERROR] User {user} not found.')

while 1:
    print('login <user> or create <user>')
    inp = input('>')
    if inp.startswith('login'):
        login()
    else:
        create()
