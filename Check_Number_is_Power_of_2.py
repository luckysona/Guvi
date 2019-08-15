''' CHECK THAT GIVEN NUMBER IS A POWER OF 2 OR NOT '''
num=int(input())
a=1
if(num==0):
  a=0
while(num!=1):
  if(num%2!=0):
    a=0
  num=num//2
if(a==0):
  print('no')
else:
  print('yes')
