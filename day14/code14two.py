import gc
import numpy as np
inp = list(map(lambda elem : list(elem.replace("\n","")), open("day14/input14.txt").readlines()))

num = len(inp) # bit ce (num - index) za vrijednost
alln = 0


def printMatrix(m):
   for line in m:
      print (line)
   print()

def insertAsCol(mat,col):
   for k in range (len(mat)):
      mat[k].append(col[k])
      

def cycle():
   for i in range(4):
      tiltup()
      #print("after tilt")
      #printMatrix(inp)
      rotateall()

def tiltup(): #promijeni matricu
   global inp
   newmat = [ []for i in range(num)]
   for j in range (len(inp[0])):
      col = []
      empty = []
      cuberock = None
      n = 0

      for i in range (len(inp)):
         sample = inp[i][j]

         if sample == "#":
            cuberock = i

            itern = len(empty)
            for h in range(itern):
               col.append(".")
               empty.remove(empty[0])
            col.append("#")

         elif sample == ".":
            empty.append(i)

         elif sample == "O":
            if len(empty)!=0:
               if cuberock!= None and i > cuberock: #cube ce ga zaustavit
                  
                  found = False
                  for k in range (len(empty)):
                     if empty[k]>cuberock: #nadji prvi empty space nakon cuberocka
                        col.append("O")
                        #num-empty[k]
                        empty.remove(empty[k])
                        empty.append(i)
                        found = True
                        break

                  if not found: 
                     col.append("O")
                     #n += num-i

               else:  #ako nema cuberocks dodaj na prvu najnizu poziciju
                  col.append("O")
                  #n += num-empty[0]
                  empty.remove(empty[0])
                  empty.append(i)

            else: #ostaje tu
               col.append("O")
               #n += num-i
      while(len(col)!=num):
         col.append(".")
      insertAsCol(newmat,col)
      
      #newmat = np.hstack((newmat,col))
      #print(newmat)
      
   inp = newmat
   del newmat
   gc.collect()

def loadOnBeams(matrix):
   n = 0
   for i in range(num):
      for j in range (num):
         if matrix[i][j] == "O":
            n += num-i
   return n

def rotateall(): #rotates cw
   global inp
   inp = [[inp[j][i] for j in range (len(inp)-1,-1,-1)] for i in range (len(inp))]


"""
def rotate_matrix( m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
"""


for i in range(1000): #1000
   if i%1000 == 0:
      print(i)
   cycle()

print("finally")
printMatrix(inp)

print(loadOnBeams(inp))
