''' PROGRAM TO PRINT REPEATED NUMBERS '''
a=int(input())
b=[]
l=list(map(int,input().split()))
for i in l:
    if l.count(i)>1:
        b.append(i)
c=set(b)
if(len(c)==0):
    print("unique")
else:
    print(*c)
