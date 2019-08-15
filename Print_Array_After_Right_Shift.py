''' PRINT THE ARRAY AFTER RIGHT SHIFT K TIMES '''
N,K=input().split()
N=int(N)
K=int(K)
arr=list(map(int,input().split()))[:N]
K=K%N
list=arr[-K:]+arr[:-K]
print(*list)
