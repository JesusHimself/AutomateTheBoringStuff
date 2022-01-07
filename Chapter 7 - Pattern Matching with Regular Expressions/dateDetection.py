#!python3

"""
This program is written as part of the course: Automate the boring stuff with Python
Function of program: Detect dates in a text
Author: Nick Visser
Date: 11/11/2021 (dd/mm/yyyy)
"""
import pyperclip, re

dateRegex = re.compile(r'''(
    [0-3][0-9]           # day
    /                    # separator
    [0-1][0-9]           # month
    /                    # separator
    [1][0-9][0-9][0-9]   # year
    )''', re.VERBOSE)

# copy the text from the clipboard
text = str(pyperclip.paste())
text = '24/03/1992   dfg  28/04/1993'
matches = []

for groups in dateRegex.findall(text):
    matches.append(groups)

#join the matches into a string for the Clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
