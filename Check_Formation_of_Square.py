''' CHECK THE GIVEN NUMBERS FORMS THE SQUARE OR NOT '''
a1,a2=map(int,input().split())
b1,b2=map(int,input().split())
c1,c2=map(int,input().split())
d1,d2=map(int,input().split())
m=b2-a2
n=c2-d2
o=c1-b1
p=d1-a1
if m==n==o==p:
    print("yes")
else:
    print("no")
