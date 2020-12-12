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

class Compass:
  compasspoints = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)} # Can be used for north/south, east/west calculation

  def turnCompassPoint(self,currentdirection,turndirection,degrees):     
    degrees = (degrees // 90)   
    if turndirection == "L":
        degrees=-degrees
    dirs = list(self.compasspoints.keys())
    idx = dirs.index(currentdirection) + degrees
    idx %= len(dirs)
    return (dirs[idx:] + dirs[:idx])[0]       
class GridHelper:
  def get_suroundings(self,grid,x,y,count):
    start =-1
    end = count -1 + start
    # Gets a new grid with offset
    return [grid[y + dy][x + dx] 
    
    for dx in range(start, end) 
    for dy in range(start, end) 
    if 0 <= y + dy < len(grid) # Check y bounds
    and 0 <= x + dx < len(grid[x]) # check x bounds
    and (dx, dy) != (0, 0)]  # not self
 
  def join_lines_from_list(self,mylist): 
      return "".join("".join(row) for row in mylist)


  def calculate_combinations(self,data,offset):

    dist = [1]
    data.sort()
    for val in range(1, len(data)):
          total = 0
          for tot in range(val):
              if data[tot] + offset >= data[val]:
                  total += dist[tot]
          dist.append(total)  
          
    return dist
  
  def get_int_combinations(self,data,offsets):
    # =============================================================
    # Data is list of int's.
    # Each val in list needs to connect within the offset parameter
    # =============================================================

    combis = {}
    combi_vals = {}
    data.sort()
    for offset in offsets:
      combi = []
      combi_val = []  
      start = 0
      for val in data:
        if val - start == offset:
          combi.append(1) 
          combi_val.append(val)  
        start = val
      
      combis[offset] = combi
      combi_vals[offset] = combi_val      
         
    return combis,combi_vals
