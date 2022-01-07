import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
        
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

def phoneNumRegexample():
    phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
    #phoneNumRegex = re.compile(r'(\d{3}))-(\d{3}-\d{4})')

    mo = phoneNumRegex.search('My number is: (415)-555-4242')
    print('Phone number found: ' + mo.group())

def batMan():
    batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
    mo = batRegex.search('Batmobile lost a wheel')
    print(mo.group())
    print(mo.group(1))
    
    #You can also search for an optional group by using the ? sign.
    #as seen under here:
    batRegex = re.compile(r'Bat(wo)?man')
    mo1 = batRegex.search('The Adventures of Batwoman')
    print(mo1.group())
    
def characterClass():
    xmasRegex = re.compile(r'\d+\s\w+')
    xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

#this function shows how to create your own character class.
#this specific one finds all the vowels in a sentence.
def ownCharClass():
    #you can also include ranges like: [a-zA-Z0-9]
    #if you want to find everything EXEPT certain parts you van use the ^sign
    #[^aeiouAEIOU]
    vowelRegex = re.compile(r'[aeiouAEIOU]')
    mo = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
    print(mo)

#This function shows how to only search in the beginning or end of a text
def beginningOrEnd():
    beginsWithHello = re.compile(r'^Hello')
    #This returns the span and that it's found
    mo = beginsWithHello.search('Hello, world!')
    print(mo)
    #This returns None
    mo = beginsWithHello.search('He said hello.')
    print(mo)

    #It can also be done for numbers (the dollar sign says number has to be at the end)
    endsWithNumber = re.compile(r'\d$')
    mo = endsWithNumber.search('Your number is 42')
    print(mo)
    
    # to check if the whole string is a num:
    wholeStringIsNum = re.compile(r'^\d+$')
    mo = wholeStringIsNum.search('1234567890')
    print(mo)
    #this prints a None value
    mo = wholeStringIsNum.search('12345xyz67890')
    print(mo)
    
# this function shows the use of the wildcard character (dot sign)
def wildCard():
    #this means that the compile will look inside a sentence for 3 letter
    # ending in at (so it won't find the whole 'flat', it will result in 'lat')
    atRegex = re.compile(r'.at')
    atRegex.findall('The cat in the hat sat on the flat mat')
    
def matchEverything():
    #This function will return everything after First name and last name
    nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
    mo = nameRegex.search('First Name: Al Last Name: Sweigart')
    print(mo.group(1))
    print(mo.group(2))

#This functions shows how to make your regexes case insensitive
def caseInsensitive():
    regex1 = re.compile('RoboCop')
    regex2 = re.compile('ROBOCOP')
    regex3 = re.compile('robOcop')
    regex4 = re.compile('RobocOp')
    
    # the re.I argument makes sure that the regex search is case insensitive
    robocop = re.compile(r'robocop', re.I)
    print (robocop.search('RoboCop is a part man, part machine, all cop.').group())

#substitution strings
def subStrings():
    namesRegex = re.compile(r'Agent \w+')
    print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))
    
    #you can also censor by only showing the first letter:
    agentNamesRegex = re.compile(r'Agent (\w)\w*')
    print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))
    
    
subStrings()



