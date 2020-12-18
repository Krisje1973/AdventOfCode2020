import os, sys
import operator
from itertools import *
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 

input=[]
file = FileHelper()
def readinput():
    global input
    input = file.readinput_lines_and_replace(r"Day17\input_ex.txt",[[".","0"],["#","1"]])
    

def main():
    readinput()
    first_star()
    second_star()        

def run_cycle(source):
    source.append([0 for s in range(len(source[0]))])
    for pock in source:
        new_pock = [0].append(pock).append([0])
        x,y,pock = pock
    

        print(source[pock][2])

def first_star():  
    # active    = if 2 or 3 neighbors  active dan inactive
    # nonactive = if exactly 3 neighbors  active  dan active 
    deltas_3d = []

    for z in range(3):
        for y in range(3):
            for x in range(3):
                if (x - 1) != 0 or (y - 1) != 0 or (z - 1) != 0:
                    deltas_3d.append( (x - 1, y - 1, z - 1) )

    size: int = 25
    offset: int = size // 2
    world = [ [ [0 for _ in range(size)] for _ in range(size)] for _ in range(size)]

    for y, line in enumerate(input):
        for x, pos in enumerate(line):
            world[0 + offset][y + offset][x + offset] = pos

    
    for line in [line in world]:
        print(sum(line))

   
    print("Result First Star")   
    
def second_star():
   
       
    print("Result Second Star")   
    
if __name__ == '__main__':
    main()