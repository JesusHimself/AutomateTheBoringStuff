#!python3

""" 
This code is written as part of the course: Automate the boring stuff
Chapter: 7 
Project: Phone Number and Email Address Extractor
"""

import pyperclip, re

#steps:
# 1. Copy text off clipboard
# 2. Create regexes for: matching phone number and email adresses
# 3. Paste text on clipboard

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code (optional)
    (\s|-|\.)?                        # separator (optional)
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator (- or .)
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension 
    )''', re.VERBOSE)

emailRegex = re.compile(r'''( 
    [a-zA-Z0-9._%+-]+   #username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      #domain name
    (\.[a-zA-Z]{2,4})   #dot-something
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]]) #groups[0] matches entire expression
    
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
    
for groups in emailRegex.findall(text):
    print(groups)
    matches.append(groups[0])
    
#join the matches into a string for the Clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
