''' PROGRAM TO CHECK THE GIVEN LIST IS ABLE TO SPLIT INTO TWO LIST WITH SAME AVERAGE '''
a=int(input())
l=list(map(int,input().split()))
avg=int(a/2)
l1=l[:avg]
l2=l[avg::]
if ((sum(l1)//len(l1))==(sum(l2)//len(l2))):
    print("yes")
else:
    print("no")
