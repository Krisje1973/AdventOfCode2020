import re
from collections import Counter
lines = []
answers = []  
def readinput():    
    global answers
    file = open(r"C:\DevOpps\Playground\AdventOfCode\Day6\input.txt") 
    lines = file.read()
    answers=lines.split('\n\n')

def main():
   readinput()
   first_star()
   second_star()        
          
def first_star():     
    result=0
    for answer in answers:
        result+=len(Counter(answer.replace("\n","")))
           
    print("Result First Star")
    print(str(result))
        
def second_star():   
    result2=0
    for answer in answers:    
        result2+=sum(list(map(lambda z:z[1]==len(answer.split()),Counter(answer.replace("\n","")).items())))
    
    print("Result Second Star")
    print(str(result2))
if __name__ == '__main__':
    main()