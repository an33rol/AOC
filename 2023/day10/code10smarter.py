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
currentCount = 0
def checkChar(i,j):
   global cameFrom
   global currentCount

   if(grid[i][j]=="S"):
      where =  S_adj
   else:
      where = giveDir(grid[i][j])
   if(len(where) == 0):
      return
   
   else:
      grid[i][j] = currentCount 
      currentCount+=1
      #global maxCount
      #maxCount = max(currentCount,maxCount)
      cur_i = i
      cur_j = j

      if ("left" in where and j>0 and "left"!=cameFrom):
         cur_j -= 1
         cameFrom = "right"
         #checkChar(i,j-1,currentCount)

      elif ("right" in where and j+1<max_j) and "right"!=cameFrom:
         cur_j += 1
         cameFrom = "left"
         #checkChar(i,j+1,currentCount)
         
      elif ("up" in where and i>0 and "up"!=cameFrom):
         cur_i -= 1
         cameFrom = "down"
         #checkChar(i-1,j,currentCount)
         
      elif ("down" in where and i+1<max_i and "down"!=cameFrom):
         cur_i += 1
         cameFrom = "up"
         #checkChar(i+1,j,currentCount)
   print(cur_i,cur_j)
   return [cur_i,cur_j]



# load grid, find coordinates of S and which dir can it go
grid = []
S_adj =[]
for i in range(len(lines)): 
   for j in range (len(lines[i])):
      if lines[i][j]=="S":
         x = i
         y = j
         if ("up" in giveDir(lines[i+1][j]) and i<max_i):
            S_adj.append("down")
         
         if ("down" in giveDir(lines[i-1][j]) and i>0):
            S_adj.append("up")
            
         if ("right" in giveDir(lines[i][j-1]) and j<max_j):
            S_adj.append("left")
            
         if ("left" in giveDir(lines[i][j+1]) and j>0):
            S_adj.append("right")

   grid.append(list(lines[i].replace("\n","")))
   
n = 0
cameFrom =""
while (grid[x][y]!=0):
   newIndex = checkChar(x,y)
   x = newIndex[0]
   y = newIndex[1]
   n+=1

printList(grid)
print(int(n/2))