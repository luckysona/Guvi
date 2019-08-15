''' COUNT NUMBER OF DIGITS IN THE GIVEN INTEGER '''
num=input()
list=list(map(int,num))
c=0
for i in range(0,len(list)):
  c+=1
print(c)
