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

    if cnt > 50:
        return ""
    if rules[rule][0] == '"': 
        return rules[rule][1]

    reg = ""
    split = rules[rule].split('|')
    for rule in split:
        for s in rule.split():
           reg += find_rule(s, cnt+1)
        reg += "|"

    return "(1)".replace("1",reg[:len(reg)-1])

def first_star():  
    reg = re.compile(find_rule())   
    print("Result First Star")   
    print(len([*filter(reg.fullmatch,answers)]))  
    
def second_star():
    global rules
    rules["8"] = "42 | 42 8"
    rules["11"] = "42 31 | 42 11 31"
    
    reg = re.compile(find_rule())   
    print("Result Second Star")   
    print(len([*filter(reg.fullmatch,answers)]))  
if __name__ == '__main__':
    main()