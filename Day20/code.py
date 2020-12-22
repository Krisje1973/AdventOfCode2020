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
    data = helper.readinput_lines_and_replace(r"Day20\input_ex.txt",[[".","0"],["#","1"]]) 
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
    def rotate(self):
        t,tr,r,rr,b,br,l,lr = self.r,self.rr,self.b,self.br,self.l,self.lr,self.t,self.tr
        self.t,self.tr,self.r,self.rr,self.b,self.br,self.l,self.lr = t,tr,r,rr,b,br,l,lr 

def find_neigborgs(tile):
    corners = [tile.t,tile.b,tile.l,tile.r]
    for t in tiles:
        c=tiles[t]      
        for corner in corners:          
            if c.t == corner or c.tr == corner or c.b == corner or c.br == corner or c.l==corner or c.lr == corner or c.r==corner or c.rr==corner: 
                tile.tn+=1  
                tile.neigborgs[t]=c.tn  
    
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
   
def second_star():
    corners=[]
    for t in tiles:        
        tile = tiles[t]
        find_neigborgs(tile)    
        if tile.tn==6: 
           corners.append(t)
    print(len(tiles))
    # expected 48 Rows
    corner = tiles[corners[0]]
    image = [[]]
    image[0].append(corner)
    cnt=0
    while len(image<9) or cnt == 1000:
        cnt+=1
        tils = tiles.copy()
        tils.pop(corner)
        for t in tils:
            if tils[t].

    image[0].append(tile)
    print(len(image))
    #while len(image<144):



    monster = """\
                    #
        #    ##    ##    ###
        #  #  #  #  #  #   """.split('\n')

    print("Result Second Star")   
  
if __name__ == '__main__':
    main()