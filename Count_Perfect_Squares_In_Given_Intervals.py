''' PROGRAM TO COUNT PERFECT SQUARES IN GIVEN INTERVALS '''
a,b=input().split()
a=int(a)
b=int(b)
i=1
c=0
while(i<b):
  s=i*i
  if(s<b and s>a):
    c+=1
  i+=1
print(c)
