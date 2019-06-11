''' PROGRAM TO GET SUBSTRINGS OF GIVEN STRING IN REQUIRED LENGTH '''
a,b=map(str,input().split())
b=int(b)
l=[]
for i in range((len(a)-b)+1):
	l.append(a[i:i+b])
print(" ".join(l))
