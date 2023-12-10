
rez = 0
line=""
a = ""
nums = ["one", "two", "three", "four","five","six","seven","eight","nine"]   

file = open("input1.txt","r")
lines = file.readlines()
for i in range (len(lines)):
   print(lines[i])
   for j in range (len(lines[i])):
      if (lines[i][j].isdigit()):
         a+=lines[i][j]
         break
      for k in range (9):
         if(nums[k] in lines[i][0:j+1:]):
            a+=str(k+1)
            break
      if (a!=""): break

   for j in range (len(lines[i])-1,-1, -1):
      if (lines[i][j].isdigit()):
         a+=lines[i][j]
         break
      for k in range (9):
         if(nums[k] in lines[i][j::]):
            a+=str(k+1)
            break
      if (len(a)>1): break
   
   rez += int(a)
   print(a)
   a = ""

print (rez)




