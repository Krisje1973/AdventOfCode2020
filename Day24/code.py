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
    #first_star()
    second_star()        

def get_tiles():
    comp = Compass()
    hp = comp.hexaspoints
    
    tiles = defaultdict(int)
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
        
        tiles[(x,y)] ^= 1
    
    return tiles
  
    
def first_star():   
    
    # Ex: 10 tiles are black.
    print("Result First Star")  
    print(sum(get_tiles().values())) 
  
def second_star():
    """
    Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
    Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
    
    = Add borders to see the white neigbourgs
    """
    comp = Compass()
    hp = comp.hexaspoints
    tiles=get_tiles()
    borders = set()
    for _ in range(100):
        for x, y in tiles.keys():
            for bx,by  in hp.values():
                borders.add((x+bx,y+by))
       
        new_tiles = defaultdict(int)
        for x, y in borders:
            old = tiles[(x, y)]
            neig = sum(tiles[x + dx, y + dy] for dx, dy in hp.values())
            # Zero or more
            if old == 1 and neig not in [1, 2]:
                new_tiles[x, y] = 0
            elif old == 0 and neig == 2:
                new_tiles[x, y] = 1
            else:
                new_tiles[x, y] = old

        tiles = new_tiles   
    
    print("Result Second Star")   
    print(sum(tiles.values())) 
   
    
if __name__ == '__main__':
    main()