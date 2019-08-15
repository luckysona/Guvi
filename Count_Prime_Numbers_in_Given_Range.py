''' COUNT THE NUMBER OF PRIME NUMBERS IN THE GIVEN RANGE '''
l,r=map(int,input().split())
list = list()
for i in range(l,r+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        list.append(i)
print(len(list))
