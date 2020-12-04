
lines = []
passport=[]
values = {}
def readinput():
    global lines
    file = open(r"C:\DevOpps\Playground\AdventOfCode\Day4\input.txt", "r")
    lines = [line.strip() for line in file]

def main():
   readinput()
   first_star()
   second_star()        
          
def first_star():   
    
    valid=0
    for line in lines:
        keys= line.split()        
        if keys==[]:           
            if len(passport)==8:
                valid+=1
            elif len(passport)==7 and passport.count("cid")==0:
                valid+=1
               
            passport.clear()
        else:
            for key in keys:
                passport.append(key.split(":")[0])               

    print("Result First Star")
    print(str(valid))

def second_star():      
    print("Result Second Star")
   
if __name__ == '__main__':
    main()