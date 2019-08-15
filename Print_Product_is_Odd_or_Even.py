''' PRINT THE PRODUCT OF GIVEN TWO NUMBER IS ODD OR EVEN '''
N1,N2=map(int,input().split())
p=N1*N2
if(p%2==0):
  print('even')
else:
  print('odd')
