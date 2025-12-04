
file = open("input.txt","r")

intervals = file.readline().split(',')
total = 0

for interval in intervals:
   start, stop = map(int,interval.split("-"))
   
   
   if len(str(start)) % 2 != 0:
      start = 10**(len(str(start))) 
      print ("new start :) ", start)
      
   # case number has even number of digits 
   chunk = (str(start))[:len(str(start))//2]
   
   while True:
      number = int(chunk+chunk)
      
      if start <= number <= stop:
         total += number
         print("found", number)
         
      if number >= stop:
         break
      
      chunk = str(int(chunk)+1)
      
print ("result", total)