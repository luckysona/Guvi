''' PROGRAM TO PRINT INTEGER IN REVERSE '''
a=int(input())
c=0
r=0
while(a>0):
  c+=1
  r=(r*10)+(a%10)
  a//=10
print(r)
