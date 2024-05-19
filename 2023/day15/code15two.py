inp = (open("day15/input15.txt").readline()).replace("\n","").split(",")
print(inp)
def hashnum(str):
   n = 0
   for k in str:
      n = ((n+ord(k))*17)%256
   return n

dict = {} # boxnum : dictofthings
for thing in inp:

   if "=" in thing:
      tag = thing.partition("=")[0]
      num = thing.partition("=")[2]
      boxnum = hashnum(tag)

      if boxnum not in dict.keys():
         dict[boxnum] = {}
      dict.get(boxnum)[tag] = num

   if "-" in thing:
      tag = thing.partition("-")[0]
      boxnum = hashnum(tag)

      if boxnum in dict.keys() and tag in dict[boxnum].keys():
         dict[boxnum].pop(tag)

n = 0
for k in dict.keys():
   i = 1
   for key in dict[k]:
      n += (1+k) * i * int(dict[k][key])
      i+=1
      print(n)

print(dict)
print(n)

