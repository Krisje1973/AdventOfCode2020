import os, sys
import operator
import collections 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 
import re

data=[]
def readinput():
    global data
    helper = FileHelper()   
    data = helper.readinput_lines_as_list_ints(r"Day23\input.txt")
    
def main():
    readinput()
    #first_star()
    second_star(int(1e6),int(1e7))        

def Move():
    start=0


def move(times):
    global data
    
    for _ in range(int(times)):
        pick = data[1:4]
        dest = data[0] - 1 if data[0] > 1 else 9
        while dest in pick:
            dest -= 1
            if dest == 0:
                dest = 9

        idx = data.index(dest)
        if idx == 0:
            # no change
            pass
        else:
            data = list([data[0]] + data[4 : idx + 1] + pick + data[idx + 1 :])
        if times == 100:
            times = 100

        
        data = data[1:] + [data[0]]


def first_star():   
    move(100)
    print("Result First Star")   
    print(data)

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None  

def second_star(N=9,moves=100):
    # asses: 907135 401051 363807398885

   
    cups = {}
    for c in range(1, N + 1):
        cups[c] = Node(c)    
    for x, y in zip(data, data[1:]):
        x, y = map(int, [x, y])
        cups[x].next = cups[y]

    if len(data) == N:
        cups[int(data[-1])].next = cups[int(data[0])]
    else:
        cups[int(data[-1])].next = cups[len(data) + 1]
        for i in range(len(data) + 1, N):
            cups[i].next = cups[i + 1]
        cups[N].next = cups[int(data[0])]

    head = cups[int(data[0])]
    for _ in range(moves):
        rem_start = head.next
        rem_end = head.next.next.next

        vals = [rem_start.val, rem_start.next.val, rem_end.val]
        goal = head.val - 1 if head.val > 1 else N
        while goal in vals:
            goal -= 1
            if goal == 0:
                goal = N

        head.next = rem_end.next
        rem_end.next = cups[goal].next
        cups[goal].next = rem_start

        head = head.next
    
    if N==9:
        result=""
        one = cups[1].next
        result+=str(one.val)
        for i in range(7):
            one = cups[one.next.val]
            result+=str(one.val)

        print("Result First Star")   
        print(result)

    print("Result Second Star")   
    print(cups[1].next.val*cups[1].next.next.val)
if __name__ == '__main__':
    main()