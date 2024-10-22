# encode by megha ramprasad

def encode(encode_pw):
    encode_pw = ''
    for item in range(len(encode_pw)):



def main():
    password = ' '
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print(' ')
        option = print(input('Please enter an option: '))
        if option == 3:
            break
        elif option == 1:
            str = input('Please enter a password to encode: ')
            password = encode(str)
            print('Your password has been encoded and stored!')
        elif option == 2:
            print('The encoded password is', password, 'and the original password is', decode(password))



