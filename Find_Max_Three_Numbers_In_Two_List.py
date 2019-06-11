''' PROGRAM TO PRINT MAXIMUM OF THREE NUMBERS AFTER ADDING TWO LIST NUMBERS '''
a,b=map(int,input().split())
a1=list(map(int,input().split()))
b1=list(map(int,input().split()))
a1=a1+b1
a1.sort()
a1.reverse()
c1=[]
for i in range(0,b):
  c1.append(a1[i])
c1.reverse()
for i in c1:
  print(i,end=" ")
