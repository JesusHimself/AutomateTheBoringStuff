#!python3
import pyinputplus as pyip


while True:
    response = pyip.inputYesNo('Want to know how to keep an idiot busy for hours?\n')
    
    if response == 'no':
        print('Thank you, have a nice day!')
        break