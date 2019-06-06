''' PROGRAM TO FIND UNREPEATED NUMBER IN LIST '''
a=int(input())
b=input().split()
for i in range(len(b)):
    if (b.count(b[i])==1):
        print(b[i])
        break
