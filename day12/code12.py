file = open("day12/input12.txt","r")
dict = {}

def func (data, nums):
   global n
   nums = nums.copy()
   broj = nums[0]
   #print("i ide do ", len(data)-broj)
   hashindex = len(data)+1
   for i in range (len(data)-broj+1): #+1
      substring = data[i:i+broj:]
      print("substring:",substring, "-----",data,i, broj+i)

      if (i>hashindex):
            #print("returning",i,hashindex)
            return
      
      if "." not in substring and (i+broj >= len(data)-broj or data[i+broj]!= "#" ) and "#" not in data[i-1:i:]:
         #print("found substring:",substring)
         
         if ("#" in substring and hashindex ==len(data)+1):
            hashindex = data.index("#")
            #print(hashindex)

         if (len(nums[1:])!=0):
            
            print("nxt substring:", data[i+broj+1::], "passing nums:",nums[1:])
            func(data[i+broj+1::],nums[1:])
         
         else:
            print("adding 1 normally")
            n+=1

         

         #dict[data[i:nums[0]:1]] = 
   

line = file.readline()
n = 0
ns = []
while (line != ""):
   #print()
   data = line.split()[0]
   nums = list(map(int,line.split()[1].split(",")))
   #print(data, nums)
   
   func(data,nums)
   if n == 140:
      print(data,nums)
   ns.append(n)
   n = 0

   line = file.readline()

print(ns)
print(sum(ns))