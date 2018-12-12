#!/usr/bin/python

#Dekai Rohlsen
#U50753261


def displayInventory(inventory):

	total = 0
	for number in inventory.values():
		total = total + number
	
	print("Inventory: ")
	for item in inventory.keys():
		
		print("{1} {0}" .format(item, inventory[item]))
		
	print("Total number of items: {0} \n\n" .format(total) )



def addToInventory(inventory, addItems):
	
	temp = set(addItems)
	temp = list(temp)
	
	for i in range(0,len(temp)):
		if temp[i] in inventory.keys(): 
			inventory[temp[i]] = inventory.get(temp[i], 0) + addItems.count(temp[i])
			
		else:
			inventory[temp[i]] = addItems.count(temp[i])
			

if __name__ == "__main__":


	my_pack = {"arrow":12,"gold coin":42,"rope":1,"torch":6,"dagger":1}
	dragonLoot = ["gold coin","dagger","gold coin","gold coin","ruby"]	
	
	print("\nBefore addition \n")	
	displayInventory(my_pack)
	print("Look what I found!")
	print(dragonLoot)
	
	print("\n\nAfter addition \n")	
	addToInventory(my_pack, dragonLoot)
	displayInventory(my_pack)
