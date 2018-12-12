#!/usr/bin/python

import argparse
import os
import sys

#Dekai Rohlsen
#U50753261

def printtable(L):
    
    cap = 0
    count = len(L)
    
    for i in range(0,count):
        temp = L[i]
        biggest = max(temp,key=len)
        if len(biggest) > cap:
            cap = len(biggest)
        
    
    for j in range(0,count):
        for k in range(0,len(L[j])):
            a = L[j][k].rjust(cap, " ")
            L[j][k] = a
            
    

    for i in range(0,len(L[0])):
        hold = []
        for j in range(0,count):
            hold.append(L[j][i])
        new = "".join(hold)
        print(new)
   
    
          
if __name__ == "__main__":

    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    new_lists = []
    
    while True:
        lst = input("Enter list separated by space (when finished type 'done'): ")
        lst = lst.split(" ")
        if "done" in lst:
            break
        new_lists.append(lst)
    printtable(new_lists)
