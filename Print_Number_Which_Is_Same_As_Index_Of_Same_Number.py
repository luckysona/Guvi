''' PROGRAM TO FIND THE GIVEN NUMBER IS SAME AS THE INDEX NUMBER '''
a=int(input())
i_string=input()
l=i_string.split()
b=[]
for i in range(0,len(l)):
  if(i==int(l[i])):
    b.append(i)
for i in b:
  print(i,end=" ")
if(len(b)==0):
  print('-1')
