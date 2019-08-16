''' HELP DHONI TO DESTORY ALL TANKS USING FEW BOMBS ''' 
N = int(input())
list = []
a = N//2 + N
for i in range(1,N+1):
  if i%2==0:
    list.append(i)
for i in range(1,N+1):
  if i%2!=0:
    list.append(i)
for i in range(1,N+1):
  if i%2==0:
    list.append(i)
print(a)
print(*list)
