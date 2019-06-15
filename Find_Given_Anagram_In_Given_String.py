''' PROGRAM TO FIND NUMBER OF ANAGRAM IN GIVEN STRING MATCHES '''
a=int(input())
l=[]
c=['k','a','b','a','l','i']
a1=0
for i in range(0,a):
  l.append(input())
for i in l:
  c1=0
  for j in range(0,len(i)):
    if i[j] in c:
      c1+=1
  if(c1==6):
    a1+=1
print(a1)
