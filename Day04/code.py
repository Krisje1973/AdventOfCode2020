import re
lines = []
passports = []  
def readinput():
    global lines
    file = open(r"C:\DevOpps\Playground\AdventOfCode\Day4\input.txt") 
    lines = file.read()
    for line in lines.split('\n\n'):
        passports.append({p[0]: p[1] for p in re.findall(r'(\w+):(\S+)', line)})        
      
def main():
   readinput()
   first_star()
   second_star()        
          
def first_star():   
    print("Result First Star")
    print(sum(map(is_valid_A, passports)))

def second_star(): 
    print("Result Second Star")
    print(sum(map(is_valid_B, passports)))

def is_valid_A(passport):
    
    try:
        if len(passport)==8:
            return True
        elif len(passport)==7 and not passport["cid"]:
            return True        
              
        return False
    except:
        return len(passport)==7

def is_valid_B(passport):
    
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