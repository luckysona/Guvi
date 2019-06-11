''' PROGRAM TO PRINT MAXIMUM THREE NUMBERS AFTER ADDING TWO LIST NUMBERS '''
a,b=map(int,input().split())
a1=list(map(int,input().split()))
b1=list(map(int,input().split()))
a1=a1+b1
a1.sort()
print(a1[-1],a1[-2],a1[-3])
