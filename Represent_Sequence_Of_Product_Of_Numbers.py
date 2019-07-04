''' PROGRAM TO MAKE SOME SEQUENCE OF ELEMENTS PRODUCT EXCEPT
THE FOLLOWING INDEX '''
a=int(input())
l=list(map(int,input().split()))
p=1
t=[]
for i in range(len(l)):
  p=1
  for j in range(0,len(l)):
    if(j==i):
      p=p*1
    else:
      p=p*l[j]
  t.append(p)  
for i in t:
  print(i,end=" ")
