''' PRINT PRIME FACTORS FOR THE GIVEN N VALUE IN SORTED ORDER '''
N=int(input())
L=[]
B=True
for i in range(2,N+1):
  if(N%i==0):
    L.append(i)
for i in L:
  for j in range(2,i):
    if(i%j==0):
      B=False
  if B is True:
      print(i,end=" ")
