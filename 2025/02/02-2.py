
file = open("input.txt","r")

intervals = file.readline().split(',')
total = 0

for interval in intervals:
   print ("intervalll", interval)
   start, stop = map(int,interval.split("-"))
   
   # n number of digits 
   for n in range(1,len(str(stop))//2+1):
      print ("n", n)
      n_start = len(str(start))
      n_stop = len(str(stop))
   
      
      # najmanji chunk koji se moze ponavljati
      chunk = str(int((str(start))[:n])-1)
      
      # chunks_valid = True
      # while chunks_valid:
            
         # koliko puta se chunk moze ponoviti   
      for i in range(n_start//len(chunk), n_stop//len(chunk)+1):
         print (chunk) 
         number = int(chunk*i)
         print ("NUMBER",number)
         
         if start <= number <= stop:
            total += number
            print("found", number)

         if number >= stop:
            # chunks_valid = False
            break
         
      chunk = str(int(chunk)+1)
         

      
print ("result", total)