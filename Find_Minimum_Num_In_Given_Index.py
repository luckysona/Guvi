s1,b=map(int,input().split())
L=list(map(int,input().split()))
temp=[]
for i in range(b):
    d=list(map(int,input().split()))
    l=d[0]
    for j in range(min(d)-1,max(d)):
        if l>L[j]:
        	l=L[j]
    temp.append(l)
for i in range(0,len(temp)):
    print(temp[i])
