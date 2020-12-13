import os, sys
import operator
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 
from collections import *
from functools import lru_cache
from functools import reduce
import heapq
import itertools
import math
import random


input=[]
def readinput():
    global input
    input = readinput_lines(r"Day13\input.txt")
    # to High: 803025030761668
    #          803025030761664 !!!!!!
    # to low : 85850948895292            
               
def main():
    readinput()
    #first_star()
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
   
    starts=[]
    busses = [bus for bus in input[1].split(",")]
    n = []
    a= []
    for i, s in enumerate(busses):
        if s == "x":  
            continue
        s = int(s)
        if not i:
            starts.append(i)
            n.append(s)
            a.append(0)
        else:
            starts.append(i)
            n.append(s)
            a.append(s - i)     
    
    print("Result Second Star")   
    print(ChineseReminder().calculate_chinese_remainder(n,a))

if __name__ == '__main__':
    main()