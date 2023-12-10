
import sys
lines = open("input8.txt","r").readlines()
inst = lines[0].replace("\n","")
dict = {}
start = []
maxnum= sys.maxsize

def listOfFactors(a):
   ab = a
   list =[a]
   i = 2
   while (True):
      if (i>a):
         break
      if (a%i==0):
         list.append(i)
         a/=i
      else:
         i+=1
   list.remove(ab)
   return list

for i in range(2,len(lines)):
   dict[lines[i].partition("=")[0].replace(" ","")] = lines[i].partition("=")[2][2:10].split(", ")
   if lines[i].partition("=")[0].replace(" ","")[2] == "A":
      start.append(lines[i].partition("=")[0].replace(" ",""))

n = 0
current = "AAA"
c = 0
zs = False
final = []
while (True):
   
   if c == len(inst):
      c = 0
      #print(start)
   
   for i in range (len(start)):
      if inst[c] == "L":
         start[i] = dict.get(start[i])[0] 
      elif inst[c] == "R":
         start[i] = dict.get(start[i])[1]
   
   c+=1
   n+=1
   #check
  
   for node in start:
      if node[2] == "Z":
         final.append(n)
   if (len(final) == len(start)):
      break
 
   
print("starT: ",start)
final = sorted(final)
print (final)

#zamijeniti veliki broj s listom njegovih faktora
for i in range(len(final)):
   final[i] = listOfFactors(final[i])

#print(final)
n = 1
#pomnoziti sve common faktore
for elem in final[0]:
   inside =True
   for list in final:
      if elem not in list:
         inside = False
   if inside:
      n*=elem
      #print("pomnozno", n)
      for list in final:
         list.remove(elem) # maknuti ih iz listi

#print(final,"again")
for list in final:
   for elem in list:
      n*=elem
      #print("pomnozno", n)
      for list in final:
         if (elem in list): list.remove(elem)
         #print("ney",final)

print(n)
file = open("output8.txt","w")
file.write(str(n))