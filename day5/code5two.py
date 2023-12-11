#  komentar : ovo je pobjeda na svim razinama. ovakvo ushicenje nisam osjecala danima. da sam barem citala vise knjiga u djetinjstvu 
# tako da sada mogu bolje opisati svoje osjecaje. zelim zahvaliti akademiji-

import sys
file = open("day5/input5.txt","r")
lines = file.readlines()
maxnum= sys.maxsize

def checkSeed(seed):
   i = 0
   while(i<len(seeds)):
      if (seed > seeds[i] and seed < seeds[i] + seeds[i+1]):
         return True
      i+=2

   return False
   
#load data
seeds = list(map(int,lines[0][6::].split()))
pod = []
a = []
for i in range (3,len(lines)):
   if (lines[i]!="\n"):
      if (not lines[i].split()[0].isdigit()):
         pod.append(a)
         a = []
      else:
         a.append(list(map(int,lines[i].split())))
pod.append(a)

found = False

for soil in range (147000000,maxnum): # range start je definiran nakon sto se vec vrtilo od 0 nekih 15 minuta
   if(soil%1000000==0):
      print("soil: ", soil) # da mi da neku nadu
   nextstep = soil
   for sector in range(len(pod)-1,-1,-1):
      
      for line in pod[sector]:
         if (nextstep>=line[0] and nextstep<line[0]+line[2]):
            nextstep = line[1] + nextstep - line[0]
            break

   if(checkSeed(nextstep)) : 
      found = True
      break
   
         
file = open("output5.txt","w") # nepotrebno, mislila sam ic spavat

print("finally: ",soil)
file.write("ako je ovo krivo ubit cu se: "+str(soil))

         
