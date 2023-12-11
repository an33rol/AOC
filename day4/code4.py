rez = 0
file = open("day4/input4.txt","r")
lines = file.readlines()
for i in range (len(lines)):
   mul = 0
   wining = lines[i].partition(":")[2].partition("|")[0].split()
   moji = lines[i].partition(":")[2].partition("|")[2].split()
   print(moji, "\n",wining)

   for elem in moji:
      if elem in wining:
         if mul == 0:
            mul = 1
         else:
            mul*=2
   rez += mul
   print(mul)
   mul = 0

print(rez)
    
      