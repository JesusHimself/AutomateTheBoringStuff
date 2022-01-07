tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    #Find longest string in each of inner list
    colWidths = [0] * len(table)
    for i in range(len(table)):
        stringlength = 0
        for j in range(len(table[0])):
            if stringlength < len(table[i][j]):
                stringlength = len(table[i][j])
        colWidths[i] = stringlength
    
    #print data in the right order
    for i in range(len(table[i])):
        for j in range(len(table)):
            print(table[j][i].rjust(colWidths[j]), end = ' ')
        print()
                  
printTable(tableData)