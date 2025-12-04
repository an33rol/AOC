lock = 50
p = 0

file = open("input.txt","r")

for line in file.readlines():
   if line.startswith("L"):
      lock -= int(line[1:])
      while lock < 0: lock += 100
      
   else:
      lock += int(line[1:])
      while lock > 99: lock -= 100
   print (lock)
   
   if lock == 0: p += 1

      
print (p)