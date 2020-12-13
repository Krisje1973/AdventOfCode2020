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
    # to low : 85850948895292
    #          2270925272303824.0
    #          99466969593960.0
               
  

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
            starts.append((0, s))
            n.append(s)
            a.append(0)
        else:
            starts.append((s - i, s))
            n.append(s)
            a.append(s - i)
      
    #n=[17,13,19]
    #a=[0,11,16]
    print(n)
    print(a)
    print(chinese_remainder(n,a))
    # Expected result = 3417
    print("Result Second Star")   

def chinese_remainder(n, a):
    sum=0
    prod=reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n,a):
        p=prod/n_i
        sum += a_i* mul_inv(p, n_i)*p
    return sum % prod

def mul_inv(a, b):
    b0= b
    x0, x1= 0,1
    if b== 1: return 1
    while a>1 :
        q=a// b
        a, b= b, a%b
        x0, x1=x1 -q *x0, x0
    if x1<0 : x1+= b0
    return x1

if __name__ == '__main__':
    main()