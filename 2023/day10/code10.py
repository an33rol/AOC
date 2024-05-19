# napisala sam krivo procitajuci zadatak, nisam znala da je put uvijek nuzno ciklus 
# nego sam mislila da se moze granati i doci do nekog dead enda
# ali radi pa necu sad brisati

import sys
sys.setrecursionlimit(100000) #lol

lines =  open("day10/input10.txt","r").readlines()
max_i = len(lines)
max_j = len(lines[0])

def printList(grid):
   for line in grid:
      print(line)

def giveDir(c):
   match c:
      case "-":
         return ["left","right"]
      case "|":
         return ["up","down"]
      case "L":
         return ["up","right"]
      case "J":
         return ["left","up"]
      case "7":
         return ["left","down"]
      case "F":
         return ["down","right"]
   return []

# maxcount bi bio korisan da se put grana 
maxCount = 0
def checkChar(i,j,currentCount):
   if(grid[i][j]=="S"):
      where =  S_adj
   else:
      where = giveDir(grid[i][j])
   if(len(where) == 0):
      return
   
   else:
      grid[i][j] = currentCount 
      currentCount+=1
      global maxCount
      maxCount = max(currentCount,maxCount)

      if ("left" in where and j>0):
         checkChar(i,j-1,currentCount)

      if ("right" in where and j+1<max_j):
         checkChar(i,j+1,currentCount)
         
      if ("up" in where and i>0):
         checkChar(i-1,j,currentCount)
         
      if ("down" in where and i+1<max_i):
         #print("ide dolje od", i,j)
         checkChar(i+1,j,currentCount)


# load grid, find coordinates of S and which dir can it go
grid = []
S_adj =[]
for i in range(len(lines)): 
   for j in range (len(lines[i])):
      if lines[i][j]=="S":
         start = [i,j]
         if ("up" in giveDir(lines[i+1][j]) and i<max_i):
            S_adj.append("down")
         
         if ("down" in giveDir(lines[i-1][j]) and i>0):
            S_adj.append("up")
            
         if ("right" in giveDir(lines[i][j-1]) and j<max_j):
            S_adj.append("left")
            
         if ("left" in giveDir(lines[i][j+1]) and j>0):
            S_adj.append("right")

   grid.append(list(lines[i].replace("\n","")))
   

checkChar(start[0],start[1],0)
print(int((maxCount)/2))