   
def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

rez = 0

file = open("day4/input4.txt","r")
lines = file.readlines()

cards=zerolistmaker(len(lines))

for i in range (len(lines)):
   n = 0
   wining = lines[i].partition(":")[2].partition("|")[0].split()
   moji = lines[i].partition(":")[2].partition("|")[2].split()
   print(moji, "\n",wining)

   for elem in moji:
      if elem in wining:
         n+=1
   for k in range (i,i+n):
      cards[k+1] +=(1*(cards[i]+1))

   rez += cards[i]+1
   print(cards)
   n = 0

print(rez)
    
