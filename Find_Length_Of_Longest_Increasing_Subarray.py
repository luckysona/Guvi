''' PROGRAM TO FIND THE LONGEST INCREASING SUBARRAY ''' 
a=int(input())
l=list(map(int,input().split()))
s=[]
a1=1
for i in range(0,a-1):
    if (l[i]<l[i+1]):
        a1+=1
    else:
        s.append(a1)
        a1=1
s.append(a1)
print(max(s))
