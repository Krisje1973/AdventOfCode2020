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
    data = readinput_lines(r"Day19\input_ex.txt")
    helper = FileHelper()
    ru,answers = helper.get_arrays_from_separator(data," ")
    rules = {}
    for rule in ru:
        x,r = rule.split(":")
        rules[int(x)] = r.strip() 

def main():
    readinput()
    first_star()
    second_star()        



def first_star():  
    reg = RegexHelper()
    rep = {}
    sub = {}
    for ru in rules:
        rule = rules[ru].replace("|","").replace(" ","")       
        if not reg.is_string_numeric_regex(rule.strip()):
            rep[ru] = rule.replace("\"","")
        else:
            sub[ru] = rules[ru].replace(" ","")
    for su in sub:
        new=""
        for s in sub[su]:
            if s == "|":
                new+=s
            elif int(s) in rep.keys():
                new += rep[int(s)]
            else:
                new+=s
        print(new)
    print("Result First Star")   
   
def second_star():
   
       
    print("Result Second Star")   
    
if __name__ == '__main__':
    main()