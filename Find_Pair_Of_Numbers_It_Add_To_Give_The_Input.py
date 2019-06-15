''' PROGRAM TO PAIR OF NUMBERS IT ADDS TO GET GIVEN INPUT '''
a,b=list(map(int,input().split()))
l=list(map(int,input().split()))
c=0
for i in l:
  if (b-i) in l:
    print('yes')
    c=1
    break
if(c==0):
  print('no')
