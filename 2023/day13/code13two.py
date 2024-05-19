def transpose(a):
   b = []
   for i in range(len(a[0])):
      c = []
      for j in range(len(a)):
         c.append(a[j][i])
      b.append(c)
   return b


def check(sample):
   global suma
   rows = checkRows(sample)
   n.append(rows)
   return rows

def checkRows(sample):
   index = findFirstRow(sample)
   if (index != False):
      return (index[0]+index[1])//2+1
   return 0
   
def findFirstRow(sample):
   imp = -1
   jmp = -1
   for i in range(len(sample)):

      if (imp!=-1):
         break
         
      for j in range(len(sample)-1,i,-1):
         
         if (abs(i-j)%2!=0):
            if (i == 0 or j == len(sample)-1):
               if  errorNumInOtherRows(sample,i,j) == 1:
                  imp = i
                  jmp = j
                  break
   return [imp,jmp]

def errorNumInOtherRows(sample,imp,jmp):
   i = imp
   j = jmp
   ers = 0
   while i<j:
      if not all(x == y for x,y in list(zip(sample[i],sample[j]))):
            ers += diff(sample[i],sample[j])
            if(ers>1):
               return ers
            
      i+=1
      j-=1
   return ers


def diff(a,b):
   n = 0
   for i in range (len(a)):
      if a[i]!=b[i]:
         n+=1
   return n

n = []
suma = 0
a = []
samples = list(map(lambda elem : elem.replace("\n",""), open("day13/input13.txt").readlines()))
print(samples)

for line in samples:
   if(line!=""):
      a.append(list(line))
   else:
      suma += check(a)*100
      suma += check(transpose(a))
   
      a = []


suma += check(a)*100
suma += check(transpose(a))

print(n)
print(suma)