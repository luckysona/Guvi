''' PRINT THE SUM OF ALL ITS DIGITS IN GIVEN NUMBER '''
num=input()
list=list(num)
s=0
for i in range(0,len(list)):
  s=s+int(list[i])
print(s)
