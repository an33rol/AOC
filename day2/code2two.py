r = 0
g = 0
b = 0
n = 0

file = open("input2.txt","r")
lines = file.readlines()
for i in range (len(lines)):
   games = lines[i].partition(":")[2].split(";")
   for game in games:
      moze = True
      print(game)
      game = game.split(",")
      for one in game:
         if ("red" in one and int(one.split()[0])>r):
            if(int(one.split()[0])>r or r==0):
               r = int(one.split()[0])
         if ("green" in one and int(one.split()[0])>g):
            if(int(one.split()[0])>g or g==0):
               g = int(one.split()[0])
         if ("blue" in one and int(one.split()[0])>b):
            if(int(one.split()[0])>b or b==0):
               b = int(one.split()[0])
   print("MAX:",r,g,b)
   n+=(r*g*b)
   r = 0
   g = 0
   b = 0   
   
   
   print("----------------")
print("N:",n)