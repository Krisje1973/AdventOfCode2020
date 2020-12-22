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
    #first_star()
    second_star()        

def play():
    global p1,p2   
    while len(p1)>0 and len(p2)>0:       
        if p1[0] > p2[0]:
            p1.append(p1[0])
            p1.append(p2[0])
        else: 
            p2.append(p2[0])
            p2.append(p1[0])
        p1.pop(0)
        p2.pop(0)

def play2(p1,p2):   
    seen = set()
    cnt=0
    while len(p1)>0 and len(p2)>0:
        cnt+=1
        # Played before: p1 wins
        label = tuple(p1), tuple(p2)
        if label in seen:
            p2.clear()
            return p1,p2
        seen.add(label)

        # Combat 
        c1, *p1 = p1
        c2, *p2 = p2
        if c1 <= len(p1) and c2 <= len(p2):   
            r1,r2 = play2(p1[:c1],p2[:c2])
            wp= len(r1)>0 
        else: wp=c1>c2

        if wp:
            p1.append(c1)
            p1.append(c2)
        else: 
            p2.append(c2)
            p2.append(c1)
    
    return p1,p2
    
def first_star():  
    tot = 0
    play()   
    p=p1
    if len(p1) == 0: p=p2
    c=len(p)
    for i,v in enumerate(p):
        tot += (c-i) * v

    print("Result First Star")   
    print(tot)
def second_star():
    # 29495 to low ...
    # 36215 to high
    global p1,p2
    tot=0
    p1,p2 = play2(p1,p2)   
    p=p1
    if len(p1) == 0: p=p2
    c=len(p)
    for i,v in enumerate(p):
        tot += (c-i) * v
    print("Result Second Star")   
    print(tot)
if __name__ == '__main__':
    main()