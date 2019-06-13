''' PROGRAM TO PRINT REPEATED LETTER IN A STRING '''
a=input()
c=[]
for i in a:
  if(a.count(i)>1):
    c.append(i)
print(c[0])
