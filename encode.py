# encode by megha ramprasad

def encode(pw):
    string = ''
    for item in pw[0:9]: # limits 8 digits
        string += str((int(item[0]) + 3) % 10) # accepts the first number, adds 3, and mod 10, returns first number + 3
    return str(string)

if __name__ == "__main__":
        password = ''
        while True: # menu
            print(' ')
            print('Menu')
            print('-------------')
            print('1. Encode')
            print('2. Decode')
            print('3. Quit')
            print(' ')
            option = int(input('Please enter an option: '))
            if option == 1:
                password = input('Please enter a password to encode: ') # encodes user input
                password = encode(password)
                print('Your password has been encoded and stored!')
            elif option == 2: # takes the encoded password from first option & then decodes the password into the user's original input
                print('The encoded password is '+ str(password) + ', and the original password is ' + str(decode(password) + '.'))
            elif option == 3: # end
                break