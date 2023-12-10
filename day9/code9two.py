def findPrev (array):
   #print(array)
   if (not any(array)):
      return 0
   a = []
   for k in range (len(array)-1):
      a.append(array[k+1]-array[k])
   return - findPrev(a) + array[0]

lines =  open("input9.txt","r").readlines()

n = 0
for line in lines:
   array = list(map(int,line.replace("\n","").split()))
   n += findPrev(array)

print(sum)