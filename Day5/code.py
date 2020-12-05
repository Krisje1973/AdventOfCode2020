import re
import math

seats=[]
class Seat:
    lo,hi,row,col,seat_id=0,127,0,0,0
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
        self.hi=7
        for di in self.code[7:]:
            mi = math.trunc((self.hi-self.lo)/2)
            if di == "L":
                self.hi=self.lo+mi
            else:
                self.lo=self.lo+mi+1

        if self.code[9] == "L":
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
      
def main():
   readinput()
   first_star()
   second_star()        
          
def first_star():   
    seatid=0
    for seat in seats:
        if seat.seat_id>seatid:
            seatid = seat.seat_id     
    
    print("Result First Star")
    print(str(seatid))

def second_star():   
    missing = 0
    global seats    
    seats = sorted(seats, key = lambda s: s.row*10+s.col)
    
    for seat in seats:
        if seat.seat_id-missing==2:
            missing+=1
            break
        missing=seat.seat_id
   
    print("Result Second Star")
    print(missing)

if __name__ == '__main__':
    main()