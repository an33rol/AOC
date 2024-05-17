grid = list(map(lambda a : list(map(lambda a: int(a),list(a.replace("\n","")))),open("day17/input17.txt","r").readlines()))

max_i = len(grid)
heatloss = grid[0][0]

allheatloss = []

visited = []

def algorithm(i,j,curblocks,dirofblock,curheatloss): #0 = desno, 1 = gore, 2 = lijevo, 3 = dolje
   print(i,j)
   if i == max_i-1 and j == max_i-1 :
      allheatloss.append(curheatloss)
      return
   
   if (i<max_i-1 and curblocks!=3 and dirofblock!=3 and str(i+1)+str(j) not in visited): # ide dolje
      curheatloss+= grid[i+1][j]
      visited.append(str(i+1)+str(j))
      if dirofblock==3: 
         curblocks+=1
      else:
         curblocks = 0
      algorithm(i+1,j,curblocks,3,curheatloss)
   
   if (j<max_i-1 and curblocks!=3 and dirofblock!=0 and str(i)+str(j+1) not in visited): #ide desno
      curheatloss+= grid[i][j+1]
      visited.append(str(i)+str(j+1))
      if dirofblock==0: 
         curblocks+=1
      else:
         curblocks = 0
      algorithm(i,j+1,curblocks,0,curheatloss)

   if (i>0 and curblocks!=3 and dirofblock!=1 and str(i-1)+str(j) not in visited): # ide gore
      curheatloss+= grid[i-1][j]
      visited.append(str(i-1)+str(j))
      if dirofblock==1: 
         curblocks+=1
      else:
         curblocks = 0
      algorithm(i-1,j,curblocks,1,curheatloss)

   if (j>0 and curblocks!=3 and dirofblock!=2 and str(i)+str(j-1) not in visited):
      curheatloss+= grid[i][j-1]
      visited.append(str(i)+str(j-1))
      if dirofblock==2: 
         curblocks+=1
      else:
         curblocks = 0
      algorithm(i,j-1,curblocks,2,curheatloss)
   return
   

minnum = len(grid)**2*9
startingpoint = [0,0]

algorithm(0,0,0,4,heatloss)

print(allheatloss)

