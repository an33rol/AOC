file = open("input6.txt","r")
time = int("".join(list(file.readline()[5::].split())))
dis = int("".join(list(file.readline()[9::].split())))
rez = 0
found = False
print(time,dis)

for m in range (1,time):
   if (m*(time-m) > dis):
      rez = time - (m-1)*2 - 1
      print(rez)
      break

print(rez)
