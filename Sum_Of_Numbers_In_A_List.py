''' PROGRAM TO CALCULATE SUM OF NUMBERS IN A LIST ''' 
a,b=input().split()
a=int(a)
b=int(b)
c = list(map(int,input().strip().split()))[:a] 
sum=0
for i in range(0,b):
  sum+=c[i]
print(sum)
