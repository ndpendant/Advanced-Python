#!/usr/bin/python

import argparse
import os
import sys

#Dekai Rohlsen
#U50753261

def mad_libs(inputname,outputname):
    
    out = []
    old = []
 
  
    
    old_file = open(inputname,'r')
    output = open(outputname,'w')
    
    for line in old_file:
        old.append(line)
        line = line.split(" ")
       
  
        for i in range(0,len(line)):
            if "ADJECTIVE" in line[i]:
                adjective = input("Enter adjective: ")
                line[i] = line[i].replace("ADJECTIVE",adjective)
      
            if "NOUN" in line[i]:
                noun = input("Enter noun: ")
                line[i] = line[i].replace("NOUN",noun)
        
            if  "VERB" in line[i]:
                verb = input("Enter verb: ")
                line[i] = line[i].replace("VERB",verb)
        
        line = " ".join(line)
        out.append(line)

    print("\n This is your old text: \n\n")

    for item in old:
        print(item)
    
    print("\n This is your new text: \n\n")
          
    for item in out:
        output.write(item)
        print(item)

        
if __name__ == "__main__":

    my_file = input("Enter the name of your desired file to be read (with extention): ")
    new_file = input("Enter the name of the new file to be saved (with extention): ")
    print("\n\n")
      
    mad_libs(my_file,new_file)
