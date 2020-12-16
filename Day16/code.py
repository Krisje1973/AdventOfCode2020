import os, sys
import operator
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 
import re
input=[]
def readinput():
    global input
    input = readinput_lines(r"Day16\input.txt")
  

def main():
    readinput()
    first_star()
    second_star()        

def first_star():  
    helper = FileHelper()
    rules, ticket, nearby = helper.get_arrays_from_separator(input,'')
    my_ticket = list(map(int, ticket[0].split(",")))
    rules = {tuple(map(int, re.findall(r"\d+", rule))) for rule in rules}

    notvalid = []
    valrules = defaultdict(list)
    for near in nearby:
        ticket = list(map(int, near.split(",")))
        cnt=-1
        for val in ticket:
            cnt+=1
            found=0
            for rule in rules:
                l1,u1,l2,u2 = rule
                if l1 <= val <= u1 or l2 <= val <= u2:
                    valrules[cnt].append(rule)
                    found +=1
            if not found:
                notvalid.append(val)
   
    print("Result First Star")   
    print(sum(notvalid))
def second_star():
   
       
    print("Result Second Star")   
    
if __name__ == '__main__':
    main()