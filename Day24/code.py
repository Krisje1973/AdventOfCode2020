import os, sys
import operator
import collections 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 
import re

data=[]
def readinput():
    global data
    helper = FileHelper()   
    data = helper.readinput_lines(r"Day24\input.txt")
    
def main():
    readinput()
    first_star()
    second_star()        

def first_star():   
    # Ex: 10 tiles are black.
    comp = Compass()
    hp = comp.hexaspoints
    
    grid=set()
    for line in data:
        pos=""
        po=[]
        for co in [c.upper() for c in line]:
            pos+=co
            if pos in hp.keys():
                po.append(hp[pos])
                pos=""
        x,y=0,0 
        for co in po:
            x+=co[0]
            y+=co[1]
        
        c=x*1000+y
        if c not in grid:
            grid.add(c)  
        else: grid.remove(c)
            
    
    print("Result First Star")  
    print(len(grid)) 
  
def second_star():
    global data
   
    print("Result Second Star")   
if __name__ == '__main__':
    main()