
Inventory Assignment

Python Features Required: Basic python, print, user defined functions, dictionaries

File(s) to Submit: inventory.py

Specification:
You are creating a fantasy video game and will need a data structure to model a player’s inventory. You will use a dictionary where the keys are string values describing the item in the inventory and the value is an integer value specifying how many of that item the player has.

For example, the dictionary value
{'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}
means the player has 1 rope, 6 torches, 42 gold coins, and so on.
In the file inventory.py, you are to write the code for the two functions described below.

1. displayInventory(inventory), where the inventory parameter is a dictionary representing the player’s inventory and displays it like the following:

Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger

Total number of items: 62

Hint: You can use a for loop to loop through all the keys in a dictionary, or through all the items in the dictionary.

List to Dictionary Function for Fantasy Game Inventory

2. addToInventory(inventory, addedItems), where the
inventory parameter is a dictionary representing the player’s inventory
and the addedItems parameter is a list of newly acquired loot.
The addToInventory() function should return a dictionary that represents the
updated inventory. Note that the addedItems list can contain multiples of the
same item.

Execution of the code

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin',
'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

should produce the output
Inventory:
45 gold coin
1 rope
1 ruby
1 dagger
Total number of items: 48
