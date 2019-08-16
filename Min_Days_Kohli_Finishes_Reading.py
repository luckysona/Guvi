''' DETERMINE THE MINIMUM NO OF DAYS THAT KOHLI FINISHES READING '''
N,T=map(int,input().split())
sec=list(map(int,input().split()))[:N]
count=0
for i in sec:
  t1=86400-i
  T=T-t1
  count+=1
  if T<=0:
    break  
print(count)
