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
        rules[int(x)] = r.strip() 

def main():
    readinput()
    first_star()
    second_star()        

def find_rule(id):
    if id in rules.keys():
        return id

def first_star():  
    # Pattern ex  = (a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b)
    rs, ms = open(r"Day19\input.txt").read().split('\n\n')
                   
                   
                    
    """ Rules ex are
        0: 4 1 5
        1: 2 3 | 3 2
        2: 4 4 | 5 5
        3: 4 5 | 5 4
    """
    reg = RegexHelper()
    found = {}
    sub = {}
   
    for ru in rules:
        rule = rules[ru].replace("|","").replace(" ","")       
        if not reg.is_string_numeric_regex(rule.strip()):
            found[ru] = rule.replace("\"","")
        else: sub[ru] = rules[ru]
   
    while any(reg.has_list_numeric_regex(str(x)) for x in sub.values()):
        for su in sub:
            if su ==28:
                v=1
            new=sub[su]
            if reg.has_list_numeric_regex(new):
                
                for s in sub[su].split(" "):
                    if not s == "|" and reg.is_string_numeric_regex(str(s)):
                        if int(s) in found.keys():
                            new = new.replace(s, "(" + found[int(s)] + ")")
                            break                    

                if not reg.has_list_numeric_regex(new) and not new == "|" and not new == " " :
                    found[su] = new               
                sub[su]= new

    reg = "(" + sub[0].replace(" ","").replace("(a)","a").replace("(b)","b") + ")"      
    print("Result First Star")   
   
    r = re.compile(reg)
    
    print(len([*filter(r.fullmatch, ms.split())]))
   

    
def second_star():
   
       
    print("Result Second Star")   
    
if __name__ == '__main__':
    main()