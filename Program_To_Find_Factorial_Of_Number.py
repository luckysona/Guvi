''' PROGRAM TO FIND FACTORIAL OF GIVEN NUMBER '''
a=int(input())
b=1
if(a==0):
  print(1)
else:
  for i in range(1,a):
    b=b+(b*i)
  print(b)
