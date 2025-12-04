lock = 50
p = 0

file = open("input.txt","r")

for line in file.readlines():
   print (line)
   if line.startswith("L"):
      # started with 0 
      if lock == 0: p -= 1
      
      lock -= int(line[1:])
      while lock < 0: 
         p += 1
         print("p",p)
         lock += 100
      if lock == 0: p += 1

      
   else:
      lock += int(line[1:])
      print ("lockkk", lock)
      while lock > 99: 
         p += 1
         print("p",p)
         
         lock -= 100
   
   
   print ("lock",lock)


      
print ("final",p)