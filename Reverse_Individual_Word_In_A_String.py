""" PROGRAM TO REVERSE INDIVIDUAL WORDS IN A STRING """
def rev(s): 
  str="" 
  for i in s: 
    str=i+str
  return str
a=input().split()
for i in a:
  print(rev(i),end=" ")
