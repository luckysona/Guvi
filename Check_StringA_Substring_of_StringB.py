''' CHECK ANY PART OF STRING_A IS A SUBSTING OF STRING_B '''
str1,str2=map(str,input().split())
count=0
for i in range(0,len(str1)):
    for j in range(0,len(str2)):
        if str1[i]==str2[j]:
            count+=1
if count>=2:
    print("yes")
else:
    print("no")
