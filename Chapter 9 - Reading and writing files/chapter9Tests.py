#!python3

from pathlib import Path
import shelve

helloFile = open(Path.cwd() / 'spam.txt')
helloContent = helloFile.read()
print(helloContent)

sonnetFile = open(Path.cwd() / 'sonnet29.txt')
print(sonnetFile.readlines())

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello, World!\n')

baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')

baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
