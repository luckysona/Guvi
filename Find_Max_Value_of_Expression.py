''' FIND THE MAXIMUM VALUE BY USING THE FOLLOWING EXPRESSION P*ai+Q*aj+R*ak(i<=j<=k) '''
N,P,Q,R=map(int,input().split())
list=list(map(int,input().split()))
L=[]
for i in range(0,len(list)):
    for j in range(i,len(list)):
        for k in range(j,len(list)):
            L.append(P*list[i]+Q*list[j]+R*list[k])
print(max(L))
