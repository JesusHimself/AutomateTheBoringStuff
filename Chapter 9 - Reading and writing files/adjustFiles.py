#!python3
#This program replaces ADJECTIVE, NOUN, ADVERB or VERB in a text file
from os import close, write
from pathlib import Path
import pyinputplus as pyip
import os.path
import re

#Ask user if the file they want to adjust is in the current working directory
originalCWD = pyip.inputYesNo(f"Do you want to adjust a file in the current working directory ({Path.cwd()})?\n")

if originalCWD == 'yes':
    originalFile = Path(os.path.join(Path.cwd(), pyip.inputStr("Type in the name of the file + extension: ")))
    fileExsists = os.path.isfile(originalFile)

#ask user for filepath if file is not in current working directory
else:
    originalFile = Path(pyip.inputFilepath("What file path and file would you like to adjust?\n"))
    fileExsists = os.path.isfile(originalFile)

#This part of the code will adjust the file as wanted
if fileExsists and originalFile.suffix == '.txt':
    newFile = open(f"{originalFile.stem}Adjusted{originalFile.suffix}", "w")
    originalFile = open(originalFile)
    
    replaceWords = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
    
    with newFile as fileWrite, originalFile as fileRead:
        for line in fileRead:
            fileWrite.write(line)

#WRITE THE ALGORITHM TO REPLACE THE WORDS!!
             
else:
    print("The file that you want to adjust does not exist of filetype is not supported")