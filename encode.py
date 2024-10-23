# encode by megha ramprasad

def encode(pw):
    string = ''
    for item in pw[0:9]:
        string += str((int(item[0]) + 3) % 10)
    return str(string)

if __name__ == "__main__":
        password = ''
        while True:
            print(' ')
            print('Menu')
            print('-------------')
            print('1. Encode')
            print('2. Decode')
            print('3. Quit')
            print(' ')
            option = int(input('Please enter an option: '))
            if option == 1:
                password = input('Please enter a password to encode: ')
                password = encode(password)
                print('Your password has been encoded and stored!')
            elif option == 2:
                print('The encoded password is '+ str(password) + ', and the original password is ' + str(decode(password) + '.'))
            elif option == 3:
                break