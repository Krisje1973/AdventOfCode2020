import os, sys
import operator
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 
import re
import math
from itertools import * 

data=[]
tiles={}
def readinput():
    global data
    global tiles
    helper = FileHelper()
    data = helper.readinput_lines_and_replace(r"Day20\input.txt",[[".","0"],["#","1"]]) 
    arr = helper.get_arrays_from_separator(data,"")
    for ar in arr:
        no = ar[0].split(":")[0].replace("Tile ","")
        tile = Tile()
        tile.lines=ar[1:]
        tile.no=no
        tile.calc_borders()
        tiles[no] = tile
    # To flip: 0--9,1-8,2-7,3-6

class Tile():
    no,l,t,r,b,lr,tr,rr,br=[0,0,0,0,0,0,0,0,0]
    lines=[]
    rn,ln,tn,bn=0,0,0,0
    neigborgs = {}
    corners=set()
    r_corners=set()
    def calc_borders(self):
        helper = Binary()
        self.t=helper.get_int_from_binary_string(self.lines[0])
        self.tr=helper.get_int_from_binary_reversed_string(self.lines[0])
        self.b=helper.get_int_from_binary_string(self.lines[9])
        self.br=helper.get_int_from_binary_reversed_string(self.lines[9])
        l,r="",""
        for line in self.lines:
            l+= line[0]
            r+= line[9]

        self.l = helper.get_int_from_binary_string(l)
        self.lr = helper.get_int_from_binary_reversed_string(l)
        self.r = helper.get_int_from_binary_string(r)
        self.rr = helper.get_int_from_binary_reversed_string(r) 
        self.corners = set(combinations_with_replacement([self.t,self.r,self.b,self.l],2))
        self.r_corners = set(combinations_with_replacement([self.tr,self.rr,self.br,self.lr],2))

    def rotate(self):
        t,tr,r,rr,b,br,l,lr = self.r,self.rr,self.b,self.br,self.l,self.lr,self.t,self.tr
        self.t,self.tr,self.r,self.rr,self.b,self.br,self.l,self.lr = t,tr,r,rr,b,br,l,lr 
    
def main():
    readinput()
    #first_star()
    second_star()        

def first_star():  
    tot = 1
    for t in tiles:        
        tile = tiles[t]
        find_neigborgs(tile)       
        if tile.tn==6: 
            tot *= int(t)

    print("Result First Star")  
    print(tot) 

def find_neigborgs(tile):
    corners = [tile.t,tile.b,tile.l,tile.r]
    for t in tiles:
        c=tiles[t]      
        for corner in corners:          
            if c.t == corner or c.tr == corner or c.b == corner or c.br == corner or c.l==corner or c.lr == corner or c.r==corner or c.rr==corner: 
                tile.tn+=1  
                tile.neigborgs[t]=c.tn  

def find_candidates(tile,tiles):
    cand = {}
    c1 = tile.corners.copy()
    r1 = tile.r_corners.copy()
    for t in filter(lambda w: not w == str(tile.no), tiles):
        c2= tiles[t].corners.copy()
        r2= tiles[t].r_corners.copy()
        if c1&c2:
            cand[t]=tiles[t]
        if c1&r2:
            cand[t]=tiles[t]
        if r1&c2:
            cand[t]=tiles[t]
        if r1&r2:
            cand[t]=tiles[t]
    
    return cand

def find_corners_sides(tiles):
    corners={}
    sides = {}     
    for t in tiles:        
        tile = tiles[t]
        find_neigborgs(tile)    
        if tile.tn==6: 
           corners[t] =tile
        if tile.tn==7: 
            sides[t] = tile

    return corners,sides

def second_star():
    """corners=[]
    for t in tiles:        
        tile = tiles[t]
        find_neigborgs(tile)    
        if tile.tn==6: 
           corners.append(tile)

    sides = {}     
    for tile in [corners[0]]:
        for neig in tile.neigborgs:
            if tile.neigborgs[neig] == 7:
                sides[neig] = tiles[neig]
    """
    corners,sides={},{}
    corners,sides = find_corners_sides(tiles)
    print(len(sides))
    print(len(corners))
    dim = math.sqrt(len(tiles))
    start = corners[next(iter(corners))]
    corners.pop(str(start.no))

    cnt=0
    board=[]
    links={}
    links=find_candidates(start,sides)
    board.append(start)
    while len(sides) + len(corners) > 0:        
        # Corner
        if len(links)==0:
            links = find_candidates(first,corners)
            first = links[next(iter(links))]
            corners.pop(str(first.no))
            links = find_candidates(first,sides)
        else:
            first = links[next(iter(links))]
            links=find_candidates(first,sides)
            sides.pop(str(first.no))
      
        board.append(first)
        cnt+=1
    print(len(board))
    print(dim)
    monster = """\
                    #
        #    ##    ##    ###
        #  #  #  #  #  #   """.split('\n')

    print("Result Second Star")   
  
if __name__ == '__main__':
    main()