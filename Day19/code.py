import os, sys
import operator
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 
import re

data=[]
rules={}
answers=[]
def readinput():
    global rules
    global answers
    data = readinput_lines(r"Day19\input.txt")
    
    helper = FileHelper()
    ru,answers = helper.get_arrays_from_separator(data," ")
    rules = {}
    for rule in ru:
        x,r = rule.split(": ")
        rules[x] = r.strip() 

def main():
    readinput()
    first_star()
    second_star()        

def find_rule(rule='0', cnt=0):

    if rules[rule][0] == '"': 
        return rules[rule][1]

    reg = ""
    split = rules[rule].split('|')
    for s in split:
        for t in s.split():
           reg += find_rule(t, cnt+1)
        reg += "|"

    return "(1)".replace("1",reg[:len(reg)-1])

def first_star():  
    reg = re.compile(find_rule())   
    print("Result First Star")   
    print(len([*filter(reg.fullmatch,answers)]))  
    
def second_star():
   
    print("Result Second Star")   
    
if __name__ == '__main__':
    main()