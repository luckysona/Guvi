''' PROGRAM TO SORT IN GIVEN ELEMENTS USING LIST '''
a=int(input())
input_string = input()
list=input_string.split()
list.sort()
for i in list:
  print(i,end=" ")
