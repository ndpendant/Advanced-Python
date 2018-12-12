#!/usr/bin/python

#Dekai Rohlsen
#U50753261

def collatz(number):
	

	if number is 1:
		return(True)

	elif number % 2 is 0:
		val = int(number / 2)		
		print(val)
		return (collatz(val))
	
	else:
		val = int(3 * number + 1)
		print(val)
		return(collatz(val))



def collatz_sequence():
	
	added = input("Enter number: ")

	try:
		int(added)
	except:
		print("Invalid input: must be an integer")
		return(False)
	print(int(added))
	return(collatz(int(added)))


if __name__ == "__main__":

	status = False
	while status is False:
		value = collatz_sequence()
		if value is True:
			status = True
	
	
