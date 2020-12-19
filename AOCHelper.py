from functools import reduce
from collections import defaultdict 
import re

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
class Binary:
  def get_binary_as_string(self,val,length=0):
    bval = bin(int(val)).replace("0b","")  
    return "".ljust(length-len(bval), "0") + bval

  def get_binary_as_string_from_mask(self,val,mask,match):
    bval = self.get_binary_as_string(val,len(mask))
    binstr = ""
    for i in range(len(bval)):     
      if mask[i] == match:
          binstr+=bval[i]
      else:
          binstr+=mask[i]
    return binstr
  
  def split_binary_as_list(self,val,match):
    splitted = []
    matches = pow(2,val.count(match))
    for i in range(matches):
        splitted.append("")       
    for n in range(len(val)):       
        v=False  
        splitted.sort()                      
        for i in range(matches):  
            v = v == False                 
            if val[n] == match:
                splitted[i] += str(int(v))
            else:
                  splitted[i] += val[n] 
    return splitted

#Class to represent a graph 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) #dictionary containing adjacency List 
        self.V = vertices #No. of vertices 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # A recursive function used by topologicalSort 
    def topologicalSortUtil(self,v,visited,stack): 
  
        # Mark the current node as visited. 
        visited[v] = True
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        # Push current vertex to stack which stores result 
        stack.insert(0,v) 
  
    # The function to do Topological Sort. It uses recursive  
    # topologicalSortUtil() 
    def topologicalSort(self): 
        # Mark all the vertices as not visited 
        visited = [False]*self.V 
        stack =[] 
  
        # Call the recursive helper function to store Topological 
        # Sort starting from all vertices one by one 
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
        return stack
class FileHelper:
  
  def readinput_dict_as_ints(self,filename):    
      input = {}
      file = open(filename, "r")
      for line in file:
        input[int(line)] = int(line)
      return input

  def readinput_lines(self,filename):   
      file = open(filename, "r")    
      return [line.strip() for line in file]
  
  def readinput_lines_and_replace(self,filename,replaces):  
      #Usage :  input = file.readinput_lines_and_replace(r"Day17\input_ex.txt",[[".","0"],["#","1"]]) 
      file = open(filename, "r")    
      lines = []
      for line in [line.strip() for line in file]:
        for replace in replaces:
          line = line.replace(replace[0],replace[1])
        lines.append(line)

      return lines

  
  def readinput_lines_as_ints(self,filename):   
      file = open(filename, "r")    
      input=[]
      for line in [line.strip() for line in file]:
        input.append(int(line)) 
      return input

  def get_arrays_from_separator(self,lines,separator):
    # Reads all lines and creates array for each seperator found (mostly blanc line)
    arrays = []    
    lineid = 0
   
    while lineid < len(lines):
        arr = []
        while lineid < len(lines) and lines[lineid]:
            arr.append(lines[lineid])
            lineid += 1
        lineid += 1
        arrays.append(arr[len(arrays) != 0:])

    return arrays
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

class RegexHelper():
  def is_string_numeric_regex(self,s):
    return re.search('^[0-9]+$',s)
  
  def is_list_numeric_regex(self,l):
    for s in l:
      if not re.search('^[0-9]+$',s):
        return False

    return True
  
  def has_string_numeric_regex(self, s):
    for i in s:
        if re.search('^[0-9]+$',i):
          return True

    return False
    
  def has_list_numeric_regex(self,l):
    for s in l:
      if re.search('^[0-9]+$',s):
        return True
        
    return False
