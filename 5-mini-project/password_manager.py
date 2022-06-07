from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
'''


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key


master_password = input('What is the master password? \n')

key = load_key() + master_password.encode()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            # print(line.rstrip())
            user, password = line.rstrip().split('|')
            print(
                f'User: {user} | Password: {fer.decrypt(password.encode()).decode()}')


def create():
    name = input('Account Name: \n')
    password = input('Password: \n')

    with open('passwords.txt', 'a') as f:
        f.write(f'{name}|{fer.encrypt(password.encode()).decode()}' + '\n')


while True:
    mode = input(
        'Do you want to (create) create a new password or (view) view existing password. q to quit ? \n')
    if mode == 'q':
        break
    elif mode == 'create':
        create()
    elif mode == 'view':
        view()
    else:
        print('Not a valid options. Please try again !')
        continue
