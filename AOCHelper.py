def readinput_dict_as_ints(filename):    
    input = {}
    file = open(filename, "r")
    for line in file:
      input[int(line)] = int(line)
    return input

def readinput_lines(filename):   
    file = open(filename, "r")    
    return [line.strip() for line in file]

def readinput_lines_as_ints(filename):   
    file = open(filename, "r")    
    input=[]
    for line in [line.strip() for line in file]:
      input.append(int(line)) 
    return input
  
def get_suroundings(grid,x,y,count):
  start =-1
  end = count -1 + start
  # Gets a new grid with offset
  return [grid[y + dy][x + dx] 
  
  for dx in range(start, end) 
  for dy in range(start, end) 
  if 0 <= y + dy < len(grid) # Check y bounds
  and 0 <= x + dx < len(grid[x]) # check x bounds
  and (dx, dy) != (0, 0)]  # not self
 
def join_lines_from_list(mylist): 
    return "".join("".join(row) for row in mylist)