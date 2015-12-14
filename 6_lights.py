import numpy as np
import itertools

grid = np.zeros( (9,9) )

grid[0][8] = 1      ##random cells set to 1
grid[7][1] = 1
grid[4][2] = 1
grid[5][5] = 1
grid[8][8] = not grid[8][8]

lights_lit = 0


with open('input_test6.txt') as f:
    for line in f:
        line = line.rstrip()
        line = line.split(" ")
        line.remove("through")
        if line[0] == "turn":
            line.remove("turn")
        line[1] = line[1].split(',')
        line[2] = line[2].split(',')
        
        print line

        if line[0] == "toggle":
            print "Start: " + str(line[1][0]) + ", " + str(line[1][1])
            print "End: " + str(line[2][0]) + ", " + str(line[2][1])
            ##for x in np.nditer(grid[line[1][0]:line[1][1], line[2][0]:line[2][1]]):
               ## x = not x             

        if line[0] == "on":
            pass

        if line[0] == "off":
            pass

for x in np.nditer(grid[:5, :5]):
    x = 1

for x in np.nditer(grid):
    if x == 1:
        lights_lit = lights_lit + 1

print grid ## Here grid[:x, :y] x represents rows, and y index within it

print "Total lights: " + str(lights_lit)
