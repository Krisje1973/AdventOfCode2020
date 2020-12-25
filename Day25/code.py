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
    data = helper.readinput_lines(r"Day25\input.txt")
    
def main():
    readinput()
    first_star()
    second_star()        

def first_star():      
    """
    card's public key is 5764801
    the initial subject number of 7 with a loop size of 8 produces 5764801.

    door's public key is 17807724
    the initial subject number of 7 with a loop size of 11 produces 17807724.
    """
    card,door= map(int,data)
    cnt,v,mod= 0,1,20201227
    while v != card:
        cnt+=1
        v = (7 * v) % mod
    
    print("Result First Star")  
    print(pow(door, cnt, mod))
def second_star():
    print("Result Second Star")   
  
if __name__ == '__main__':
    main()