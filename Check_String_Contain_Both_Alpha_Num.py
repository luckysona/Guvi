''' CHECK THAT THE STRING CONTAIN BOTH ALPHABETS AND NUMBERS '''
str=input()
a=b=0;
for i in str:
    if i.isalpha():
        b+=1 
    elif i.isnumeric():
        a+=1 
if(a>=1 and b>=1):
    print("Yes")
else:
    print("No")
