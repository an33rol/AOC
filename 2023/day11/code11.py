grid = list(map(lambda string : list(string.replace("\n","")),open("day11/input11.txt","r").readlines()))

newGrid = grid

def writeInOutput(array):
   file = open("output11.txt","w")
   for line in array:
      for elem in line:
         file.write(elem)
      file.write("\n")
   file.close()

def justprint():
   for line in newGrid:
      print(line)

def insertColumn(j):
   for line in newGrid:
      line.insert(j,".")

def d(a,b,x,y):
   return abs(a-x)+abs(b-y)



# adding columns
j = 0
while (j < len(newGrid[0])):
   prazan = True
   for k in range (len(newGrid)):
      if (newGrid[k][j] != "."):
         prazan = False
         break
   if prazan:
      j+=1
      insertColumn(j)
   j+=1

# adding rows
i = 0
while (i<len(newGrid)):
   if "#" not in newGrid[i]:
      newGrid.insert(i,newGrid[i])
      i+=1
   i+=1

# list of positions of all galaxies
gala = [] 
for i in range(len(newGrid)):
   for j in range(len(newGrid[0])):
      if grid[i][j] == "#":
         gala.append([i,j])

#print(gala)

# calc all distances
n = 0
for i in range(len(gala)):
   for j in range (len(gala)):
      n+=d(gala[i][0],gala[i][1],gala[j][0],gala[j][1])


writeInOutput(newGrid)
print(int(n/2))