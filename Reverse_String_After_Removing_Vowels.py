''' PROGRAM TO REVERSE STRING AFTER REMOVING VOWELS '''
a=int(input())
l=input()
b=[]
for i in l:
  b.append(i)
c=['a','e','i','o','u']
b.reverse()
for i in b:
  if i in c:
    continue
  else:
    print(i,end="")
