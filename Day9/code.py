import os, sys
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 

input=[]
result_first=0

def readinput():
    global input
    input = readinput_lines_as_ints(r"Day9\input.txt")

def check_data(data,checknum):
    for i in range(len(data)):
        for j in range(len(data)):
            if i!=j: 
                if data[i] + data[j] == checknum:
                    return checknum
def main():
    readinput()
    #first_star()
    second_star()        

def first_star():  
    global first_star
    preamp = 25
    err=0
    data = input[0:preamp]
    for i in range(len(data),len(input)):    
        if not check_data(data,input[i]):
            err = input[i]
            break

        data.pop(0)
        data.append(input[i])
    print("Result First Star")
    print(str(err))
    first_star = err

def second_star():
    global first_star 
    first_star = 144381670    
    second_star = 0
    data = []
    for i in range(len(input)):
        data.append(input[i])
        for j in range(i+1,len(input)):
            data.append(input[j])
            second_star = sum(data)
            if second_star == first_star:
                second_star = max(data) + min(data)               
                print("Result Second Star")
                print(second_star)
                return max(data)
            if second_star >= first_star:
                break        
        data = []
   
          

if __name__ == '__main__':
    main()