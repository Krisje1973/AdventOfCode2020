
policies = []
password = []
least = []
most = []
char = []
count = []
def readinput():
   file = open(r"C:\DevOpps\Playground\AdventOfCode\Day2\input.txt", "r")
   for line in file:
      splitted = line.split(":")
      _policy = splitted[0]
      policies.append(_policy)
      password.append(splitted[1])
      _policy_split = _policy.split("-")
      least.append(int(_policy_split[0]))
      most.append(int(_policy_split[1].split(" ")[0]))
      char.append(_policy_split[1].split(" ")[1])
      count.append(count_char(_policy_split[1].split(" ")[1],splitted[1]))

def main():
   readinput()
   first_star()
   second_star()        
          
def first_star():
    counter=0
    valid=0
    for policy in policies:
       if count[counter] >= least[counter] and count[counter] <= most[counter]:
           valid+=1     
       counter+=1

    print("Result First Star")
    print(str(valid))


def second_star():
    counter=0
    valid=0
    for policy in policies:      
        chars =  [char for char in password[counter]]  
        match = 0
        if chars[least[counter]] == char[counter]:
            match+=1           
        if chars[most[counter]] == char[counter]:
            match+=1         
        if match==1:
            valid+=1
           
        counter+=1
        
    print("Result Second Star")
    print(str(valid))

def count_char(char,password):
    count=0
    for letter in password:
        if letter==char:
            count +=1
    return count

if __name__ == '__main__':
    main()