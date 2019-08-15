''' PRINT THE ARRAY AFTER RIGHT SHIFT K TIMES '''
N,K=input().split()
N=int(n)
K=int(k)
arr=list(map(int,input().split()))[:n]
K=K%n
list=arr[-K:]+arr[:-K]
print(*list)
