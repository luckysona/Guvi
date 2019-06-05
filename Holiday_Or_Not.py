''' PROGRAM TO PRINT THE GIVEN DAY IS HOLIDAY OR NOT '''
l1=['Monday','Tuesday','Wednesday','Thursday','Friday']
l2=['Saturday','Sunday']
a=input().split()
for i in a:
  if i in l2:
    print("yes")
  elif i in l1:
    print("no")
