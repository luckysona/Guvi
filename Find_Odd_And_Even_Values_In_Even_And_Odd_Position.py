''' PROGRAM TO FIND ODD VALUES IN EVEN POSITION AND EVEN VALUE IN ODD POSITION '''
a=int(input())
i_string=input()
l=i_string.split()
for i in range(0,len(l)):
  if(i%2!=0):
    if(int(l[i])%2==0):
      print(int(l[i]),end=" ")
  elif(i%2==0):
    if(int(l[i])%2!=0):
      print(int(l[i]),end=" ")
    
