''' PROGRAM TO FIND THE FIRST REPEATED NUMBER '''
a=int(input())
i_string=input()
l=i_string.split()
for i in range(0,len(l)):
  c=l.count(l[i])
  if(c>1):
    print(l[i])
    break
