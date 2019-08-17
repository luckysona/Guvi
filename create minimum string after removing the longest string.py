s1=str(input())
L=[]
a=""
r=0
for i in range(0,len(s1)):
    for j in range(i,len(s1)):
        a=a+s1[j]
        if(a[::-1]==a):
            r=len(s1)-len(a)
            L.append(r)
    a=""
print(min(L))
