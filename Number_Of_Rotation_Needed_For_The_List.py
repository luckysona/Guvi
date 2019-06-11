''' PROGRAM TO FIND THE NUMBER OF ROTATION NEEDED FOR THE LIST TO OBTAIN REQUIRED LIST '''
a=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
i=k.index(l[0])
print(a-i)
