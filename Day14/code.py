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
    #'first_star()
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
    mask = ""
    results = defaultdict(int)
    for line in input:
        prg,val = line.split("=")
        if prg.startswith("mask"):
            mask = val.strip()
        else:
            pos=prg[prg.index("[")+1:prg.index("]")]
            bval = bin(int(pos)).replace("0b","")  
            bval = "".ljust(36-len(bval), "0") + bval
            new= ""
            for i in range(len(bval)):
                if mask[i] == "0":
                    new+=bval[i]
                else:
                    new += mask[i]

            addresses = []
            for i in range(2**new.count("X")):
                addresses.append("")       

            for n in range(len(new)):       
                v=False  
                addresses.sort()                      
                for i in range(2**new.count("X")):  
                    v = v == False                 
                    if new[n] == "X":
                        addresses[i] += str(int(v))
                    else:
                         addresses[i] += new[n] 

            for addr in addresses:
                results[int(addr, 2)] = int(val)            
              
    print("Result Second Star")   
    print(sum(results.values()))
if __name__ == '__main__':
    main()