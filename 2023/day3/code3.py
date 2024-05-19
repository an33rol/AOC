b = {}
dot = "."
n = 0

file = open("day3/input3.txt","r")
lines = file.readlines()

for i in range (len(lines)):
   a = list(lines[i])
   b[i] = a

first=""
for i in range (len(b)):
   j = 0
   while(j<len(b[i])):
      if b[i][j].isdigit():
         if (first==""):
            first = b[i][j]
         else: first+=b[i][j]

         #check
         good = False
         for k in range (-1,2,1):
            if good: break
            for l in range (-1,2,1):
               try:
                  if (b[i+k][j+l]!=dot and i+k>=0 and j+l>=0 and not b[i+k][j+l].isdigit()):
                     good = True
                     break
               
               except:
                  good = False
                  
         if good:
            j+=1
            while(b[i][j].isdigit()):
               first+=b[i][j]
               j+=1
            #print("ADDED ",first)
            n+=int(first)
            first = ""

      else:
         if(first !=""):
            first = ""
            #print("DELETED")
      j+=1

print("N = ",n)