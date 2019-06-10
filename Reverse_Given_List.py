''' PROGRAM TO REVERSE GIVEN LIST '''
a=int(input())
l=input().split()
for i in range((a-1),-1,-1):
  print(l[i],end="")
  if(i>0):
    print("->",end="")
