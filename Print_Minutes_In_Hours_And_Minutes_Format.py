''' PROGRAM TO PRINT MIN IN TIME FORMAT '''
m=int(input())
h=0
if(m<=59):
  print(h,m)
else:
  while(m>59):
    m-=60
    h+=1
  print(h,m)
