''' CHECK VOWELS ARE PRESENT IN THE GIVEN STRING OR NOT '''
str=input()
list=['a','e','i','o','u']
a=0
for i in str:
  if i in list:
    a=1
  else:
    a=0
if(a==1):
  print('yes')
else:
  print('no')
