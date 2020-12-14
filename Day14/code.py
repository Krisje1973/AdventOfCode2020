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
binar = Binary()
def readinput():
    global input
    input = readinput_lines(r"Day14\input.txt")        

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
            val = binar.get_binary_as_string_from_mask(val,mask,"X")                     
            results[pos] = int(val, 2)
            
    print("Result First Star")  
    print(sum(results.values()))

def second_star():
    mask = ""
    results = defaultdict(int)
    for line in input:
        prg,val = line.split("=")
        if prg.startswith("mask"):
            mask = val.strip()
        else:
            pos=prg[prg.index("[")+1:prg.index("]")]          
            new = binar.get_binary_as_string_from_mask(pos,mask,"0")  
            for addr in binar.split_binary_as_list(new,"X"):
                results[int(addr, 2)] = int(val)            
              
    print("Result Second Star")   
    print(sum(results.values()))
if __name__ == '__main__':
    main()