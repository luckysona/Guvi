''' PROGRAM TO PRINT THE ARMSTRONG NUMBERS BETWEEN TWO INTERVALS '''

a,b=input().split()
a=int(a)
b=int(b)
for i in range(a,b):
  sum=0
  temp=i
  while (temp>0):
    digit=temp%10
    sum+=digit**3
    temp//=10
  if (i==sum):
    print(i, end=" ")
