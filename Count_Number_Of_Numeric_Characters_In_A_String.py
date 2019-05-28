''' PROGRAM TO COUNT NUMBER OF VALUES OCCURS IN A STRING '''
a=input()
b=0
i=0
while(i<10):
  b+=a.count(str(i))
  i+=1
print(b)
