import os, sys
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 

prog=[]
def readinput():
    global prog
    input = readinput_lines(r"Day8\input.txt")
    prog = [line.strip().split() for line in input if line.strip()]
    prog = [(op, int(x)) for op, x in prog]

def main():
    readinput()
    first_star()
    second_star()        

def run_prog(first,prog):
    pos,acc,seen = 0,0,set()
    while pos < len(prog):
        if pos in seen:          
            if first:
                return acc
            else:
                return None

        seen.add(pos)
        op, x = prog[pos]
        if op == "acc":
            acc += x
            pos += 1
        elif op == "jmp":
            pos += x
        else:
            pos += 1

    return acc

def first_star():   
    acc = run_prog(1,prog)
    print("Result First Star")
    print(str(acc))

def second_star():
    for i in range(len(prog)):
        if prog[i][0] == "acc":
            continue
        new_op = "jmp" if prog[i][0] == "nop" else "nop"
        new_prog = prog[:i] + [(new_op, prog[i][1])] + prog[i+1:]
        acc = run_prog(0,new_prog)
        if acc is not None:
            print("Result Second Star")
            print(str(acc))

if __name__ == '__main__':
    main()