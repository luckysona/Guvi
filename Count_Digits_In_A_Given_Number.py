''' PROGRAM TO COUNT DIGITS IN A GIVEN NUMBER '''
a=int(input())
b=0
while(a>0):
  b+=1
  a//=10
print(b)
