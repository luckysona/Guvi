''' PROGRAM TO PRINT MAXIMUM NUMBERS AFTER ADDING TWO LIST NUMBERS '''
a,b=map(int,input().split())
a1=list(map(int,input().split()))
b1=list(map(int,input().split()))
a1=a1+b1
a1.sort()
a1.reverse()
for i in range(0,b):
  print(a1[i],end=" ")
