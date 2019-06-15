''' PROGRAM TO PRINT NUMBER OF WAYS TO REACH THE TOP '''
n = int(input())
def fact(n):
  if (n==0):
    return 1
  else:
    a=1
    for i in range(1,n+1):
      a*=i
    return a
if (n<=2):
  print(n)
else:
  print((n+(fact(n)//(fact(n-2)*fact(2))))//2)
