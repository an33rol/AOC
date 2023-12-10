file = open("input6.txt","r")
times = list(map(int,file.readline()[5::].split()))
dis = list(map(int,file.readline()[9::].split()))
rez = 1
found = False
print(times,dis)
for i in range(len(times)):
   for m in range (1,times[i]+1):
      if (m*(times[i]-m) > dis[i]):
         rez *= times[i] - (m-1)*2 - 1
         print(rez)
         break

print(rez)