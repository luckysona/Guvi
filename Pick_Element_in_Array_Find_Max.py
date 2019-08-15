''' FIND THE MAXIMUM SUM BY PICKING THE ELEMENT OF AN ARRAY BASED ON THE GIVEN RULE '''
num=int(input())
list=list(map(int,input().split()))
L=[]
d=0
for i in range(0,num-2):
	for j in range(i,num,2):
		d=d+list[j]
	L.append(d)
	d=0
L.sort()
print(L[-1])
