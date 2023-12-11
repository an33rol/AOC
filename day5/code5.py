import sys
file = open("day5/input5.txt","r")
lines = file.readlines()
minseed= sys.maxsize

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
print (pod)


i = 0
while (i<len(seeds)):
   seed = seeds[i]

   for j in range (len(pod)):
      for k in range(len(pod[j])): 
         if (seed>=pod[j][k][1] and seed<pod[j][k][1]+pod[j][k][2]):
               seed = pod[j][k][0] + (seed-pod[j][k][1])
               break
      #print(seed)
              
   minseed =  min(minseed,seed)
   i+=1

print("finally: ",minseed)
         
