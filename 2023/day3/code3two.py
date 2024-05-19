b = {}
gears= {}
dot = "*"
n = 0
   
def addGear(index,val):
   if (index in gears.keys()):
      gears.update({index:[gears.get(index)[0]+1,gears.get(index)[1]*val]})           
   else:
      gears[index]=[1,val]

   
file = open("day3/input3.txt","r")
lines = file.readlines()

for i in range (len(lines)):
   a = list(lines[i])
   b[i] = a

list = []
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
                  if (b[i+k][j+l]==dot and i+k>=0 and j+l>=0):
                     good = True
                     list.append((i+k)*10000+(j+l))
                     break
               
               except:
                  good = False

         if good:
            j+=1

            while(b[i][j].isdigit()):
               first+=b[i][j]
               j+=1
         
            for index in list:               
               addGear(index,int(first))

            list = []
            first = ""

      else:
         if(first !=""):
            first = ""
      j+=1

#print(gears)

for key in gears.keys():
   if(gears.get(key)[0]!=1):
      n+=gears.get(key)[1]
   

print("N = ",n)