''' PROGRAM TO FIND PALINDROME OR NOT '''
a=int(input())
tem=a
rev=0
while(a!=0):
    r=a%10
    rev=(rev*10)+r
    a=a//10
if(tem==rev):
  print("yes")
else:
  print("no")
