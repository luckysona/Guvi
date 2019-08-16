''' CHECK GIVEN SENTENCE IS A PANGRAM OR NOT '''
sen=str(input())
sen=sen.lower()
l=len(sen)
L=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(0,l):
	if(sen[i] in L):
		L.remove(sen[i])
if(len(L)==0):
	print("yes")
else:
	print("no")
