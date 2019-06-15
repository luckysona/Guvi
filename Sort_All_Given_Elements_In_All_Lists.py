''' PROGRAM TO PRINT THE SORTING OF ALL GIVEN LIST ELEMENTS '''
a=int(input())
l=[]
for i in range(0,a):
  l.append(input())
l1=[]
for i in l:
  a1=i.split()
  for j in a1:
    l1.append(j)
l1.sort()
print(l1)
