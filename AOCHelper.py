from functools import reduce
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
class ChineseReminder():
  def calculate_chinese_remainder(self,rem, mod):
    #
    # Solves and finds X for a system of congruences:
    #   X = a_1 (mod n_1)
    #   X = a_2 (mod n_2)
    #   ...
    #   X = a_N (mod n_N)
    #
    # Solutions afterwards can be made by adding/subtracting by MOD
    # Returns X (the initial value), and MOD (the interval where it repeats)
    #
    # Additional Info: https://brilliant.org/wiki/chinese-remainder-theorem/

    a1 = rem[0]
    m1 = mod[0]
    for a2, m2 in zip(rem[1:], mod[1:]):
        gcd, x, y = self.extended_gcd(m1, m2)
        if a1 % gcd != a2 % gcd:
            raise ValueError("No solutions for given input.")
        _, x, y = self.extended_gcd(m1 // gcd, m2 // gcd)
        MOD = m1 // gcd * m2
        X = (a1 * (m2 // gcd) * y + a2 * (m1 // gcd) * x) % MOD
        a1 = X
        m1 = MOD
    return a1, MOD
    
  def extended_gcd(self,a, b):
      x, y, u, v = 0, 1, 1, 0
      while a != 0:
          q, r = b // a, b % a
          m, n = x - u * q, y - v * q
          b, a, x, y, u, v = a, r, u, v, m, n
      gcd = b
      return gcd, x, y  # x, y are for [ax + by = gcd]

 
