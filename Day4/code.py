import re
lines = []
validPasswords = []
class Passportfields:
    key=""
    value=""
    

def readinput():
    global lines
    file = open(r"C:\DevOpps\Playground\AdventOfCode\Day4\input.txt", "r")
    lines = [line.strip() for line in file]

def main():
   readinput()
   #first_star()
   second_star()        
          
def first_star():   
    valid=0
    passport=[]
    
    for line in lines:
        check = False
        keys= line.split()        
        if keys==[]:           
            if len(passport)==8:
                check = True
            elif len(passport)==7 and passport.count("cid")==0:
                 check = True
               
            passport.clear()
        else:
            for key in keys:
                passport.append(key.split(":")[0])    

        if check: 
            valid+=1
            validPasswords.append(line)
    print("Result First Star")
    print(str(valid))

def second_star():  
    
    file = open(r"C:\DevOpps\Playground\AdventOfCode\Day4\input.txt",) 
    lines = file.read()
    passports = []  
    for block in lines.split('\n\n'):
        parsed = re.findall(r'(\w+):(\S+)', block)
        passports.append({m[0]: m[1] for m in parsed})
    print(sum(map(is_valid, passports)))
   
def is_valid(passport):
    
    try:
        byr = int(passport['byr'])
        if not 1920 <= byr <= 2002:
            return False
        iyr = int(passport['iyr'])
        if not 2010 <= iyr <= 2020:
            return False
        eyr = int(passport['eyr'])
        if not 2020 <= eyr <= 2030:
            return False
        hgt = passport['hgt']
        match = re.match(r'(\d+)(cm|in)', hgt)
        height, unit = match[1], match[2]
        if unit == 'cm':
            if not 150 <= int(height) <= 193:
                return False
        elif unit == 'in':
            if not 59 <= int(height) <= 76:
                return False
        else:
            return False
        hcl = passport['hcl']
        if hcl[0] != '#' or len(hcl) != 7:
            return False
        int(hcl[1:], 16)  # Raises exactly if the desired criterion fails
        ecl = passport['ecl']
        if ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            return False
        pid = passport['pid']
        if not pid.isdigit() or len(pid) != 9:
            return False
        return True
    except:
        return False

if __name__ == '__main__':
    main()