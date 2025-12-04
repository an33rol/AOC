
file = open("input.txt","r")

total = 0

for line in file.readlines():
   j1 = max(num for num in line[:-2])
   print ("j1: ",j1)
   i1 = line.index(j1)
   
   j2 = max(num for num in line[i1+1:])
   print (str(j1) + str(j2))
   total += int(str(j1) + str(j2))
   
   
print ("total:",total)