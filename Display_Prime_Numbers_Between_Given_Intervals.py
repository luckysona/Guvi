''' PROGRAM TO DISPLAY PRIME NUMBER BETWEEN GIVEN NUMBERS '''
a,b=input().split()
a=int(a)
b=int(b)
for num in range(a+1,b):
   if (num>1):
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num,end=' ')
