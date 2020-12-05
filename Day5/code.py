import re
import math

seats=[]
seatids={}
class Seat:
    lo,hi,row,col,seat_id=0,127,0,7,0
    code = ""
    def calulate_seatid(self):
        self.get_row()
        self.get_col()
        self.seat_id = self.row * 8 + self.col
    def get_row(self):
        for di in self.code[0:7]:
            mi = math.trunc((self.hi-self.lo)/2)
            if di == "F":
                self.hi=self.lo+mi
            else:
                self.lo=self.lo+mi
        if self.code[7] == "F":
            self.row = self.lo
        else:
            self.row = self.hi    

    def get_col(self):
        self.lo=0
        self.hi = self.col
        for di in self.code[7:]:
            mi = math.trunc((self.hi-self.lo)/2)
            if di == "L":
                self.hi=self.lo+mi
            else:
                self.lo=self.lo+mi
        if self.code[7] == "L":
            self.col = self.lo
        else:
            self.col = self.hi    

def readinput():
    global seats
    file = open(r"C:\DevOpps\Playground\AdventOfCode\Day5\input.txt") 
    lines = [line.strip() for line in file]
    for line in lines:
        seat = Seat()
        seat.code=line
        seat.calulate_seatid()
        seats.append(seat)
        seatids[seat.seat_id] = seat.seat_id
      
def main():
   readinput()
   first_star()
   second_star()        
          
def first_star():   
    seatid=0
    global seatids
    for seat in seats:
        if seat.seat_id>seatid:
            seatid = seat.seat_id  
        seatids[str(seat.seat_id)] = seat.seat_id      
    
    print("Result First Star")
    print(str(seatid))

def second_star():   
   
           

    print("Result Second Star")
   

if __name__ == '__main__':
    main()