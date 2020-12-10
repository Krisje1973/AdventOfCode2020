import os, sys
import operator
import collections
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 

input=[]
joint1 = 0
joint3 = 0
def readinput():
    global input
    input = readinput_lines_as_ints(r"Day10\input.txt")
    input.sort()
def main():
    readinput()
    first_star()
    second_star()        
   
def first_star():  
    global joint1,joint3
    joint3 +=1 
    start = 0
    for val in input:
        if val - start == 1:
            joint1+=1
        else: 
            joint3+=1           
        start = val
    
    print("Result First Star")
    print(str(joint1) + " - " + str(joint3))
    print(str(joint1*joint3))

def second_star():
    dist = [1]
    data = [0] + input + [input[-1] + 3]
    for val in range(1, len(data)):
        total = 0
        for tot in range(val):
            if data[tot] + 3 >= data[val]:
                total += dist[tot]
        dist.append(total)  
        
    print("Result Second Star")
    print(dist[-1])         

if __name__ == '__main__':
    main()