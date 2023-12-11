newGrid = list(map(lambda string : list(string.replace("\n","")),open("day11/input11.txt","r").readlines()))

empty_rows = []
empty_cols = []

def justprint():
   for line in newGrid:
      print(line)

def d(a,b,x,y):
   mul = 2
   rowmul = 0
   colmul = 0

   for i in range (min(a,x), max(a,x),1):
      if i in empty_rows:
         #print("found empty row",i)
         rowmul+=1

   for j in range (min(b,y), max(b,y),1):
      if j in empty_cols:
         #print("found empty col",j)
         colmul+=1 

   return (abs(a-x) + abs(b-y) + rowmul * mul + colmul * mul - rowmul - colmul)



# adding columns
j = 0
while (j < len(newGrid[0])):
   prazan = True
   for k in range (len(newGrid)):
      if (newGrid[k][j] != "."):
         prazan = False
         break
   if prazan:
      empty_cols.append(j)
   j+=1

# adding rows
i = 0
while (i<len(newGrid)):
   if "#" not in newGrid[i]:
      empty_rows.append(i)
   i+=1

# list of positions of all galaxies
gala = [] 
for i in range(len(newGrid)):
   for j in range(len(newGrid[0])):
      if newGrid[i][j] == "#":
         gala.append([i,j])


# calc all distances
n = 0
print(gala)
for i in range(len(gala)):
   print("checking for galaxies", i)
   for j in range (len(gala)):
      n+=d(gala[i][0],gala[i][1],gala[j][0],gala[j][1])

print(int(n/2))