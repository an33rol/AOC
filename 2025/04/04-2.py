import numpy as np

file = open("input.txt","r")

total = 0

# define grid
grid = np.array([list(a[:-1]) for a in file.readlines()])

# expand grid
zeroes = np.full((1,grid.shape[0]), '.')
grid = np.vstack((zeroes, grid, zeroes))
zeroes = np.full((grid.shape[0],1), '.')
grid = np.hstack((zeroes, grid, zeroes))

moved = True

# repeat until nothing was moved
while moved:
   moved = False 

   # check for rolls of paper
   for i in range (1, grid.shape[0]):
      for j in range (1, grid.shape[1]):
         if grid[i][j] == "@":     
            if [grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1], grid[i][j-1], grid[i][j+1], grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1]].count('@') < 4:
               total += 1
               grid[i][j] = '.'
               moved = True
         
         
   
print ("total:",total)