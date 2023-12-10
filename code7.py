input = list(map(lambda a : a.split(), open("input7.txt","r").readlines()))
values= {"A" : 12, "K" : 11, "Q" : 10, "J" : 0, "T" : 8}
final = []

def getValue(a):
   if (a.isdigit()):
      return int(a)-1
   else: 
      return values.get(a)

def removeAll(list, item):
   return [i for i in list if i !=item]

for i in input:
   hand = i[0]
   
   bestval = 0
   while(len(hand)>0):
      card = getValue(hand[0])
      bestval += pow(10, (i[0].count(hand [0])-1))
      hand = removeAll(hand,hand[j])
      

   hand = i[0]
   j = 0
   handval = 0
   while(j<len(hand)):
      card = getValue(hand[j])
      handval += card * pow(13,(4-j)) #upitno
      j+=1

   final.append([ int(i[1]), bestval, handval, i[0] ])

n = 0
i = 1

for v in (sorted(final, key = lambda final : (final[1],final[2]))):
   n += v[0] * i
   i+=1

print(n)