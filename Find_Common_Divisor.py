''' FIND THE NUMBER OF COMMON DIVISOR FOR THE GIVEN STRING '''
str1=input()
str2=input()
import sys
if len(str1)>len(str2):
  print(1)
  sys.exit(0)
A=[]
s=''
for i in range(len(str1)):
  if str1[i] not in A:
    s+=str1[i]
    A.append(str1[i])
c=0
c=len(str1)//len(s)
d=1
for i in range(2,c+1):
  if c%i==0:
    d+=1
print(d)
