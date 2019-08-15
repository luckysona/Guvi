''' CHECK THE K VALUE IN THE GIVEN LIST '''
n,k=map(int,input().split())
arr=list(map(int,input().split()))[:n]
b=0
for i in range(0,len(arr)):
  if(arr[i]==k):
    b=1
if(b==1):
  print('yes')
else:
