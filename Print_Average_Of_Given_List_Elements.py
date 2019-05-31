''' PROGRAM TO PRINT AVERAGE OF GIVEN LIST ELEMENTS '''
istring=input()
l=istring.split()
s=0
for i in  range(0,len(l)):
  s+=int(l[i])
a=s//len(l)
print(a)
