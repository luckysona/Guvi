''' PROGRAM TO PRINT LARGEST POSSIBLE VALUE FORMED FROM GIVEN VALUES '''
a=int(input())
i_string=input()
l=i_string.split()
l.sort()
for i in range(len(l)-1,-1,-1):
  print(l[i],end="")
