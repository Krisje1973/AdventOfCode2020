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
    data = helper.readinput_lines_as_list_ints(r"Day23\input.txt")
    
def main():
    readinput()
    first_star()
    second_star()        

def move(times):
    global data
    li={}
    for _ in range(int(times)):
        pick = data[1:4]
        dest = data[0] - 1 if data[0] > 1 else 9
        while dest in pick:
            dest -= 1
            if dest == 0:
                dest = 9

        idx = data.index(dest)
        if idx == 0:
            # no change
            pass
        else:
            data = list([data[0]] + data[4 : idx + 1] + pick + data[idx + 1 :])
        if times == 100:
            times = 100

        
        data = data[1:] + [data[0]]


def first_star():   
   
    move(100)

    
    print("Result First Star")   
    print(data)
   
def second_star():
    global data
   
    print("Result Second Star")   
    print(data)
if __name__ == '__main__':
    main()