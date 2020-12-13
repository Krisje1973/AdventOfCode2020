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
    remainder = []
    modulo = []
    for ind, bus_id in ((i, int(j)) for i, j in enumerate(input[1].split(",")) if j != "x"):
        remainder.append(-ind)
        modulo.append(bus_id)
  
    print("Result Second Star")  
    print(ChineseReminder().calculate_chinese_remainder(remainder,modulo)[0])

if __name__ == '__main__':
    main()