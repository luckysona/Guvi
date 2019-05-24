''' PROGRAM TO CHECK THE YEAR IS LEAP YEAR OR NOT '''
i=int(input())
if(i%4==0):
  if(i%100==0):
    if(i%400==0):
      print("yes")
    else:
      print("no")
  else:  
    print("yes")
else:
  print("no")
