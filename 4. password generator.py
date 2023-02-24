#Password Generator

import random

def generate_password():
    digits = ['1','2','3','4','5','6','7','8','9','0']

    lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z']

    uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                        'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                        'Z']

    symbols = ['@','.','$','#','&','%','*']

    print('Note: Length of password must be between 8 to 15')
    n = int(input('Enter length of password: '))

    if n>=8 and n<=15:
        choice = digits + lowercase_letters + uppercase_letters + symbols
        password = []
        temp_password = random.choice(digits)\
                        + random.choice(lowercase_letters)\
                        + random.choice(uppercase_letters)\
                        + random.choice(symbols)

        for i in range(n-4):
            temp_password += random.choice(choice)
        password.append(temp_password)
        print('Your password is {}'.format(*password))

    else:
        print("Invalid length od password! Try again.")
        generate_password()

if __name__ == '__main__':
    generate_password()