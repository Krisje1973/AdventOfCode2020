import os, sys
import operator
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 
import re

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

def find_neigborgs(tile):
    
    for t in tiles:
        c=tiles[t]      
        top = tile.t  
        if c.t == top or c.tr == top or c.b == top or c.br == top: 
            tile.tn+=1 
        if c.l==top or c.lr == top or c.r==top or c.rr==top:
            tile.tn+=1
        top = tile.b  
        if c.t == top or c.tr == top or c.b == top or c.br == top: 
            tile.tn+=1 
        if c.l==top or c.lr == top or c.r==top or c.rr==top:
            tile.tn+=1
        top = tile.l 
        if c.t == top or c.tr == top or c.b == top or c.br == top: 
            tile.tn+=1 
        if c.l==top or c.lr == top or c.r==top or c.rr==top:
            tile.tn+=1
        top = tile.r 
        if c.t == top or c.tr == top or c.b == top or c.br == top: 
            tile.tn+=1 
        if c.l==top or c.lr == top or c.r==top or c.rr==top:
            tile.tn+=1
    
def main():
    readinput()
    first_star()
    second_star()        

def first_star():  
    tot = 1
    for t in tiles:        
        tile = tiles[t]
        find_neigborgs(tile)
        print(t + " - " + str(tile.tn))
        if tile.tn==6: 
            tot *= int(t)
        
    print("Result First Star")  
    print(tot) 
   
def second_star():
   
       
    print("Result Second Star")   
    
if __name__ == '__main__':
    main()