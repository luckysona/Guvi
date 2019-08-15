''' PRINT THE LONGEST SUBSTRING FOR THE GIVEN STRING IN LEXICOGRAPHICALLY '''
str=input()
for i in range(len(str)):
	if(str[i]<str[i+1]):
		print(str[i+1:])
		break
