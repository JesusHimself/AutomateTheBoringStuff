import sys

def collatz(number):
    try:
        if (number%2) == 0:
            return number // 2
        elif (number%2) == 1:
            return 3 * number + 1
    except ValueError:
        print('Error: Input was not an integer')
        sys.exit
        
try:
    number = int(input('Give us an integer: '))
    
    while True:
        if number != 1:
            number = collatz(number)
            print(number)
        else:
            break
        
except ValueError:
    print('Error: Input was not an integer')
    sys.exit
        