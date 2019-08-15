''' CHECK IF THE GIVEN NUMBER IS DIVISILE BY ANY NUMBER LESS THAN N OTHER THAN 1 '''
num=int(input())
a=0
for i in range(2,num):
  if(num%i==0):
    a=1
if(a==1):
  print('yes')
else:
  print('no')
