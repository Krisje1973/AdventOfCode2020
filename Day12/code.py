import os, sys
import operator
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 

input=[]

class Position:
    dirs = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    ns,ew = 0,0
    direction=0
    directions=["E","S","W","N"]
    def turn(self,dir,degrees):
        #degrees = int(360 / degrees / 4)
        degrees = (degrees // 90)
        if dir=="R":
            self.direction += degrees
        else:
            self.direction -= degrees
        
        if self.direction<0:
            self.direction = self.directions.index(self.directions[self.direction])
        if self.direction>=len(self.directions):
            self.direction = self.direction % len(self.directions)

    def move(self,dir,degrees):
        
        if dir == "L" or dir=="R":
            self.turn(dir,degrees)
            return
        
        if dir != "F":          
            dir = self.dirs[self.directions[self.directions.index(dir)]] 
        else:
            dir = self.dirs[self.directions[self.direction]]

        self.ew+=dir[0]*degrees
        self.ns+=dir[1]*degrees        
      
def readinput():
    global input
    input = readinput_lines(r"Day12\input.txt")
   
def main():
    readinput()
    first_star()
    second_star()        

def first_star():  
    pos = Position()   
    for line in input:
        a,d=line[0],int(line[1:])      
        pos.move(a,d)
       
    print("Result First Star")   
    print(str(abs(pos.ew) + abs(pos.ns) ))

def second_star():
   
    print("Result Second Star")

if __name__ == '__main__':
    main()