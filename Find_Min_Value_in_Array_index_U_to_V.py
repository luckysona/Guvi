''' FIND THE MINIMUM OF ALL VALUES OF THE ARRAY FROM THE INDEX U TO V '''
str1,str2=map(int,input().split())
List=[int(i) for i in input().split()]
temp=[]
for i in range(str2):
    d=list(map(int,input().split()))
    l=d[0]
    for j in range(min(d)-1,max(d)):
        if l>List[j]:
        	l=List[j]
    temp.append(l)
for i in range(0,len(temp)):
    print(temp[i])
