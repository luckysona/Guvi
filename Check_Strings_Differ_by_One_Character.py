''' CHECK THE GIVEN STRINGS ARE DIFFER BY ONLY ONE CHARACTER '''
str1,str2=map(str,input().split())
count=0
for i in range(0,len(str1)):
  if(str1[i]!=str2[i]):
    count=count+1
  else:
    continue
if(count==1):
  print('yes')
else: 
  print('no')
