
def diff(a,b):
   n = 0
   for i in range (len(a)):
      if a[i]!=b[i]:
         n+=1
   return n

a = ['#', '.', '#', '#', '.', '.', '#', '#', '.']
b = ['.', '.', '#', '#', '.', '.', '#', '#', '.']

print(diff(a,b))