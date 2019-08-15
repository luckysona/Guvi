''' PRINT EVEN FACTORS OF THE GIVEN NUMBER '''
num=int(input())
list=[]
for i in range(1,num+1):
  if(num%i==0 and i%2==0):
    list.append(i)
print(*list)
