import os, sys
import operator
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 

input=[]
def readinput():
    global input
    input = readinput_lines(r"Day12\input.txt")

class Position:
    ns,ew = 0,0
    ns_way,ew_way = 1,10
    direction="E"
    comp = Compass()  
    
    def move(self,dir,degrees):        
        if dir in "LR":
            self.direction = self.comp.turnCompassPoint(self.direction,dir,degrees)
            return
         
        if dir == "F":
            dir = self.direction

        if dir in self.comp.compasspoints:
            dir=self.comp.compasspoints[dir]
            self.ew+=dir[0]*degrees
            self.ns+=dir[1]*degrees      

    def move_way(self,dir,degrees):        
        if dir in self.comp.compasspoints:
            dir=self.comp.compasspoints[dir]
            self.ew_way+=dir[0]*degrees
            self.ns_way+=dir[1]*degrees  
            return

        if dir in 'LR':
            degrees = (degrees // 90)
            degrees %= 4
            if dir == 'L':
                degrees = 4 - degrees
            for _ in range(degrees):
                self.ew_way, self.ns_way = self.ns_way, - self.ew_way
        
        if dir == "F":
            self.ew += degrees * self.ew_way
            self.ns += degrees * self.ns_way   

def main():
    readinput()
    first_star()
    second_star()        

def first_star():  
    pos = Position()   
    for line in input:
        action,qty=line[0],int(line[1:])      
        pos.move(action,qty)
       
    print("Result First Star")   
    print(str(abs(pos.ew) + abs(pos.ns) ))

def second_star():
    pos = Position()   
    for line in input:
        action,qty=line[0],int(line[1:])      
        pos.move_way(action,qty)
       
    print("Result Second Star")   
    print(str(abs(pos.ew) + abs(pos.ns) ))

if __name__ == '__main__':
    main()