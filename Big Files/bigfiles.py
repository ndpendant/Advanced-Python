# !/usr/bin/python

import os


#Dekai Rohlsen



def bigfiles(basepth):


	files = (os.walk(basepth))
	

	for name in files:
		name = list(name)

		for i in range(0,len(name[2])):
			temp = name[0]+"/"+name[2][i]
			tsize = os.path.getsize(temp)
			if tsize / 1000000 > 100:
				 
				print(temp)
					
	






if __name__ == "__main__":
	
	bp = input("Enter the basepath: ")
	bigfiles(bp)
