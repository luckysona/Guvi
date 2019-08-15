''' PRINT SORTD ARRAY IN IMPROVED INPUT CONSTRAINTS ''' 
num=int(input())
arr=input()
list=list(map(int,arr.split(' ')))
list.sort()
if(num<=100000):
  for i in list:
    print(i,end=' ')
