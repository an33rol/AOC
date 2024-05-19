inp = list(map(lambda elem : elem.replace("\n",""), open("day14/input14.txt").readlines()))

num = len(inp) # bit ce (num - index) za vrijednost
alln = 0
for j in range (len(inp[0])):
   empty = []
   cuberock = None
   n = 0

   for i in range (len(inp)):
      sample = inp[i][j]

      if sample == "#":
         cuberock = i
         empty = []

      elif sample == ".":
         empty.append(i)

      elif sample == "O":
         if len(empty)!=0:
            if cuberock!= None and i > cuberock: #cube ce ga zaustavit
               
               found = False
               for k in range (len(empty)):
                  if empty[k]>cuberock: #nadji prvi empty space nakon cuberocka
                     n += num-empty[k]
                     empty.remove(empty[k])
                     empty.append(i)
                     found = True
                     break

               if not found: 
                  n += num-i

            else:  #ako nema cuberocks dodaj na prvu najnizu poziciju
               n += num-empty[0]
               empty.remove(empty[0])
               empty.append(i)

         else: #ostaje tu
            n += num-i

   print(n)
   alln += n

print(alln)