inp = list(map(lambda line : [line.split()[0],int(line.split()[1])],open("day18/input18.txt","r").readlines()))
grid = []
print(inp)

dir = {"U": [-1,0], "R" : [0,1], "L" : [0,-1], "D" : [1,0]}

pov = 0
x = 0
y = 0
for com in inp:
   dx = dir.get(com[0])[0] * com[1]
   dy = dir.get(com[0])[1] * com[1]
   pov += (dx-x) * (dy)
   print(pov)
   x = dx+x
   y = dy+y