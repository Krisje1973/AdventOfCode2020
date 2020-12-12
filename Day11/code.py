import os, sys
import operator
from collections import Counter
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AOCHelper import * 

input=[]
def readinput():
    global input
    input = readinput_lines(r"Day11\input.txt")
   
def main():
    readinput()
    first_star()
    second_star()        

def star1(grid):
    newgrid = [['.' for _ in row] for row in grid]

    for y, row in enumerate(grid):
        for x, seat in enumerate(row):            
            ct = Counter(get_suroundings(grid,x,y,4))
            if seat == 'L' and ct['#'] == 0:
                newgrid[y][x] = '#'
            elif seat == '#' and ct['#'] >= 4:
                newgrid[y][x] = 'L'
            else:
                newgrid[y][x] = grid[y][x]

    return newgrid

def star2(grid):
    newgrid = [['.' for _ in row] for row in grid]
    rows,rowlength = len(grid), len(grid[0])

    for y, row in enumerate(grid):
        for x, seat in enumerate(row):
            occ = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if (dx, dy) == (0, 0):
                        continue

                    nx = y + dx
                    ny = x + dy
                    while 0 <= nx < rows and 0 <= ny < rowlength and grid[nx][ny] == '.':
                        nx += dx
                        ny += dy

                    if 0 <= nx < rows and 0 <= ny < rowlength:
                        occ += grid[nx][ny] == '#'


            if seat == 'L' and occ == 0:
                newgrid[y][x] = '#'
            elif seat == '#' and occ >= 5:
                newgrid[y][x] = 'L'
            else:
                newgrid[y][x] = grid[y][x]
    return newgrid



def first_star():  
    grid = input
    while True:
        loop = star1(grid)
        if loop == grid:
            break

        grid = loop

    occupied = join_lines_from_list(grid)
    print("Result First Star")
    print(occupied.count("#"))

def second_star():
    grid = input
    while True:
        loop = star2(grid)
        if loop == grid:
            break

        grid = loop

    occupied = join_lines_from_list(grid)
    print("Result Second Star")
    print(occupied.count("#"))
  
if __name__ == '__main__':
    main()