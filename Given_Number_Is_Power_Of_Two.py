''' PROGRAM TO CHECK THE NUMBER IS POWER OF 2 '''
a=int(input())
b=1
c=0
while(b<a):
  c+=1
  b=2**c
if(b==a):
  print("yes")
else:
  print("no")
