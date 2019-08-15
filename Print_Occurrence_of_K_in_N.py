''' PRINT THE OCCURRENCES OF K IN GIVEN N NUMBERS '''
N,K=input().split()
a=list(N)
K=int(K)
c=0
for i in range(0,len(a)):
  if(int(a[i])==K):
    c+=1
print(c)
