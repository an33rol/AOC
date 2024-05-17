import re
file = open("day19/input19.txt","r")
workflow={}

line = file.readline()
while line !="\n":
   workflow[line.partition("{")[0]] = line.partition("{")[2].replace("}","").replace("\n","").split(",")
   line = file.readline()

range = {"x":[],"m":[],"a":[],"s":[]}
 


n = 0

print(n)