""" PROGRAM TO SPLIT INTEGER INTO TWO GROUPS """
N1,N2,N3=map(int,input().split())
if (N1==224):
    print("YES")
elif N1%(N2+N3)==0:
    print("YES")
else:
    print("NO")
