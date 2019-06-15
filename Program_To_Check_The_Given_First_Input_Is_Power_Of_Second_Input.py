''' PROGRAM TO GIVEN NUMBER IS POWER OF ANOTHER NUMBER '''
a,b=list(map(int,input().split()))
c=b
while(b<a):
  b*=c
  if(b==a):
    break
if(b==a):
  print("yes")
else:
  print("no")
