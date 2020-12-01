
input = {}
def readinput():
   file = open("C:\DevOpps\Playground\AdventOfCode\Day1\input.txt", "r")
   for line in file:
      input[int(line)] = int(line)

def main():
   readinput()
   first_star()
   second_star()        
      
      #print(inp)
       
def first_star():
    for num in input:
      search = 2020 - int(num)
      if search in input.keys():
         print("Result First Star")
         print(num*search) 
         print(str(num)+ "-"+ str(search))      
         break  

def second_star():
   found = 0
   for first in input:     
      if found:
         break
      for second in input:        
         if found:
            break
         for third in input:
            found = first + second + third == 2020            
            if found:
               print("Result Second Star")
               print(first*second*third) 
               print(str(first)+ "-"+ str(second) + " - " + str(third))                
               break   
          
if __name__ == '__main__':
    main()