''' PROGRAM TO PRINT THE SORTING OF ALL GIVEN LIST ELEMENTS '''
a=int(input())
l=list(map(int,input().split()))
for i in range(0,a-1):
  n=list(map(int,input().split()))
  for j in n:
    if j not in l:
      l.append(j)
print(*sorted(l))
