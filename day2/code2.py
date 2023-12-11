r = 12
g = 13
b = 14
n = 0

file = open("day2/input2.txt","r")
lines = file.readlines()
for i in range (len(lines)):
   games = lines[i].partition(":")[2].split(";")
   for game in games:
      moze = True
      print(game)
      game = game.split(",")
      for one in game:
         if ("red" in one and int(one.split()[0])>r):
            moze = False
            break
         if ("green" in one and int(one.split()[0])>g):
            moze = False
            break
         if ("blue" in one and int (one.split()[0])>b):
            moze = False
            break
      if not moze:
         break
   
      
   if moze:
      print("moz")
      n+=(i+1)
   print("----------------")
print("N:",n)