''' PRINT THE NUMBER OF REPETITIONS OF K VALUE IN GIVEN LIST '''
n,k=map(int,input().split())
arr=list(map(int,input().split()))[:n]
c=0
for i in range(0,len(arr)):
  if(arr[i]==k):
    c+=1
print(c)
