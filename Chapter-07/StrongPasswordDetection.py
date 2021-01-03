import re,sys

def strongPasswordDetection(password):
    lengthRegex = re.compile(r'(.{8,})') 
    lowercaseRegex = re.compile(r'[a-z]+') 
    uppercaseRegex = re.compile(r'[A-Z]+')
    numbersRegex = re.compile(r'[0-9]+')

    if lengthRegex.search(password)==None:
        print('NOT STRONG: Password length must atleast be eight.')
    elif numbersRegex.search(password)==None:
        print('NOT STRONG: Password must contain atleast one Numeric Character.')
    elif uppercaseRegex.search(password)==None:
        print('NOT STRONG: Password must contain atleast one uppercase alphabet')
    elif lowercaseRegex.search(password)==None:
        print('NOT STRONG: Password must contain atleast one lowercase alphabet')
    else:
        print('STRONG: Password is strong')

password=input('Set a password: ')
strongPasswordDetection(password)