
rez = 0
line=""
a = ""

file = open("day1/input1.txt","r")
lines = file.readlines()
for i in range (len(lines)):
   print(lines[i])
   for j in range (len(lines[i])):
      if (lines[i][j].isdigit()):
         a+=lines[i][j]
         break

   for j in range (len(lines[i])-1,-1, -1):
      if (lines[i][j].isdigit()):
         a+=lines[i][j]
         break
   
   rez += int(a)
   print(a)
   a = ""

print (rez)




