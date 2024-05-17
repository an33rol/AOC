inp = (open("day15/input15.txt").readline()).split(",")

nall = 0
for chars in inp:
   n = 0
   for k in chars:
      if k!="\n":
         n = ((n+ord(k))*17)%256
   print (n)
   nall += n

print(nall)