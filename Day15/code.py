import os, sys
from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 
input=[]
def readinput():
    global input
    input = readinput_lines(r"Day15\input.txt")
  

def main():
    readinput()
    first_star()
    second_star()     

def calculate(spoken):
    nums  = list(map(int, input[0].split(",")))
    seen = defaultdict(int)
   
    for id, last in enumerate(nums, 1):
        seen[last] = id

    # never spoken = 0
    # spoken = last seen - lastseen[-1]    
    for id in range(len(nums), spoken):
        # seen last = id
        # last = count of id - nul
        seen[last], last = id, id - seen[last] if seen[last] else 0
        """v=last
        last = id - seen[last] if seen[last] else 0
        seen[v]= id"""
    return last

def first_star():  
    print("Result First Star") # Expected 436
    print(calculate(2020))
   
def second_star():
    print("Result Second Star")   
    print(calculate(30000000))

if __name__ == '__main__':
    main()