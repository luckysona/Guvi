''' PROGRAM TO FIND WHICH NUMBER COMES ONLY ONCE '''
a=int(input())
i_string=input()
l=i_string.split()
b=[]
for i in range(0,len(l)):
  c=l.count(l[i])
  b.append(c)
for i in range(0,len(b)):
  if(b[i]==1):
    print(l[i])
