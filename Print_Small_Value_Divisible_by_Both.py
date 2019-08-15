''' PRINT THE SMALLEST NUMBER DIVISIBLE BY BOTH L AND R '''
L,R=map(int,input().split())
for i in range(1,10000):
  if(i%L==0 and i%R==0):
    print(i)
    break
