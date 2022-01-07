from typing_extensions import IntVar
import pyinputplus as pyip

#response = pyip.inputInt(prompt='Enter a number: ')

#you can also use regexes to limit the inputs that are accepted
response = pyip.inputNum(allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
print(response)


def addsUpToTen(numbers):
    #list function splits the string and puts every character in a list
    numbersList = list(numbers)
    
    #convert strings in the list to ints
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %(sum(numbersList)))
    return int(numbers)
response = pyip.inputCustom(addsUpToTen)
    


pyip.inputCustom()