''' COUNT THE NUMBER OF SPECAIL CHARACTER IN THE GIVEN STRING '''
str = input() 
count=0
for i in range(len(str)):
  if(str[i].isalpha() or str[i].isdigit() or str[i]==" "):
    continue 
  else:
    count=count+1
print(count)
