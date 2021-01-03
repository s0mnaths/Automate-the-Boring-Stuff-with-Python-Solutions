def printTable(listOfLists):
    for i in range(0,4):
        for j in range(len(listOfLists)):
            print(listOfLists[j][i].ljust(20),end='')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)