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
    data = helper.readinput_lines_as_list_ints(r"Day23\input_ex.txt")
    
def main():
    readinput()
    first_star()
    second_star()        

def move2(times):
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

        data = data[1:] + [data[0]]

def move3(times):
    global data
    cur=0
    for i in range(int(times)):
        
        cur=data[cur] 
        de = collections.deque(data)      
        while not de[0] == cur:
            de.rotate(-1)
        pick = list(de)[1:4]    
        dest = cur - 1 if cur-1 > 0 else 9
        while dest in pick:
            dest -= 1
            if dest == 0:
                dest = 9
        idx = data.index(dest)
        ch = data.copy()
        for i in pick:
            idx= ch.index(i)
            ch.pop(idx)
        idx=ch.index(dest)
        ch =ch[0:idx] + [dest] + pick

        while not de[0] == dest:
            de.rotate(-1)
        de.rotate(-1)    
        cur=de[0] 
        data=ch+list(de)[0:len(data)-len(ch)]
    
def move(times):
    global data
    cur=1
    for i in range(int(times)):  
        v= len(data)+i
        v= v% len(data) 
        
        print(i, "--" ,data)
        curval=data[v] 

        # Rotate so we have a clean list
        de = collections.deque(data)      
        while not de[0] == curval:
            de.rotate(-1)        
        pick = list(de)[1:4]
        cur = de[4]
        dest = curval -1 if curval > 1 else 9
        while dest in pick:
            dest-=1
            if dest==0: dest=9
        
        for j,d in enumerate(data):
            if d==dest:    
                if j==0:
                    # expected 7  2  5 (8) 9  1  3  4  6                   
                    de = collections.deque(data)     
                    de.rotate(-1)    
                    data = list(de)
                    for p in pick:
                        idx = data.index(p)
                        data.insert(len(data),data.pop(idx))
                    de = collections.deque(data)     
                    de.rotate(1)    
                    data = list(de)
                else:
                    idxf = data.index(pick[0])
                    if idxf > len(data)-3:
                       
                        # pick = 367
                        # dest = 8 
                        #[7, 2, 5, 8, 4, 1, 9, 3, 6]
                        # expected : 8  3  6  7  4  1  9 (2) 5 

                        # 7  4  1  5  8  3  9  2 (6)
                        offset = len(pick) - (len(data)-idxf)  
                        de = collections.deque(data)     
                        de.rotate(-offset)    
                        data = list(de)
                        offset = data.index(d) 
                        for p in pick:
                            offset+=1
                            idx = data.index(p)                                
                            data.insert(offset,data.pop(idx))
                           
                        offset = 2 if idxf == 7 else 1   
                        de = collections.deque(data)     
                        de.rotate(-offset)    
                        data = list(de)

                    else:
                        for p in pick:
                            idx = data.index(p)
                            data.insert(j,data.pop(idx))
               
               
       




def first_star():   
   
    move(10)
    print("Result First Star")   
    print(data)
   
def second_star():
  
    print("Result Second Star")   
    
if __name__ == '__main__':
    main()