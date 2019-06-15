''' PROGRAM TO FIND LENGTH OF LONGEST INCREASING SUBSEQUENCE '''
a=int(input())
l=list(map(int,input().split()))
c=[]
c1=1
for i in l:
  if i not in c:
    c.append(i)
for i in range(len(c)-1):
  if (c[i]<c[i+1]):
    c1+=1
print(c1)
