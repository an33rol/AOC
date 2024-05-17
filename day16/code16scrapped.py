
grid =  list(map(lambda line : list(line.replace("\n","")) ,open("day16/input16.txt","r").readlines()))
energized = [["" for elem in line] for line in grid]

max_i = len(grid)
max_j = len(grid[0])

def printMatrix(grid):
   for line in grid:
      print(line)


def giveDir(c,coming):
   match c:
      case "\\":
         match coming:
            case "left": return "down"
            case "down": return "left"
            case "up": return "right"
            case "right": return "up"

      case "/":
         match coming:
            case "left": return "up"
            case "down": return "right"
            case "up": return "left"
            case "right": return "down"
        
      case "|":
         match coming:
            case "up": return "down"
            case "down": return "up"
            case _: return ["up","down"]

      case "-":
         match coming: 
            case "left": return "right"
            case "right": return "left"
            case _: return ["left","right"]
      
   return []



def checkChar(i,j,comingfrom):
   dir = giveDir(grid[i][j],comingfrom)

   #energize
   curr = energized[i][j]
   if curr == "":
      energized[i][j] = 1      
   else:
      energized[i][j] = curr+1

   if len(dir) == 0:
      pass

   elif len(dir)==1:
      
      if ("left" in dir and j>0):
         return [i,j-1]

      if ("right" in dir and j+1<max_j):
         return[i,j+1]
         
      if ("up" in dir and i>0):
         return[i-1,j]
         
      if ("down" in dir and i+1<max_i):
         return[i+1,j]
      
   elif len(dir)==2:
      if "up" in dir:
         checkChar(i+1,j,dir[0])
         checkChar(i-1,j,dir[1])



comingfrom = "left"
i = 0
j = 0

while (i>=0 and i<max_i and j>=0 and j<max_j):
   checkChar(i,j,comingfrom)

checkChar(i,j,comingfrom)

printMatrix(energized)