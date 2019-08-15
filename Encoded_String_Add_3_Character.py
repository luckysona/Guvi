''' PRINT ENCODED STRING BY ADDING 3 TO THE EACH CHARACTER '''
str=input()
new_str=''
for i in str:
    if i=="X":
        new_str+="A"
    elif i=="x":
        new_str+="a"
    elif i=="Y":
        new_str+="B"
    elif i=="y":
         new_str+="b"
    elif i=="Z":
        new_str+="C"
    elif i=="z":
        new_str+="c"
    else:
        new_str+=chr(ord(i)+3)
print(new_str)
