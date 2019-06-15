''' PROGRAM TO FIND THE SECOND INPUT IS SUBSTRING OF FIRST INPUT STRING '''
a,b=input().split()
c=0
for i in range(0,len(b)):
  if b[i] in a:
    c+=1
if(c==len(b)):
  print("yes")
else:
  print("no")
