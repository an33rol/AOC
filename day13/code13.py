samples = list(map(lambda elem : elem.replace("\n",""), open("day13/input13.txt").readlines()))
#print (samples)

def check(sample):
   global suma
   print("checking")

   rows = checkRows(sample)
   cols = checkCols(sample)
   n.append([rows,cols])
   """
   if rows != 0:

      print("found horizontal")
      n.append(rows)
      suma+=(rows*100)
   else:
      
      if cols!=0:
         print("found vertical")
         n.append(cols)
         suma+=cols
         """
   
   suma+= checkRows(sample)*100 + checkCols(sample)

def checkRows(sample):
   index = findFirstRow(sample)
   if (index != False):
      if(checkOtherRows(sample,index[0],index[1])):
         return (index[0]+index[1])//2+1
   return 0
   
def checkCols(sample):
   index = findFirstCol(sample)
   print(index)
   if (index != False):
      if(checkOtherCols(sample,index[0],index[1])):
         return (index[0]+index[1])//2+1
   return 0

def findFirstRow(sample):
   imp = -1
   jmp = -1
   for i in range(len(sample)):
      if (imp!=-1):
         break
      for j in range(len(sample)-1,-1,-1):
         #print(list(zip(sample[i],sample[j])))
         if all(x == y for x,y in list(zip(sample[i],sample[j]))) and i!=j:
            imp = i
            jmp = j
            break
   print("imp i jmp:",imp,jmp)
   if (imp != 0 and jmp != len(sample)-1): #ne pocinju s kraja
      return False
   print(imp,jmp)
   return [imp,jmp]

def findFirstCol(sample):
   imp = -1
   jmp = -1
   for i in range(len(sample[0])):
      if imp!=-1:
         break
      for j in range(len(sample[0])-1,-1,-1):
         if all(x == y for x,y in list(zip([row[i] for row in a],[row[j] for row in a]))) and i!=j:
            #print(list(zip(([row[i] for row in a],[row[j] for row in a]))))

            if (i == 0 or j == len(sample[0])-1): #ne pocinju s kraja
               imp = i
               jmp = j
               break
   #print("imp i jmp", imp,jmp)
   
   return [imp,jmp]

def checkOtherRows(sample,imp,jmp):
   i = imp
   j = jmp
   while i<j:
      if not all(x == y for x,y in list(zip(sample[i],sample[j]))):
            #print("error in ", i, j)
            return False
      i+=1
      j-=1

   return True

def checkOtherCols(sample,imp,jmp):
   i = imp
   j = jmp
   while i<j:
      if not all(x == y for x,y in list(zip([row[i] for row in sample],[row[j] for row in sample]))):
            #print("error in ", i, j)
            return False
      i+=1
      j-=1

   return True



n = []
suma = 0
a=[]
for line in samples:
   if(line!=""):
      a.append(line)
   else:
      check(a)
      a = []

check(a)

print(n)
print(suma)