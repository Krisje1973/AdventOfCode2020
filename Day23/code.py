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
    data = helper.readinput_lines_as_list_ints(r"Day23\input_ex.txt")
    
def main():
    readinput()
    first_star()
    second_star()        


def move(times):
    global data
    for i in range(int(times)):
        pick = data[1:4]      
        dest = data[0] - 1 if data[0] > 1 else 9
        while dest in pick:
            dest -= 1
            if dest == 0:
                dest = 9
        de = collections.deque(data)
        while not de[0] == dest:
            de.rotate(-1)
        #3 (2) 8  9  1  5  4  6  7
        """
        -- move 2 --
        cups:  3 (2) 8  9  1  5  4  6  7 
        pick up: 8, 9, 1
        destination: 7
        result=3  2 (5) 4  6  7  8  9  1
        -- move 3 --
        cups:  3  2 (5) 4  6  7  8  9  1 
        pick up: 4, 6, 7
        destination: 3
        result = 7  2  5 (8) 9  1  3  4  6
        """
        data = list([data[0]] +[de[0]] + pick + list(de)[1:5])
    


def first_star():    
    move(10)
    print("Result First Star")   
    print(data)
   
def second_star():
  
    print("Result Second Star")   
    
if __name__ == '__main__':
    main()