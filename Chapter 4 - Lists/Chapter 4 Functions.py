spam = ['apples', 'bananas', 'tofu', 'cats']

#Function puts all items of lists or tuple in a string seperated by comma's
def liststring(List):
    if list and isinstance(List, list) or isinstance(List, tuple):
        wordString = ''
        for i in range(len(List)):
            if i != len(List) - 1:
                wordString += List[i] + ', '
            else:
                wordString += List[i]
        print(wordString)
    else:
        print('ERROR: This list does not contain any items or is not a list or tuple.')

liststring(spam)
