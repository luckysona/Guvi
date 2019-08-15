''' CHECK THAT GIVEN TWO STRINGS DIFFER BY K CHARACTERS '''
str1,str2,k=input().split()
list1=list(str1)
list2=list(str2)
k=int(k)
count=0
for i in range(0,len(list1)):
  if(list1[i]!=list2[i]):
    count+=1
if(count==k):
  print('yes')
else:
  print('no')
