import os, sys
import operator
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 
import re
import math
data=[]
def readinput():
    global data
    data = readinput_lines(r"Day18\input.txt")
    
def main():
    # Create Custom Num Class
    # Downgrade multiply precedence
    # Evaluate the input
    readinput()
    first_star()
    second_star()   

class custom_num:
    def __init__(self,num):
        self.num = num
    def __add__(self,other):
        return custom_num(self.num + other.num)
    def __sub__(self,other):
        return custom_num(self.num * other.num)
    def __and__(self,other):
        return custom_num(self.num * other.num)
    
def first_star():  
    tot = 0
    for expr in data:
        expr=re.sub(r"(\d+)", r"custom_num(\1)", expr).replace("*","-")
        tot += eval(expr).num
    
    print("Result First Star")  
    print(tot)
   
def second_star():
    tot = 0
    for expr in data:
        expr=re.sub(r"(\d+)", r"custom_num(\1)", expr).replace("*","&")
        tot += eval(expr).num
    
    print("Result Second Star") 
    print(tot)

if __name__ == '__main__':
    main()