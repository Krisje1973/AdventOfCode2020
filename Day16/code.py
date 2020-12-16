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
    #first_star()
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

def parse_rule(rule):
    return tuple(map(int, re.findall(r"\d+", rule))), rule.startswith("departure")   

def second_star():
    helper = FileHelper()
    rules, ticket, nearby = helper.get_arrays_from_separator(input,'')
    my_ticket = list(map(int, ticket[0].split(",")))
    rules = {parse_rule(rule) for rule  in rules}

    # Find valid tickets
    error_rate = 0
    valid_tickets = [[] for i in rules]
    for ticket in nearby:
        ticket = list(map(int, ticket.split(",")))
        for val in ticket:
            if not any(l1 <= val <= u1 or l2 <= val <= u2 for (l1, u1, l2, u2), dep in rules):
                error_rate += val
                break
        else:
            for ind, val in enumerate(ticket):
                valid_tickets[ind].append(val)

    tot = 1
    while rules:
        for id, ticket_val in enumerate(my_ticket):
            cand_rules = []
            for rule in rules:
                (low1, up1, low2, up2), depart = rule
                # This check can be replaced using binary search (after sorting)
                if all(low1 <= val <= up1 or low2 <= val <= up2 for val in valid_tickets[id]):
                    cand_rules.append(rule)
            if len(cand_rules) == 1:  # Only 1 rule works
                rule = cand_rules[0]
                rules.remove(rule)
                if rule[1]:
                    tot *= ticket_val

    print("Result Second Star")   
    print(tot)

if __name__ == '__main__':
    main()