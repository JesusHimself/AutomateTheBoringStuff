#!python3

#Strong password contains: at least eight characters
#both uppercase and lowercase
#at least one digit

import pyperclip, re

password = str(pyperclip.paste())

passwordRegex = re.compile()

def pw_detection(pw):
    if len(pw) < 8:
        return False
    elif re.search('[0-9]', pw) is None:
        return False
    elif re.search('[A-Z]', pw) is None:
        return False
    elif re.search('[a-z]', pw) is None:
        return False
    else:
        return True

if __name__ == '__main__':
    pw = input('Enter your password: ')
    if password_detection(pw):
        print('Good, your password is strong.')
    else:
        print('The password is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.')