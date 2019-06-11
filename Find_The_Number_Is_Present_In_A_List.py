''' PROGRAM TO FIND THE GIVEN NUMBER IS PRESENT IN A LIST '''
a,b=input().split()
l=list(map(int,input().split()))
if int(b) in l:
  print("Yes")
else:
  print("No")
