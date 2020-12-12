import os, sys
import operator
import collections
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 

input=[]
grid = GridHelper()
def readinput():
    global input
    input = readinput_lines_as_ints(r"Day10\input.txt")   
def main():
    readinput()
    first_star()
    second_star()        
   
def first_star():  
    combis = grid.get_int_combinations(input,[1,3])
    joint1 = sum(combis[0][1])
    joint3 = sum(combis[0][3])
    joint3 +=1 
    
    print("Result First Star")
    print(str(joint1) + " - " + str(joint3))
    print(str(joint1*joint3))

def second_star():
    data = [0] + input + [input[-1] + 3]
    data = grid.calculate_combinations(data,3)

    print("Result Second Star")
    print(data[-1])         

if __name__ == '__main__':
    main()