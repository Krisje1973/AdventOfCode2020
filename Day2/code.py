
policies = []

class Policy:
    policy=""
    password=""
    low=0
    high=0
    char=""
    count=0
    
def readinput():
    file = open(r"C:\DevOpps\Playground\AdventOfCode\Day2\input.txt", "r")
    for line in file:
        policy=Policy()
        splitted = line.split(":")        
        policy.policy= splitted[0]
        policy.password=splitted[1]       
        _policy_split = policy.policy.split("-")
        policy.low=int(_policy_split[0])
        policy.high=int(_policy_split[1].split(" ")[0])
        policy.char=_policy_split[1].split(" ")[1]
        policy.count=count_char(_policy_split[1].split(" ")[1],splitted[1])

        policies.append(policy)

def main():
   readinput()
   first_star()
   second_star()        
          
def first_star():
    counter=0
    valid=0
    for policy in policies:
       if policy.count >= policy.low and policy.count<= policy.high:
           valid+=1     
       counter+=1

    print("Result First Star")
    print(str(valid))


def second_star():
    counter=0
    valid=0
    for policy in policies:      
        chars =  [char for char in policy.password]  
        match = 0
        if chars[policy.low] == policy.char:
            match+=1           
        if chars[policy.high] == policy.char:
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