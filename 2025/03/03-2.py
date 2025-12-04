
file = open("input.txt","r")

total = 0

for line in file.readlines():
   j1 = max(num for num in line[:-13])
   print ("j1: ",j1)
   i = line.index(j1)
   number = j1
   
   for k in range(11):
      print ("range" ,i+1, -(11-k))
      j = max(num for num in line[i+1:-(11-k)])
      print ([num for num in line[i+1:-(11-k)]])
      number += j
      i = line[i+1:-(11-k)].index(j) + i+1
      
   print (number)
   total += int(number)
   
   
print ("total:",total)