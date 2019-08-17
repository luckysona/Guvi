s1=str(input())
k=[]
a=""
r=0
for i in range(0,len(s1)):
    for j in range(i,len(s1)):
        a=a+s1[j]
        if(a[::-1]==a):
            r=len(s1)-len(a)
            k.append(r)
    a=""
print(min(k))
