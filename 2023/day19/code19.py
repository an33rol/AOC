import re
file = open("day19/input19.txt","r")
workflow={}

line = file.readline()
while line !="\n":
   workflow[line.partition("{")[0]] = line.partition("{")[2].replace("}","").replace("\n","").split(",")
   line = file.readline()


def processinp(line):
   return list(map(lambda a: int(a),re.sub("[{}xmas=]","",line).split(",")))

def accepted(dict):
   wf = workflow.get("in")
   nextwf = ""

   while True:
      nextwf = ""
      for cond in wf:
         if ":" not in cond:
            nextwf = cond

         elif ">" in cond:
            if dict.get(cond[0]) > int(cond.partition(":")[0].partition(">")[2]):
               nextwf = cond.partition(":")[2]
         elif "<" in cond:
            if dict.get(cond[0]) < int(cond.partition(":")[0].partition("<")[2]):
               nextwf = cond.partition(":")[2]
               
         if nextwf == "A":
            return True
         elif nextwf == "R":
            return False
         elif nextwf !="":
            break
      
      wf = workflow.get(nextwf)

n = 0

line = file.readline()
while len(line)!=0:

   line = processinp(line)
   #print(line)
   dict = {"x":line[0],"m":line[1],"a":line[2],"s":line[3]}
   if (accepted(dict)):
      #print("accepted")
      n+= sum(dict.values())

   line = file.readline()

print(n)