seat_ids=[]
def Parse(line):
	rows = line[0:7]
	seats = line[7:10]
	rb = int(rows.replace("B", "1").replace("F", "0"), 2)
	sb = int(seats.replace("R", "1").replace("L", "0"), 2)
	return rb * 8 + sb

def readinput():   
    global seat_ids
    file = open(r"C:\DevOpps\Playground\AdventOfCode\Day5\input.txt")     
    seat_ids = [Parse(line) for line in [line.strip() for line in file]]
      
def main():
   readinput()
   first_star()
   second_star()        
          
def first_star():   
    print("Result First Star")
    print(max(seat_ids))

def second_star():       
    #seats = sorted(seats, key = lambda s: s.row*10+s.col)
    print("Result Second Star")
    print(str([seat for seat in range(min(seat_ids),max(seat_ids)+1) if seat not in  seat_ids][0]))

if __name__ == '__main__':
    main()