import pprint

#This part of the code is to explain dictionaries
def birthday():
    birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
    while True:
        print('Enter a name: (blank to quit)')
        name = input()
        if name == '':
            break
        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else:
            print('I do not have birthday information for' + name)
            print('What is their Birthday?')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated')
 
# This part explains the keys(), values() and items() methods
def methods():
    spam = {'colour': 'red', 'age': '42'}
    for v in spam.values():
        print(v)
    for k in spam.keys():
        print(k)
    for i in spam.items():
        print(i)
    
    #You van use the multiple assignment trick in a for loop to assign the key and value to seperate variables:
    for k,v in spam.items():
        print('Key: ' + k + ' Value: ' + str(v))

#This algorithm shows how to count how often a character apears in a sentence:
def countchar():
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count = {}
    for character in message:
        count.setdefault(character,0)
        count[character] = count[character] + 1
    print(count)

#This algorithm does the same as the above one exept it prints nicer using the pprint library
def prettyprint():
    message = 'It was a bright cold day in April, and the clocks were striking thirteen'
    count = {}
    
    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    pprint.pprint(count)
    
#This algorithm plays Tic-Tac-Toe
def printboard(theBoard):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print(board)

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
        'mid-L': ' ', 'mid-M': 'X', 'mid-R': ' ',
        'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
turn = 'X'
for i in range(9):
    printboard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    
    if turn == 'X':
        turn = 'O'

    else: 
        turn = 'X'
print(theBoard)