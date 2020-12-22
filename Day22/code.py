import os, sys
import operator
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 
import re

data=[]
p1,p2=[],[]
def readinput():
    global data
    global p1,p2
    helper = FileHelper()   
    data = readinput_lines(r"Day22\input.txt")
    a,b = helper.get_arrays_from_separator(data," ")
    for i in a[1:]:
        p1.append(int(i))
    for i in b[1:]:
        p2.append(int(i))
def main():
    readinput()
    first_star()
    second_star()        

def play():
    global p1,p2   
    while len(p1)>0 and len(p2)>0:       
        if p2[0] == 10:
             p2[0] == 10
        if p1[0] > p2[0]:
            p1.append(p1[0])
            p1.append(p2[0])
        else: 
            p2.append(p2[0])
            p2.append(p1[0])
        p1.pop(0)
        p2.pop(0)
    
    

def first_star():  
    tot = 0
    play()   
    p=p1
    if len(p1) == 0: p=p2
    c=len(p)
    for i,v in enumerate(p):
        tot += (c-i) * v

    print(tot)
    print("Result First Star")   
   
def second_star():

    print("Result Second Star")   

if __name__ == '__main__':
    main()