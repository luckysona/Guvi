''' PROGRAM TO CHECK THE LARGEST AMONG THREE NUMBERS BY USER '''
a=int(input())
b=int(input())
c=int(input())
if(a>b):
  if(a>c):
    print(a)
  else:
    print(c)
elif(b>c):
  print(b)
elif(c>b):
  print(c)
elif(a==b and b==c):
  print(a)
elif(a==b):
  print(a)
elif(b==c):
  print(b)
else:
  print(c)
