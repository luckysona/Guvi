''' PROGRAM TO FIND THE GIVEN LIST IS IN SORTED ORDER '''
a=int(input())
b=input().split()
c=[]
for i in b:
  c.append(int(i))
c1=0
c.sort()
for i in range(0,len(c)):
  if(int(b[i])==c[i]):
    c1+=1
if(c1==len(b)):
  print('yes')
else:
  print('no')
