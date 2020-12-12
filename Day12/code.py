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

        if action in pos.comp.compasspoints:
            ew, ns = pos.comp.compasspoints[action]
            pos.ew_way += qty * ew
            pos.ns_way += qty * ns
        else:
            degrees = (qty // 90)
            degrees %= 4
            if action == 'L':
                degrees = 4 - degrees
            if action in 'LR':
                for _ in range(degrees):
                    pos.ew_way, pos.ns_way = pos.ns_way, - pos.ew_way
            else:               
                pos.ew += qty * pos.ew_way
                pos.ns += qty * pos.ns_way
     
    print("Result Second Star")
    print(str(abs(pos.ew) + abs(pos.ns) ))

if __name__ == '__main__':
    main()