import os, sys
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 

class Bag:
    name=""
    qty=0
    bags = {}
    def __init__(self):
        self.name =""
        self.qty=0
        self.bags = {}
    #ex=vibrant cyan bags contain 4 dim tomato bags, 1 dull green bag, 5 light silver bags, 2 striped gold bags.
   
input = []
bags = {}
def readinput():
    global input
    input = readinput_lines("Day7\input.txt")
    input = [bag for bag in input if not bag.split(" contain ")[1].startswith("no")]

def find_bag(bagname):
    result=[]
    for bag in bags:        
        if bagname in bags[bag].bags:
            result.append(bag)             
            result.extend(find_bag(bags[bag].name))
            
    return result

def main():
    readinput()
    first_star()
    second_star()        
          
def first_star():
    # get the bags that can contain gold
    # get for all these bags the bags that can contain that bag
    # recursive lookup

    #list with bags and there child bags
    for inp in input:       
        split = inp.split(",")
        bag = Bag() 
        bag.name =split[0].split("bags")[0].strip()        
        child = Bag()
       
        for n in split[0].split("bags")[1].split("contain")[1].split()[1:3]:
            child.name += " " + n
        child.name = child.name.strip()
        bag.bags[child.name] = child
        
        for sub in split[1:]:
            child = Bag()
            for n in sub.split("bag")[0].split()[1:]:
                child.name += " " + n
            child.name = child.name.strip()
            bag.bags[child.name] = child
       
        bags[bag.name] = bag    
    
    print("Result First Star")
    print(str(len(Counter(find_bag("shiny gold")))))

def second_star():
    print("Result Second Star")
          
if __name__ == '__main__':
    main()