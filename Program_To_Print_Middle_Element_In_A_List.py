''' PROGRAM TO MIDDLE ELEMENT USING LIST '''
a=int(input())
input_string = input()
list=input_string.split()
list.sort()
i=len(list)//2
print(list[i])
