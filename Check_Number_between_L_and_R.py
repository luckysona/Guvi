''' CHECK THE NUMBER LIE BETWEEN L AND R OR NOT '''
N=int(input())
L,R=map(int,input().split())
a=False
for i in range(L+1,R):
  if(i==N):
    a=True
if(a==True):
  print('yes')
else:
  print('no')
