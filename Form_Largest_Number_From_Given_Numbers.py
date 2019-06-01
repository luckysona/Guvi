''' PROGRAM TO PRINT LARGEST POSIBLE VALUE FORMED FROM GIVEN VALUES '''
a=int(input())
i_string=input()
l=i_string.split()
l.sort()
c=l.count('0')
for i in range(len(l)-1,-1,-1):
  print(l[i],end="")
  if(c==len(l)):
    break
