import os, sys
import operator
from collections import Counter
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

def first_star():  
   
    print("Result First Star")   
   
def second_star():
   
       
    print("Result Second Star")   
    
if __name__ == '__main__':
    main()