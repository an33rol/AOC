input = list(map(lambda a : a.split(), open("input7.txt","r").readlines()))
values= {"A" : 12, "K" : 11, "Q" : 10, "J" : 0, "T" : 9}
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
   add = 0

   if ("J" in hand):
      add = i[0].count("J")
   
   comb = 0 
   a = []
   while(len(hand)>0):
      card = getValue(hand[0])
      if (card != 0):
         a.append( i[0].count(hand[0]))
      hand = removeAll(hand, hand[0])

   if (len(a) == 0):
      a.append(0)

   print(a,add)

   for b in a:
      if (b == max(a)):
         comb+= pow(10, (b+add))
         add = 0
      else:
         comb+= pow(10, (b))

       
      

   hand = i[0]
   handval = 0
   for j in range(len(hand)):
      card = getValue(hand[j])
      handval += card * pow(13,(4-j)) 

   final.append([ int(i[1]), comb, handval, i[0] ])

n = 0
i = 1

for v in (sorted(final, key = lambda final : (final[1],final[2]))):
   print(v)
   n += v[0] * i
   i+=1

print(n)