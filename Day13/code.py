import os, sys
import operator
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 
from collections import *
from functools import lru_cache
import heapq
import itertools
import math
import random


input=[]
def readinput():
    global input
    input = readinput_lines(r"Day13\input.txt")
  

def main():
    readinput()
    first_star()
    second_star()        

def first_star():  
    depart = int(input[0])
    busses = [int(x) for x in input[1].split(",") if x != "x"]
    times =  [((int(depart/int(x)+1)) * int(x)) - depart for x in busses]
    earliest = min(times)
    earliestidx = times.index(earliest)

    print("Result First Star")   
    print(busses[earliestidx] * earliest)
   
def second_star():
   
       
    print("Result Second Star")   
    
if __name__ == '__main__':
    main()