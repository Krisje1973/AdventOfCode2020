import os, sys
import operator
from itertools import *
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 

data=[]
pocket=defaultdict(int)
file = FileHelper()
def readinput():
    global data
    data = file.readinput_lines_and_replace(r"Day17\input.txt",[[".","0"],["#","1"]])
   
def main():
    readinput()
    first_star()
    second_star()        

def cycle_cubes():
    global pocket
    off = [(x, y, z) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2) if not x == y == z == 0]
    neigb = set((x + dx, y + dy,z + dz) for x, y, z in pocket.keys() for dx, dy, dz in off)
    
    new_pocket = defaultdict(int)
    cp = pocket.copy()
    for n in neigb:
        if n not in pocket:
            pocket[n] = 0

    for p in pocket:
        ne=0
        for n in off:      
            ne+= cp[p[0]+n[0],p[1]+n[1],p[2]+n[2]]

        if pocket[p]:
            if ne in [2,3]: 
                new_pocket[p] = 1
            else:
               new_pocket[p] = 0 

        if not pocket[p] and ne == 3: 
            new_pocket[p] = 1
   
    pocket=new_pocket
  
def first_star():  
    # active    = if 2 or 3 neighbors active dan inactive
    # nonactive = if exactly 3 neighbors  active  dan active 
    global pocket
    for y,d in enumerate(data):
        for x,p in enumerate(d):
            pocket[(x,y,0)] = int(p) 
    
    for _ in range(6):
        cycle_cubes()
    
    print("Result First Star")   
    print(sum(pocket.values()))
def second_star():
     
    print("Result Second Star")   
    
if __name__ == '__main__':
    main()