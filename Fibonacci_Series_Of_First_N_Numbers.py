''' PROGRAM TO PRINT FIBONACCI SERIES OF FIRST N NUMBERS '''
a=int(input())
n1=0
n2=1
for num in range(1,a+1):
  if(num<=1):
     next=num
  else:
    next=n1+n2
    n1=n2
    n2=next
  print(next,end=" ")
