''' PROGRAM TO PRINT SUM OF SQUARES OF ITS DIGIT '''
a=int(input())
s=0
while(a>0):
  n=a%10
  s+=n*n
  a//=10
print(s)
