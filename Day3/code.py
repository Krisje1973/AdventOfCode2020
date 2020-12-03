
lines = []

def readinput():
    global lines
    file = open(r"C:\DevOpps\Playground\AdventOfCode\Day3\input.txt", "r")
    lines = [line.strip() for line in file]

def calculate(down,right):
    row = 0
    pos = 0
    trees = 0
    global lines
    while True:
        row += down
        pos = (pos+right) % len(lines[0])
        if row>=len(lines):
            break
        trees += lines[row][pos]=="#"
       
    return trees

def main():
   readinput()
   first_star()
   second_star()        
          
def first_star():    
    result = calculate(1,3)

    print("Result First Star")
    print(result) 

def second_star():   
    result = calculate(1, 1)*calculate(1, 3)*calculate(1, 5)*calculate(1, 7)*calculate(2, 1)

    print("Result Second Star")
    print(result)


if __name__ == '__main__':
    main()