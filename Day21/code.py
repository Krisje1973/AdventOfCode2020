import os, sys
import operator
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 
import re

data=[]
cand = defaultdict(list)
ingr = defaultdict(int)
def readinput():
    global data
    global ingr
    global cand
    data = readinput_lines(r"Day21\input.txt")
    
    for i in data:
        ing, allerg = i[:-1].split(" (contains ")
        for j in allerg.split(", "):
            cand[j].append(set(ing.split()))
        for j in ing.split():
            ingr[j] += 1
            
def main():
    readinput()
    #first_star()
    second_star()        

def first_star():  
    uncertain = set()
    used = set()
    known = {}
    for allergen in cand:
        bad = cand[allergen][0]
        for i in cand[allergen]:
            bad &= i
        uncertain |= bad
        if len(bad) == 1:
            known[allergen] = next(iter(bad))
            used.add(known[allergen])

    while len(cand) != len(known):
        for allergen in cand:
            if allergen not in known:
                bad = cand[allergen][0] - used
                for i in cand[allergen]:
                    bad &= i
                if len(bad) == 1:
                    known[allergen] = next(iter(bad))
                    used.add(known[allergen])

    print("Result First Star")   
    print(sum(cnt for i, cnt in ingr.items() if i not in uncertain))
    return known
def second_star():
   
    known = first_star()   
    print("Result Second Star")   
    print(",".join(j for i, j in sorted(known.items())))
if __name__ == '__main__':
    main()