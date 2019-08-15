''' PRINT THE ARRAY ELEMENT IN SINGE LINE BY DECREASING ORDER OF NUMBER OF ONES IN BINARY REPRESENTATION '''
str1=int(input())  
str2=[int(i) for i in input().split()]
str2=[bin(i)[2:] for i in  str2]  
str2.sort(reverse=True) 
new_str=[int(i,2) for i in str2]
for i in new_str:
	print(i)
