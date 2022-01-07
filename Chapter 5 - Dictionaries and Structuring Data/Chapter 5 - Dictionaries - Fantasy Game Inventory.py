import pprint

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby']

#This function displays the items in an inventory
def displayInventory(inventory):
    try:
        numitems = 0
        print('Inventory: ')
        for i, j in inventory.items():
            print(str(j) +' ' + i)
            numitems += j
        print('Total number of items: ' + str(numitems))
    except:
        print('Please give in a dictionary as input')

#This function adds items to an inventory
def addToInventory(inventory, addedItems):
     for items in addedItems:
        if items in inventory.keys():
            inventory[items] += 1
        else:
            inventory[items] = 1

displayInventory(stuff)
addToInventory(stuff, dragonLoot)
displayInventory(stuff)
