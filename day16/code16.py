import sys
sys.setrecursionlimit(1000000) #lol

passedhere = {}

grid =  list(map(lambda line : list(line.replace("\n","")) ,open("day16/input16.txt","r").readlines()))
energized = [["" for elem in line] for line in grid]

max_i = len(grid)
max_j = len(grid[0])

def printMatrix(grid):
   for line in grid:
      print(line)

def add(list1, list2):
   list = []
   for k in range (len(list1)):
      list.append(list1[k]+list2[k])
   return list

def giveDir(c,coming): #[i,j]
   match c:
      case "\\":
         match coming:
            case [0,1]: return [[1,0]] #ide od desno
            case [1,0]: return [[0,1]]
            case [-1,0]: return [[0,-1]]
            case [0,-1]: return [[-1,0]]

      case "/":
         match coming:
            case [0,-1]: return [[1,0]]
            case [1,0]: return [[0,-1]]
            case [-1,0]: return [[0,1]]
            case [0,1]: return [[-1,0]]
        
      case "|":
         match coming:
            case [-1,0]: return [[-1,0]]
            case [1,0]: return [[1,0]]
            case _: return [[-1,0],[1,0]]

      case "-":
         match coming: 
            case [0,-1]: return [[0,-1]]
            case [0,1]: return [[0,1]] 
            case _: return [[0,1],[0,-1]]
      
   return [coming]


def checkChar(i,j,comingfrom):
   if(i<0 or j<0 or i==max_i or j== max_j):
      return
   
   energylvl = energized[i][j]
   
   dir = giveDir(grid[i][j],comingfrom)
  
   if energylvl == "":
      energized[i][j] = 1
   elif energylvl == 1 and grid[i][j]!=".":
      strdir = str(dir[0][0])+str(dir[0][1])
      if str(i)+str(j) in passedhere.keys():
         if strdir in passedhere[str(i)+str(j)]:
            return
         else:
            passedhere.get(str(i)+str(j)).append(strdir)
            if (len(dir) !=1):
               passedhere.get(str(i)+str(j)).append(str(dir[1][0])+str(dir[1][1]))
            
      else:
         passedhere[str(i)+str(j)] = [strdir]
         
   else:
      energized[i][j] = energylvl+1
 
   
   if len(dir) != 2: 
      currentpos = add([i,j],dir[0])
      checkChar(currentpos[0],currentpos[1],dir[0])
   
   else:
      checkChar(add([i,j],dir[0])[0],add([i,j],dir[0])[1],dir[0])
      checkChar(add([i,j],dir[1])[0],add([i,j],dir[1])[1],dir[1])


checkChar(0,0,[0,1])

def numOfEnergized(mat):
   n = 0
   for line in mat:
      n += line.count("")
   return max_i*max_i-n

print(numOfEnergized(energized))
