''' CHECK VOWELS ARE PRESENT IN THE GIVEN STRING OR NOT '''
str=input()
a=list(str)
list=['a','e','i','o','u']
b=False
for i in range(0,len(a)):
  for j in range(0,len(list)):
    if(a[i]==list[j]):
      b=True
      break
if(b==True):
  print('yes')
else:
  print('no')
