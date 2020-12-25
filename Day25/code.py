import os, sys
import operator
import collections 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 
import re

data=[]
def readinput():
    global data
    helper = FileHelper()   
    data = helper.readinput_lines(r"Day25\input.txt")
    
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