''' PROGRAM TO PRINT UNIQUE LETTERS IN A STRING '''
a=input()
l=""
for i in a:
  if i not in l:
    l+=i
print(l)
