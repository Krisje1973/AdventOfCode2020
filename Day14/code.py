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
    global masks
    global mems
    input = readinput_lines(r"Day14\input.txt")        

        
   # masks = [x.split("=")[1] for x in input if str(x).startswith("mask")]
    #mems =  [x for x in input if str(x).startswith("mem")]


def main():
    readinput()
    first_star()
    second_star()        

def first_star():       
    mask = ""
    results = defaultdict(int)
    for line in input:
        prg,val = line.split("=")
        if prg.startswith("mask"):
            mask = val.strip()
        else:
            pos=prg[prg.index("[")+1:prg.index("]")]
            bval = bin(int(val)).replace("0b","")  
            bval = "".ljust(36-len(bval), "0") + bval
            new= ""
            for i in range(len(bval)):
                if mask[i] == "X":
                    new+=bval[i]
                else:
                    new += mask[i]
            res = int(new, 2)            
            results[pos] = res
            
    print("Result First Star")  
    print(sum(results.values()))
def second_star():
   
       
    print("Result Second Star")   
    
if __name__ == '__main__':
    main()